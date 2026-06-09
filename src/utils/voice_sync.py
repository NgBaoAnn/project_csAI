import subprocess
from pathlib import Path
from manim import Scene

def get_audio_duration(path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        str(path)
    ]
    try:
        out = subprocess.check_output(cmd, text=True, timeout=10).strip()
        return float(out)
    except Exception as exc:
        print(f"[WARN] Lỗi ffprobe cho {path}: {exc}")
        return 3.0

def play_voiceover_and_wait(scene: Scene, scene_num: int, seg_idx: int):
    """
    Nạp audio segment vào Manim scene và chờ đọc xong.
    Ghi thời gian thực (scene.renderer.time) vào timings.txt để
    generate_voiceover.py dùng đặt audio đúng vị trí.
    """
    cwd = Path.cwd()
    if (cwd / "output" / "audio").exists():
        base_dir = cwd
    elif (cwd.parent / "output" / "audio").exists():
        base_dir = cwd.parent
    else:
        print("[WARN] output/audio dir not found")
        return

    seg_dir = base_dir / "output" / "audio" / f"scene_{scene_num:02d}"
    if not seg_dir.exists():
        print(f"[WARN] audio dir missing: {seg_dir}")
        return

    mp3_files = list(seg_dir.glob(f"seg_{seg_idx:02d}_*.mp3"))
    if not mp3_files:
        print(f"[WARN] seg_{seg_idx:02d} not found in {seg_dir}")
        return

    mp3_path = mp3_files[0]

    # Ghi thời gian thực vào timings.txt
    # seg_idx == 0 → ghi mới (xóa cũ), còn lại → append
    actual_time = scene.renderer.time
    timing_file = seg_dir / "timings.txt"
    mode = "w" if seg_idx == 0 else "a"
    with open(timing_file, mode) as f:
        f.write(f"{seg_idx},{actual_time:.3f}\n")

    scene.add_sound(str(mp3_path))
    dur = get_audio_duration(str(mp3_path))
    scene.wait(dur + 0.1)
