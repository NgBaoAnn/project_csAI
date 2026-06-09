"""
Compile TV4 Scenes (31 to 40)
Author: Animation Assistant
Usage: run from project root using: venv/Scripts/python src/compile_tv4_scenes.py
"""

import os
import sys
import subprocess
import shutil

SCENES = [
    ("scene_31_crop_yield.py", "CropYieldScene", "scene_31_crop_yield.mp4"),
    ("scene_32_covid_mortality.py", "COVIDMortalityScene", "scene_32_covid_mortality.mp4"),
    ("scene_33_no_env_labels.py", "NoEnvLabelsScene", "scene_33_no_env_labels.mp4"),
    ("scene_34_hrm_loop.py", "HRMLoopScene", "scene_34_hrm_loop.mp4"),
    ("scene_35_colored_mnist.py", "ColoredMNISTScene", "scene_35_colored_mnist.mp4"),
    ("scene_36_hard_noisy_samples.py", "HardNoisySamplesScene", "scene_36_hard_noisy_samples.mp4"),
    ("scene_37_geometric_wasserstein.py", "GeometricWassersteinScene", "scene_37_geometric_wasserstein.mp4"),
    ("scene_38_error_slices.py", "ErrorSlicesScene", "scene_38_error_slices.mp4"),
    ("scene_39_stability_feature.py", "StabilityFeatureScene", "scene_39_stability_feature.mp4"),
    ("scene_40_deployment_conclusion.py", "DeploymentConclusionScene", "scene_40_deployment_conclusion.mp4"),
]

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_dir = os.path.join(project_root, "src")
    output_dir = os.path.join(project_root, "output")
    tv4_dest_dir = os.path.join(output_dir, "tv4_scenes")
    
    # Create destination directory if not exists
    os.makedirs(tv4_dest_dir, exist_ok=True)
    
    print("=" * 60)
    print("BATCH COMPILING SCENES 31 TO 40 (TV4)")
    print(f"Project Root: {project_root}")
    print(f"Output Directory: {tv4_dest_dir}")
    print("=" * 60)
    
    python_exe = sys.executable
    print(f"Using Python: {python_exe}\n")
    
    success_count = 0
    
    for filename, class_name, out_name in SCENES:
        file_path = f"scenes/{filename}"
        print(f"--> Compiling {filename} ({class_name})...")
        
        # Execute manim render command via python -m manim
        # We run it in 'src' directory where manim.cfg is located
        cmd = [
            python_exe, "-m", "manim",
            "-ql",  # Low quality, fast compile (15 fps)
            file_path,
            class_name
        ]
        
        result = subprocess.run(cmd, cwd=src_dir, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"    Compile Successful!")
            # Locate file in output/media/videos/{filename_base}/480p15/{class_name}.mp4
            file_base = os.path.splitext(filename)[0]
            src_video = os.path.join(output_dir, "media", "videos", file_base, "480p15", f"{class_name}.mp4")
            dest_video = os.path.join(tv4_dest_dir, out_name)
            
            if os.path.exists(src_video):
                shutil.copy2(src_video, dest_video)
                print(f"    Copied & Renamed to: output/tv4_scenes/{out_name}")
                success_count += 1
            else:
                print(f"    Warning: Compiled successfully, but could not find output video at:\n    {src_video}")
        else:
            print(f"    [ERROR] Failed compiling {filename}")
            print(result.stderr)
            print("-" * 40)
            
    print("\n" + "=" * 60)
    print(f"Compilation finished. Successfully built: {success_count}/{len(SCENES)} scenes.")
    print(f"Outputs saved in: output/tv4_scenes/")
    print("=" * 60)

if __name__ == "__main__":
    main()
