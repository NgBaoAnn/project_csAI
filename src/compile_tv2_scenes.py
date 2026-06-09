"""
Compile TV2 Scenes (11 to 20)
Author: Animation Assistant
Usage: run from project root using: venv/Scripts/python src/compile_tv2_scenes.py
"""

import os
import sys
import subprocess
import shutil

SCENES = [
    ("scene_11_hidden_subpopulations.py", "HiddenSubpopulationsScene", "scene_11_hidden_subpopulations.mp4"),
    ("scene_12_pipeline_view.py", "PipelineViewScene", "scene_12_pipeline_view.mp4"),
    ("scene_13_erm_formula.py", "ERMFormulaScene", "scene_13_erm_formula.mp4"),
    ("scene_14_average_risk.py", "AverageRiskScene", "scene_14_average_risk.mp4"),
    ("scene_15_spurious_cow_camel.py", "SpuriousCowCamelScene", "scene_15_spurious_cow_camel.mp4"),
    ("scene_16_dro_intuition.py", "DROIntuitionScene", "scene_16_dro_intuition.mp4"),
    ("scene_17_uncertainty_set.py", "UncertaintySetScene", "scene_17_uncertainty_set.mp4"),
    ("scene_18_f_divergence.py", "FDivergenceScene", "scene_18_f_divergence.mp4"),
    ("scene_19_wasserstein.py", "WassersteinScene", "scene_19_wasserstein.mp4"),
    ("scene_20_dro_limits.py", "DROLimitsScene", "scene_20_dro_limits.mp4"),
]

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_dir = os.path.join(project_root, "src")
    output_dir = os.path.join(project_root, "output")
    tv2_dest_dir = os.path.join(output_dir, "tv2_scenes")
    
    # Create destination directory if not exists
    os.makedirs(tv2_dest_dir, exist_ok=True)
    
    print("=" * 60)
    print("BATCH COMPILING SCENES 11 TO 20 (TV2)")
    print(f"Project Root: {project_root}")
    print(f"Output Directory: {tv2_dest_dir}")
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
            dest_video = os.path.join(tv2_dest_dir, out_name)
            
            if os.path.exists(src_video):
                shutil.copy2(src_video, dest_video)
                print(f"    Copied & Renamed to: output/tv2_scenes/{out_name}")
                success_count += 1
            else:
                print(f"    Warning: Compiled successfully, but could not find output video at:\n    {src_video}")
        else:
            print(f"    [ERROR] Failed compiling {filename}")
            print(result.stderr)
            print("-" * 40)
            
    print("\n" + "=" * 60)
    print(f"Compilation finished. Successfully built: {success_count}/{len(SCENES)} scenes.")
    print(f"Outputs saved in: output/tv2_scenes/")
    print("=" * 60)

if __name__ == "__main__":
    main()
