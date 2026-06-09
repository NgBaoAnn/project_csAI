"""
Compile TV3 Scenes (21 to 30)
Author: TV3 (Animation Lead)
Usage: run from project root using: venv/Scripts/python src/compile_tv3_scenes.py
"""

import os
import sys
import subprocess
import shutil

SCENES = [
    ("scene_21_invariant_features.py", "InvariantFeaturesScene", "scene_21_invariant_features.mp4"),
    ("scene_22_irm_objective.py", "IRMObjectiveScene", "scene_22_irm_objective.mp4"),
    ("scene_23_irm_limits.py", "IRMLimitsScene", "scene_23_irm_limits.mp4"),
    ("scene_24_clip_contrastive.py", "CLIPContrastiveScene", "scene_24_clip_contrastive.mp4"),
    ("scene_25_more_data_not_right_data.py", "MoreDataNotRightDataScene", "scene_25_more_data_not_right_data.mp4"),
    ("scene_26_deductive_inductive.py", "DeductiveInductiveScene", "scene_26_deductive_inductive.mp4"),
    ("scene_27_income_ca_pr.py", "IncomeCaPrScene", "scene_27_income_ca_pr.mp4"),
    ("scene_28_ambiguity_variables.py", "AmbiguityVariablesScene", "scene_28_ambiguity_variables.mp4"),
    ("scene_29_mutual_information.py", "MutualInformationScene", "scene_29_mutual_information.mp4"),
    ("scene_30_predictive_heterogeneity.py", "PredictiveHeterogeneityScene", "scene_30_predictive_heterogeneity.mp4"),
]

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_dir = os.path.join(project_root, "src")
    output_dir = os.path.join(project_root, "output")
    tv3_dest_dir = os.path.join(output_dir, "tv3_scenes")
    
    # Create destination directory if not exists
    os.makedirs(tv3_dest_dir, exist_ok=True)
    
    print("=" * 60)
    print("BATCH COMPILING SCENES 21 TO 30")
    print(f"Project Root: {project_root}")
    print(f"Output Directory: {tv3_dest_dir}")
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
            dest_video = os.path.join(tv3_dest_dir, out_name)
            
            if os.path.exists(src_video):
                shutil.copy2(src_video, dest_video)
                print(f"    Copied & Renamed to: output/tv3_scenes/{out_name}")
                success_count += 1
            else:
                print(f"    Warning: Compiled successfully, but could not find output video at:\n    {src_video}")
        else:
            print(f"    [ERROR] Failed compiling {filename}")
            print(result.stderr)
            print("-" * 40)
            
    print("\n" + "=" * 60)
    print(f"Compilation finished. Successfully built: {success_count}/{len(SCENES)} scenes.")
    print(f"Outputs saved in: output/tv3_scenes/")
    print("=" * 60)

if __name__ == "__main__":
    main()
