"""
Compile TV1 Scenes (1 to 10)
Author: Animation Assistant
Usage: run from project root using: venv/Scripts/python src/compile_tv1_scenes.py
"""

import os
import sys
import subprocess
import shutil

SCENES = [
    ("scene_01_accuracy_fail.py", "AccuracyFailScene", "scene_01_accuracy_fail.mp4"),
    ("scene_02_failure_montage.py", "FailureMontageScene", "scene_02_failure_montage.mp4"),
    ("scene_03_model_or_data.py", "ModelOrDataScene", "scene_03_model_or_data.mp4"),
    ("scene_04_iid_box.py", "IIDBoxScene", "scene_04_iid_box.mp4"),
    ("scene_05_train_test_split.py", "TrainTestSplitScene", "scene_05_train_test_split.mp4"),
    ("scene_06_shift_taxonomy.py", "ShiftTaxonomyScene", "scene_06_shift_taxonomy.mp4"),
    ("scene_07_x_shift.py", "XShiftScene", "scene_07_x_shift.mp4"),
    ("scene_08_yx_shift.py", "YXShiftScene", "scene_08_yx_shift.mp4"),
    ("scene_09_data_sources.py", "DataSourcesScene", "scene_09_data_sources.mp4"),
    ("scene_10_pooled_illusion.py", "PooledIllusionScene", "scene_10_pooled_illusion.mp4"),
]

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_dir = os.path.join(project_root, "src")
    output_dir = os.path.join(project_root, "output")
    tv1_dest_dir = os.path.join(output_dir, "tv1_scenes")
    
    # Create destination directory if not exists
    os.makedirs(tv1_dest_dir, exist_ok=True)
    
    print("=" * 60)
    print("BATCH COMPILING SCENES 1 TO 10 (TV1)")
    print(f"Project Root: {project_root}")
    print(f"Output Directory: {tv1_dest_dir}")
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
            dest_video = os.path.join(tv1_dest_dir, out_name)
            
            if os.path.exists(src_video):
                shutil.copy2(src_video, dest_video)
                print(f"    Copied & Renamed to: output/tv1_scenes/{out_name}")
                success_count += 1
            else:
                print(f"    Warning: Compiled successfully, but could not find output video at:\n    {src_video}")
        else:
            print(f"    [ERROR] Failed compiling {filename}")
            print(result.stderr)
            print("-" * 40)
            
    print("\n" + "=" * 60)
    print(f"Compilation finished. Successfully built: {success_count}/{len(SCENES)} scenes.")
    print(f"Outputs saved in: output/tv1_scenes/")
    print("=" * 60)

if __name__ == "__main__":
    main()
