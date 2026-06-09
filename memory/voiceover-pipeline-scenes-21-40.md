---
name: voiceover-pipeline-scenes-21-40
description: User's manim OOD video project — voiceover assignment, pipeline, and completion status
metadata:
  type: project
---

User được phân làm voiceover (giọng Adam ElevenLabs, tiếng Việt) cho **scene 21–40** của video manim về OOD Generalization. Tính tới 2026-06-09, **toàn bộ 21–40 đã hoàn thành**: mỗi scene có lời giới thiệu tiêu đề (seg 0) + narration đồng bộ animation; scene 40 có thêm card "Cảm ơn các bạn đã lắng nghe".

**Quy trình chuẩn 3 bước cho mỗi scene (chạy từ root):**
1. `python src/generate_voiceover.py --scenes XX --audio-only` → tạo mp3 segment
2. `cd src && python -m manim -ql scenes/scene_XX_*.py ClassName` → render + ghi `output/audio/scene_XX/timings.txt`
3. `python src/generate_voiceover.py --scenes XX` → ghép `output/final/scene_XX_with_voice.mp4`

**Cơ chế khớp tiếng:** [src/utils/voice_sync.py](../src/utils/voice_sync.py) `play_voiceover_and_wait(self, scene, seg_idx)` phát audio đúng vị trí animation và ghi thời gian thực vào timings.txt. [src/generate_voiceover.py](../src/generate_voiceover.py) `build_audio_track` đọc timings.txt để đặt tiếng đúng chỗ (không dùng mốc đoán), và độ dài track = `max(duration, segment_cuối + 0.5)` để không cắt câu insight.

**Gotchas Windows:** mỗi scene + generate_voiceover.py cần `sys.stdout.reconfigure(encoding='utf-8')` ở đầu file, nếu không print tiếng Việt sẽ lỗi charmap. API key ElevenLabs hard-code trong generate_voiceover.py.
