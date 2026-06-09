"""
generate_voiceover.py
=====================
Tạo voiceover cho scenes 21-30 bằng OpenAI TTS, sau đó ghép vào video Manim qua FFmpeg.

Pipeline:
    1. Đọc narration text đã căn chỉnh timing theo từng scene
    2. Gọi OpenAI TTS → xuất MP3 cho từng đoạn narration
    3. Dùng ffmpeg adelay để đặt đúng vị trí thời gian trong audio track
    4. Ghép audio track vào video Manim → output/final/scene_XX_with_voice.mp4

Yêu cầu:
    pip install openai
    ffmpeg phải có trong PATH (https://ffmpeg.org/download.html)

Cách dùng:
    # 1. Đặt API key
    set OPENAI_API_KEY=sk-...

    # 2. [Tuỳ chọn] Render Manim trước
    cd src
    python -m manim -ql scenes/scene_21_invariant_features.py InvariantFeaturesScene

    # 3. Tạo audio + ghép video
    python generate_voiceover.py --scenes 21-30

    # 4. Hoặc chỉ tạo audio (nếu chưa có video)
    python generate_voiceover.py --scenes 21-30 --audio-only

    # 5. Chỉ một scene:
    python generate_voiceover.py --scenes 21

Kết quả:
    output/audio/scene_XX/   — các file MP3 segment
    output/final/scene_XX_with_voice.mp4  — video cuối đã có voice
"""

import os
import sys
import time
import argparse
import subprocess
from pathlib import Path

# Fix Windows stdout encoding for Vietnamese characters
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import requests
import json

# ─────────────────────────── CẤU HÌNH ───────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR      = PROJECT_ROOT / "src"
AUDIO_DIR    = PROJECT_ROOT / "output" / "audio"
FINAL_DIR    = PROJECT_ROOT / "output" / "final"

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
FINAL_DIR.mkdir(parents=True, exist_ok=True)

# Cấu hình ElevenLabs
ELEVENLABS_API_KEY = "49ed90f02548cf8d1fb3ffd6270a0a9e24c0964e4aed5b2fb7615cf0fc27de15"
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam
TTS_VOICE = "Adam (ElevenLabs)"
TTS_MODEL = "eleven_turbo_v2_5"
TTS_FORMAT = "mp3"

# ──────────────────────── TIMING ANALYSIS ────────────────────────────────────
#
# Mỗi voice_segment có dạng: (start_sec, text)
# start_sec: giây trong video bắt đầu đọc narration này
#
# Timing được tính bằng cách cộng dồn:
#   - run_time của các animation
#   - self.wait(t) 
#   - animate_title_card mặc định ~4.2s (1s Create + 1.2s Write + 1.5s wait + 0.5s FadeOut)
#
# ─────────────────────────────────────────────────────────────────────────────

SCENE_NARRATIONS = {

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 21 – Invariant Features
    # Duration: ~70s
    # Timeline:
    #   0.0  – Title card intro (Create frame 1s + Write 1.2s + wait 1.5s + FadeOut 0.5s + wait 1.0s) = ~5.2s
    #   5.2  – FadeIn sub1 + wait 4.0s = 9.2s
    #   9.2  – FadeIn env1 box (1s) + bg/shape (1s) + wait 3.5s = 14.7s
    #   14.7 – FadeIn env2 box (1s) + bg/shape (1s) + wait 3.5s = 20.2s
    #   20.2 – FadeIn env3 box (1s) + bg/shape (1s) + wait 5.0s = 27.2s
    #   27.2 – Transform sub2 + wait 4.5s = 31.7s
    #   31.7 – Create crosses + FadeIn spurious_label (1s) + wait 7.0s = 39.7s
    #   39.7 – Transform sub3 + wait 4.5s = 44.2s
    #   44.2 – FadeIn glows + pulsate (2s) + wait 7.5s = 53.7s
    #   53.7 – FadeOut sub + FadeIn insight (1s) + wait 9.5s = 64.2s
    #   64.2 – FadeOut outro (1s) + wait 2.5s = 67.7s
    # ──────────────────────────────────────────────────────────────────────────
    21: {
        "class":    "InvariantFeaturesScene",
        "file":     "scene_21_invariant_features.py",
        "duration": 68,
        "voice_segments": [
            (0.0, "Phần 21: Invariant Features. Feature nào còn đúng khi environment thay đổi?"),
            # Đọc ngay sau title card
            (5.5,
             "Invariant learning bắt đầu từ một ý tưởng đơn giản nhưng sâu sắc: "
             "feature ổn định, tức là causal feature, "
             "nên hữu ích qua nhiều environments khác nhau."),
            # Khi env1 xuất hiện
            (10.5,
             "Đây là environment 1: con bò trên nền đồng cỏ xanh."),
            # Khi env2 xuất hiện
            (16.5,
             "Environment 2: cùng loài vật, nhưng trên nền sa mạc khô cằn."),
            # Khi env3 xuất hiện
            (22.5,
             "Environment 3: con bò trên bờ biển. "
             "Background hoàn toàn khác — nhưng hình dáng vật thể vẫn giữ nguyên."),
            # Subtitle 2 + crosses xuất hiện
            (28.5,
             "Background đổi theo từng environment — "
             "đây là spurious feature, không đáng tin cậy."),
            # Crosses + spurious label
            (33.0,
             "Các dấu X đỏ đánh dấu background là feature giả — "
             "nếu model học theo background, nó sẽ fail khi environment đổi."),
            # Sub3 + glows xuất hiện
            (40.5,
             "Nhưng hình dáng vật thể — đường viền xanh đang sáng lên — "
             "đây là invariant feature, tín hiệu bền vững qua mọi môi trường."),
            # Insight box
            (55.0,
             "Stable feature tồn tại qua sự thay đổi environment. "
             "Đây là nền tảng của mọi phương pháp invariant learning."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 22 – IRM Objective
    # Duration: ~80s
    # Timeline:
    #   0.0  – Title card (Create axes 0.8s + Create lines 0.8s + wait 0.4s
    #           + Morph 1.8s + wait 1.5s + FadeOut 1.0s + wait 1.0s) = ~7.3s
    #   7.3  – FadeIn sub1 + wait 7.0s = 14.3s
    #   14.3 – FadeIn axes + title (1s) = 15.3s
    #   15.3 – FadeIn e1_points + boundary (1s) = 16.3s
    #   16.3 – FadeIn e2_points + boundary (1s) = 17.3s
    #   17.3 – Flash boundaries red (1s) + wait 1.0s + revert (1s) + wait 4.0s = 24.3s
    #   24.3 – GrowArrow mapping (1s) = 25.3s
    #   25.3 – FadeIn axes_right + title (1s) = 26.3s
    #   26.3 – TransformFromCopy (3.0s) = 29.3s
    #   29.3 – Create shared_boundary + label (1s) = 30.3s
    #   30.3 – wait 6.0s = 36.3s
    #   36.3 – Transform sub2 + wait 5.0s = 41.3s
    #   41.3 – FadeOut all (1s) = 42.3s
    #   42.3 – Write term_erm formula (1s) + FadeIn label (1s) + wait 7.5s = 51.8s
    #   51.8 – Write term_inv formula (1s) + FadeIn label (1s) + wait 8.5s = 62.3s
    #   62.3 – FadeOut sub + FadeIn insight (1s) + wait 9.5s = 72.8s
    #   72.8 – FadeOut outro (1s) + wait 4.0s = 77.8s
    # ──────────────────────────────────────────────────────────────────────────
    22: {
        "class":    "IRMObjectiveScene",
        "file":     "scene_22_irm_objective.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 22: Invariant Risk Minimization Objective. Khám phá cách tìm ra một classifier chung cho mọi môi trường."),
            # Ngay sau title card
            (8.0,
             "Làm sao ép representation học feature invariant? "
             "Đây là mục tiêu của IRM — Invariant Risk Minimization."),
            # Sub1 + raw space xuất hiện
            (15.5,
             "IRM học một representation Phi của X, "
             "sao cho cùng một classifier w là tối ưu trên mọi training environment. "
             "Nếu w phải dùng được ở mọi nơi, "
             "representation không nên giữ feature chỉ hữu ích cục bộ."),
            # Env1 boundary xuất hiện
            (25.5,
             "Trong raw space X, environment 1 màu xanh có đường ranh giới dốc dương, "
             "environment 2 màu vàng có đường ranh giới dốc âm — chúng không khớp nhau."),
            # Arrow + Rep space xuất hiện
            (36.5,
             "Qua ánh xạ Phi của X vào representation space, "
             "cả hai environment được phân tách bởi cùng một đường biên tím — "
             "đó chính là classifier w duy nhất và tối ưu."),
            # Formula ERM term
            (43.5,
             "Hàm mục tiêu IRM gồm hai phần. "
             "Phần đầu: tổng rủi ro huấn luyện trung bình "
             "trên tất cả training environments."),
            # Formula invariant penalty
            (53.5,
             "Phần hai: hình phạt classifier đồng nhất — "
             "buộc gradient của w tại điểm bằng 1 phải bằng 0 ở mọi environment. "
             "Đây là điều kiện để w là tối ưu đồng thời trên mọi nơi."),
            # Insight
            (64.0,
             "IRM yêu cầu một classifier tối ưu duy nhất trên mọi environment. "
             "Đây là ràng buộc mạnh, giúp loại bỏ các feature chỉ hữu ích cục bộ."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 23 – IRM Limits
    # Duration: ~70s
    # Timeline:
    #   0.0  – Title card (Create split 0.8s + FadeIn glow + Write 1.5s
    #           + flash 0.4+0.4s + wait 1.5s + FadeOut 0.5s + wait 1.0s) = ~6.1s
    #   6.1  – FadeIn sub1 + wait 6.5s = 12.6s
    #   12.6 – FadeIn train_envs (1.5s) + wait 6.5s = 20.6s
    #   20.6 – Create inv_frame + Write inv_text (1s) + wait 7.0s = 28.6s
    #   28.6 – Transform sub2 + wait 6.5s = 35.1s
    #   35.1 – scale train + FadeIn test (1s) + wait 6.0s = 42.1s
    #   42.1 – Create cross + Write fail_text (1s) + wait 8.5s = 51.6s
    #   51.6 – FadeOut sub + FadeIn insight (1s) + wait 10.5s = 63.1s
    #   63.1 – FadeOut outro (1s) + wait 3.5s = 67.6s
    # ──────────────────────────────────────────────────────────────────────────
    23: {
        "class":    "IRMLimitsScene",
        "file":     "scene_23_irm_limits.py",
        "duration": 70,
        "voice_segments": [
            # Title card intro
            (0.0, "Phần 23: IRM Limits. Khám phá những giới hạn của Invariant Risk Minimization khi environments không đủ tốt."),
            # Sau title card
            (7.0,
             "Nhưng IRM có giới hạn quan trọng. "
             "Điều gì xảy ra nếu environments không đủ đa dạng?"),
            # Sub1 + train envs
            (13.5,
             "Nếu mọi training environment đều giữ cùng một spurious correlation, "
             "feature spurious đó cũng trông invariant — "
             "bởi vì nó ổn định qua tất cả environments ta có."),
            # Train envs xuất hiện
            (22.0,
             "Ba training environments ở đây đều giống nhau: "
             "nền cỏ chiếm 90 phần trăm khi xuất hiện con bò. "
             "IRM nhìn vào và kết luận: nền cỏ là feature invariant."),
            # inv_frame highlight
            (30.0,
             "Đường viền xanh bao quanh feature nền cỏ — "
             "trong tập train, nó trông invariant."),
            # Sub2 + test env xuất hiện
            (36.5,
             "IRM cần environments đủ đa dạng để lộ ra sự không ổn định của feature giả."),
            # Test env + failure
            (42.5,
             "Test environment có nền bãi biển 100 phần trăm. "
             "Shortcut nền cỏ bị phá vỡ hoàn toàn — mô hình thất bại."),
            # Insight
            (53.5,
             "Environments xấu tạo ra invariance kém. "
             "Chất lượng của environments training quyết định chất lượng của invariant learning."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 24 – CLIP Contrastive Learning
    # Duration: ~75s
    # Timeline:
    #   0.0  – collision intro + ripple + Write title + wait 1.5s + FadeOut (0.5s) + wait 1.0s = ~6s
    #   6.0  – FadeIn sub1 + wait 6.5s = 12.5s
    #   12.5 – FadeIn encoders (1s) + wait 7.5s = 21.0s
    #   21.0 – FadeIn space + arrows (1s) + wait 7.0s = 29.0s
    #   29.0 – Transform sub2 + wait 6.5s = 35.5s
    #   35.5 – FadeIn vi, vt, incorrect (1s) + wait 6.5s = 43.0s
    #   43.0 – Create attract (1s) + Create repel (1s) + wait 8.5s = 53.5s
    #   53.5 – Write cosine_sim (1s) + wait 9.0s = 63.5s
    #   63.5 – FadeOut sub + FadeIn insight (1s) + wait 11.5s = 76.0s
    # ──────────────────────────────────────────────────────────────────────────
    24: {
        "class":    "CLIPContrastiveScene",
        "file":     "scene_24_clip_contrastive.py",
        "duration": 75,
        "voice_segments": [
            # Title intro
            (0.0, "Phần 24: CLIP Contrastive Learning. Khám phá cách mô hình lớn và dữ liệu lớn giúp đạt robustness qua học tương phản."),
            # Sau title
            (7.0,
             "Model lớn và dữ liệu lớn giúp gì cho robustness? "
             "CLIP là một ví dụ nổi bật."),
            # Sub1 + encoders
            (13.5,
             "CLIP học từ các cặp ảnh và văn bản "
             "bằng phương pháp học tương phản, contrastive learning. "
             "Image encoder và text encoder độc lập xử lý đầu vào của mình."),
            # Embedding space + arrows
            (22.5,
             "Cả hai encoder cùng chiếu vào một shared embedding space. "
             "Đây là không gian chung nơi ảnh và text có thể được so sánh trực tiếp."),
            # Sub2 + vectors trong space
            (30.5,
             "Cặp ảnh-văn bản tương ứng được kéo lại gần nhau trong embedding space. "
             "Cặp không khớp bị đẩy ra xa."),
            # Attract + repel arrows
            (44.5,
             "Mũi tên xanh lá kéo cặp đúng lại gần — attractive force. "
             "Mũi tên đỏ đẩy cặp sai ra xa — repulsive force. "
             "Đây là bản chất của contrastive loss."),
            # Cosine formula
            (55.0,
             "Mục tiêu toán học: maximize cosine similarity "
             "giữa vector ảnh và vector text của cùng cặp. "
             "Nhờ học trên hàng trăm triệu cặp, "
             "CLIP có khả năng zero-shot classification."),
            # Insight
            (65.0,
             "Pretraining trên dữ liệu đa dạng giúp học được representations tổng quát hơn — "
             "đây là một hướng cải thiện OOD robustness mà không cần explicit shift modeling."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 25 – More Data != Right Data
    # Duration: ~70s
    # Timeline:
    #   0.0  – title intro + Write title (1.0s) + FadeIn clusters (1.2+1.2s)
    #           + wait 1.5s + FadeOut (0.5s) + wait 1.0s = ~6.4s
    #   6.4  – FadeIn sub1 + wait 6.0s = 12.4s
    #   12.4 – FadeIn axes (1s) = 13.4s
    #   13.4 – FadeIn train_cloud + label (1s) = 14.4s
    #   14.4 – Create boundary (1s) = 15.4s
    #   15.4 – wait 6.5s = 21.9s
    #   21.9 – FadeIn target_cloud + label (1s) + wait 7.0s = 29.9s
    #   29.9 – FadeIn more_train_dots (1.5s) = 31.4s
    #   31.4 – Indicate boundary (1s) = 32.4s
    #   32.4 – Create crosses (1s) + wait 6.5s = 39.9s
    #   39.9 – Transform sub2 + wait 6.0s = 45.9s
    #   45.9 – FadeIn right_dots + label + arrow (1s) = 46.9s
    #   46.9 – Transform boundary (1.5s) + wait 8.5s = 56.9s
    #   56.9 – FadeOut sub + FadeIn warning (1s) + wait 10.5s = 68.4s
    # ──────────────────────────────────────────────────────────────────────────
    25: {
        "class":    "MoreDataNotRightDataScene",
        "file":     "scene_25_more_data_not_right_data.py",
        "duration": 70,
        "voice_segments": [
            # Title intro
            (0.0, "Phần 25: More Data không phải Right Data. Liệu thêm dữ liệu có luôn giúp model robust hơn?"),
            # Sau title
            (7.5,
             "Thêm data có luôn giúp model robust hơn không? "
             "Tutorial nhấn mạnh: số lượng data không đảm bảo robustness."),
            # Sub1 + axes + training cloud
            (14.5,
             "Đây là training data — tập trung ở vùng này. "
             "Decision boundary màu xanh được fit trên data đó."),
            # Target cloud xuất hiện
            (22.5,
             "Nhưng target shift màu đỏ nằm hoàn toàn ngoài vùng coverage của training data. "
             "Model chưa bao giờ thấy vùng này."),
            # More train dots
            (30.5,
             "Ta thêm nhiều data — nhưng tất cả đều trong cùng vùng training cũ. "
             "Decision boundary không thay đổi. "
             "Target shift vẫn hoàn toàn ngoài tầm với."),
            # Sub2 + right data
            (40.5,
             "Câu hỏi đúng không phải là cần bao nhiêu data, "
             "mà là cần thu thêm loại data nào, ở vùng nào, cho nhóm nào."),
            # Right data + adjusted boundary
            (47.5,
             "Chỉ một ít right data đúng vùng shift — màu xanh lá — "
             "đủ để điều chỉnh boundary và cover được target distribution."),
            # Warning insight
            (58.0,
             "More data không đồng nghĩa với right data. "
             "Trong y tế, xe tự lái, và chính sách công, "
             "dữ liệu đúng vùng shift rất đắt và khan hiếm."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 26 – Deductive vs Inductive
    # Duration: ~70s
    # Timeline:
    #   0.0  – slide in labels + Write title (1.5s) + Create divider (1.0s)
    #           + wait 1.5s + FadeOut (0.5s) + wait 1.0s = ~5.5s
    #   5.5  – FadeIn sub1 + wait 5.0s = 10.5s
    #   10.5 – Create divider (1s) = 11.5s
    #   11.5 – Write headers (1s) + wait 5.0s = 17.5s
    #   17.5 – FadeIn d1 (1s) + arrow + d2 (1s) + arrow + d3 (1s) + wait 6.0s = 26.5s
    #   26.5 – Transform sub2 + wait 5.0s = 31.5s
    #   31.5 – FadeIn i1 (1s) + arrow + i2 (1s) + wait 5.5s = 39.0s
    #   39.0 – Transform sub3 + wait 5.0s = 44.0s
    #   44.0 – arrow + i3 (1s) + arrow + i4 (1s) = 46.0s
    #   46.0 – FadeIn glow i4 (1s) + wait 6.5s = 53.5s
    #   53.5 – FadeOut sub + FadeIn insight (1s) + wait 9.0s = 63.5s
    #   63.5 – FadeOut outro (1s) + wait 2.5s = 67.0s
    # ──────────────────────────────────────────────────────────────────────────
    26: {
        "class":    "DeductiveInductiveScene",
        "file":     "scene_26_deductive_inductive.py",
        "duration": 70,
        "voice_segments": [
            # Title intro
            (0.0, "Phần 26: Deductive và Inductive. Ta nên bắt đầu từ lý thuyết hay từ hiện tượng thực tế?"),
            # Sau title
            (6.5,
             "Ta nên bắt đầu từ method hay từ hiện tượng thật? "
             "Đây là sự khác biệt giữa hướng diễn dịch và quy nạp."),
            # Sub1 + headers
            (12.0,
             "Hướng diễn dịch — deductive — xuất phát từ lý thuyết. "
             "Đặt ra giả định về phân phối, "
             "thiết kế thuật toán dựa trên giả định đó, "
             "rồi mới áp dụng vào dữ liệu thực tế."),
            # Deductive flow nodes
            (18.5,
             "Bước 1: giả định lý thuyết. "
             "Bước 2: thiết kế thuật toán. "
             "Bước 3: áp dụng vào dữ liệu. "
             "Đây là con đường từ trên xuống."),
            # Sub2 + inductive flow
            (27.5,
             "Hướng quy nạp — inductive — đi ngược lại. "
             "Bắt đầu từ lỗi thực tế, quan sát pattern shift, "
             "rồi mới thiết kế giả định và chọn method phù hợp."),
            # i3 + i4 xuất hiện
            (39.5,
             "Từ lỗi thực tế, phân tích kiểu shift. "
             "Từ phân tích shift, thiết kế giả định tùy chỉnh. "
             "Từ giả định, lựa chọn phương pháp phù hợp nhất."),
            # Glow i4
            (47.0,
             "Phương pháp quy nạp thực tiễn hơn vì "
             "dữ liệu thực tế thường không khớp với giả định lý thuyết có sẵn."),
            # Insight
            (55.0,
             "Bắt đầu từ các dịch chuyển quan sát được. "
             "Đây là điểm khởi đầu đúng đắn nhất."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 27 – Income CA -> PR
    # Duration: ~80s
    # Timeline:
    #   0.0  – FadeIn dots + GrowArrow + Write title (0.8+1.5+0.8s) + wait 1.5s
    #           + FadeOut (0.5s) + wait 1.0s = ~6.1s
    #   6.1  – FadeIn sub1 + wait 6.5s = 12.6s
    #   12.6 – FadeIn cards + arrow (1s) + wait 9.0s = 22.6s
    #   22.6 – Transform sub2 + wait 6.5s = 29.1s
    #   29.1 – FadeOut desc + FadeIn hist (1s) + Write x_shift_label (1s) + wait 9.5s = 40.6s
    #   40.6 – Transform sub3 + wait 6.5s = 47.1s
    #   47.1 – FadeOut hist + FadeIn axes + reg lines (1s) + Write yx_label (1s) + wait 10.0s = 59.1s
    #   59.1 – FadeOut sub + FadeIn insight (1s) + wait 11.5s = 71.6s
    #   71.6 – FadeOut outro (1s) + wait 3.5s = 76.1s
    # ──────────────────────────────────────────────────────────────────────────
    27: {
        "class":    "IncomeCaPrScene",
        "file":     "scene_27_income_ca_pr.py",
        "duration": 80,
        "voice_segments": [
            # Title intro
            (0.0, "Phần 27: Income Prediction từ California sang Puerto Rico. Phân tích nguyên nhân sụt giảm hiệu năng."),
            # Sau title
            (7.5,
             "Trong income prediction, source là California và target là Puerto Rico. "
             "Khi deploy model từ CA sang PR, performance thường giảm mạnh. "
             "Drop đến từ đâu?"),
            # Cards xuất hiện
            (14.0,
             "California: thu nhập trung bình 80 nghìn đô, ngành công nghệ cao, "
             "làm khoảng 40 giờ mỗi tuần. "
             "Puerto Rico: thu nhập trung bình 22 nghìn đô, "
             "ngành công nghệ thấp hơn, làm 32 giờ mỗi tuần."),
            # Sub2 + histograms (X-shift)
            (23.5,
             "Drop có thể đến từ X-shift: "
             "phân phối work hours, occupation và education "
             "khác nhau đáng kể giữa California và Puerto Rico."),
            # Histograms + x-shift label
            (30.5,
             "Histograms xanh và vàng cho thấy rõ: "
             "phân phối đặc trưng đã thay đổi — "
             "đây là covariate shift, hay X-shift."),
            # Sub3 + Y|X regression
            (41.5,
             "Nhưng cũng có thể đến từ Y given X shift. "
             "Cùng một occupation nhưng income có ý nghĩa khác "
             "tùy theo bối cảnh xã hội và kinh tế địa phương."),
            # Regression lines
            (48.5,
             "Hai đường hồi quy khác nhau về độ dốc: "
             "P của Y given X tại California "
             "khác P của Y given X tại Puerto Rico. "
             "Đây là concept shift."),
            # Insight
            (61.0,
             "Target drop có thể trộn lẫn cả X-shift và Y given X shift. "
             "Phân tách hai loại shift này là bước đầu tiên "
             "để hiểu và sửa model đúng cách."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 28 – Ambiguity Set Theo Biến
    # Duration: ~70s
    # Timeline:
    #   0.0  – Create ellipse + FadeIn vars + snap vars + Write title (0.8+0.8+1.8+1.5s)
    #           + FadeOut (0.5s) + wait 1.0s = ~6.4s
    #   6.4  – FadeIn sub1 + wait 6.0s = 12.4s
    #   12.4 – FadeIn dashboard (1s) = 13.4s
    #   13.4 – FadeIn set_group (1s) + wait 7.0s = 21.4s
    #   21.4 – Transform s_age + ambiguity_set (1s) + wait 6.5s = 28.9s
    #   28.9 – Transform sub2 + wait 6.0s = 34.9s
    #   34.9 – Scale top_group (1s) = 35.9s
    #   35.9 – FadeIn chart + label (1s) + wait 9.0s = 45.9s
    #   45.9 – FadeOut sub + FadeOut chart + FadeIn insight (1s) + wait 10.5s = 57.4s
    #   57.4 – FadeOut outro (1s) + wait 2.5s = 60.9s
    # ──────────────────────────────────────────────────────────────────────────
    28: {
        "class":    "AmbiguityVariablesScene",
        "file":     "scene_28_ambiguity_variables.py",
        "duration": 70,
        "voice_segments": [
            # Title intro
            (0.0, "Phần 28: Ambiguity Set theo biến. Ràng buộc độ robust của DRO vào các biến số thực tế."),
            # Sau title
            (7.5,
             "DRO nên robust trên biến nào? "
             "Thay vì chọn ambiguity set trừu tượng, "
             "ta có thể chọn theo biến có subgroup differences lớn."),
            # Sub1 + dashboard
            (14.0,
             "Dashboard bên trái liệt kê các biến: Age, Education, Occupation. "
             "Ambiguity set bên phải hiển thị hình dạng tương ứng — "
             "ban đầu là hình tròn, tức là không có ràng buộc hướng cụ thể."),
            # Toggle Age active
            (22.0,
             "Khi bật biến Age, ambiguity set thay đổi thành ellipse nằm ngang. "
             "Điều này có nghĩa: ta kỳ vọng shift chủ yếu xảy ra theo hướng Age, "
             "và ràng buộc robustness vào hướng đó."),
            # Sub2 + performance
            (30.0,
             "Ràng buộc robustness vào đúng các biến dịch chuyển "
             "giúp tối ưu hóa worst-group performance thực sự."),
            # Bar chart
            (36.5,
             "Bar chart so sánh: ambiguity set trừu tượng đạt 55 phần trăm worst-group accuracy, "
             "trong khi ràng buộc theo biến cụ thể đạt 82 phần trăm. "
             "Sự khác biệt rất đáng kể."),
            # Insight
            (47.0,
             "Robustness phải được gắn với các biến số dịch chuyển cụ thể. "
             "Đây là bước chuyển từ DRO trừu tượng sang DRO thực tiễn."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 29 – Mutual Information
    # Duration: ~85s
    # Timeline:
    #   0.0  – Venn circles slide + Write title + FadeIn intersection (1.0+1.5+0.8s)
    #           + wait 1.5s + FadeOut (0.5s) + wait 1.0s = ~6.3s
    #   6.3  – FadeIn sub1 + wait 7.0s = 13.3s
    #   13.3 – Create h_y_rect + Write labels (1s) + wait 10.0s = 24.3s
    #   24.3 – FadeIn x_box (1s) = 25.3s
    #   25.3 – Transform sub2 + wait 7.0s = 32.3s
    #   32.3 – Create flow_arrow (0.5s) = 32.8s
    #   32.8 – ReplacementTransform h_y -> h_yx + i_xy (1.5s) + wait 11.0s = 45.3s
    #   45.3 – Write equation (1s) + wait 11.0s = 57.3s
    #   57.3 – FadeOut sub + FadeIn insight (1s) + wait 11.5s = 69.8s
    #   69.8 – FadeOut outro (1s) + wait 3.5s = 74.3s
    # ──────────────────────────────────────────────────────────────────────────
    29: {
        "class":    "MutualInformationScene",
        "file":     "scene_29_mutual_information.py",
        "duration": 85,
        "voice_segments": [
            # Title intro
            (0.0, "Phần 29: Mutual Information. Thông tin tương hỗ giữa X và Y là gì?"),
            # Sau title
            (7.5,
             "Mutual information đo lượng thông tin X cung cấp về Y. "
             "Đây là nền tảng toán học của predictive heterogeneity."),
            # H(Y) rectangle xuất hiện
            (14.5,
             "H của Y là entropy — sự bất định ban đầu của Y "
             "trước khi ta biết bất cứ điều gì. "
             "Hình chữ nhật vàng thể hiện toàn bộ sự bất định đó."),
            # Sub2 + X_box
            (25.5,
             "Bây giờ quan sát X. "
             "H của Y given X là bất định còn lại sau khi đã biết X."),
            # Transform H(Y) -> H(Y|X) + I(X;Y)
            (33.5,
             "Phần xanh dương là bất định còn lại H của Y given X. "
             "Phần xanh lá cây là mutual information — "
             "lượng thông tin X mang lại về Y. "
             "Mutual information chính là phần bất định được giải tỏa."),
            # Equation xuất hiện
            (47.0,
             "Công thức: I của X và Y bằng H của Y trừ H của Y given X. "
             "Mutual information luôn không âm. "
             "Nó bằng không khi X và Y hoàn toàn độc lập, "
             "và tăng lên khi X mang nhiều thông tin về Y hơn."),
            # Insight
            (59.0,
             "Thông tin chính là sự giảm thiểu bất định. "
             "Hiểu mutual information là chìa khóa để hiểu "
             "tại sao một split subgroup có thể hữu ích cho prediction."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 30 – Predictive Heterogeneity
    # Duration: ~80s
    # Timeline:
    #   0.0  – node tree intro + Write title + GrowArrow (0.8+1.5+1.0s)
    #           + FadeIn children (1.0s) + wait 1.5s + FadeOut (0.5s) + wait 1.0s = ~7.3s
    #   7.3  – FadeIn sub1 + wait 6.5s = 13.8s
    #   13.8 – FadeIn axes (1s) = 14.8s
    #   14.8 – FadeIn all_dots (1s) = 15.8s
    #   15.8 – Create avg_line + Write label + GrowArrow (1s) + wait 7.5s = 24.3s
    #   24.3 – Create bad_split (1s) + Write bad labels (1s) + wait 7.5s = 33.8s
    #   33.8 – FadeOut bad split (0.5s) = 34.3s
    #   34.3 – Transform sub2 + wait 6.5s = 40.8s
    #   40.8 – Animate dot colors (1s) = 41.8s
    #   41.8 – Create g1_line + g2_line + Write labels (1s) + wait 7.0s = 49.8s
    #   49.8 – FadeOut good labels + Write obj (1s) + wait 9.0s = 59.8s
    #   59.8 – FadeOut sub + FadeIn insight (1s) + wait 10.5s = 71.3s
    #   71.3 – FadeOut outro (1s) + wait 3.5s = 75.8s
    # ──────────────────────────────────────────────────────────────────────────
    30: {
        "class":    "PredictiveHeterogeneityScene",
        "file":     "scene_30_predictive_heterogeneity.py",
        "duration": 80,
        "voice_segments": [
            # Title intro (gộp câu hỏi mở đầu)
            (0.0, "Phần 30: Predictive Heterogeneity. Khi nào một split subgroup thực sự giúp ích cho dự đoán?"),
            # Sub1 + data points
            (15.0,
             "Predictive heterogeneity tìm split E sao cho "
             "biết E làm tăng thông tin dự đoán của X về Y. "
             "Nếu I conditional lớn hơn I không conditional, "
             "groups đó phản ánh cơ chế dự đoán khác nhau."),
            # Average line + label
            (25.5,
             "Nhìn vào toàn bộ dữ liệu màu xám: "
             "đường trung bình fit rất kém — "
             "nó không mô tả đúng bất kỳ nhóm nào."),
            # Bad split
            (34.5,
             "Split ngẫu nhiên theo đường thẳng đứng không giúp ích: "
             "I conditional gần bằng I không conditional. "
             "Không phát hiện được cấu trúc ẩn."),
            # Good split — dot colors reveal
            (42.0,
             "Nhưng split đúng theo cơ chế ẩn lộ ra hai nhóm: "
             "nhóm xanh dương với hệ số dương, "
             "nhóm vàng với hệ số âm. "
             "Hai đường hồi quy hoàn toàn khác biệt."),
            # Objective formula
            (50.5,
             "Mục tiêu: tìm E maximize phần tăng thông tin. "
             "Công thức: supremum theo E của "
             "I conditional trừ I không conditional. "
             "Đây là bài toán tìm nhóm giải thích nhiều nhất sự khác biệt dự đoán."),
            # Insight
            (61.5,
             "Các nhóm hữu ích sẽ làm thay đổi mối quan hệ dự đoán. "
             "Đây là nền tảng để khám phá environments ẩn "
             "trong các ứng dụng thực tế như crop yield và COVID mortality."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 31 – Crop Yield
    # ──────────────────────────────────────────────────────────────────────────
    31: {
        "class":    "CropYieldScene",
        "file":     "scene_31_crop_yield.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 31: Crop Yield. Một biến ẩn có thể lộ ra qua chính mô hình dự đoán không?"),
            (1.0, "Trong bài toán dự đoán năng suất cây trồng, các đặc trưng khí hậu được dùng để dự đoán sản lượng."),
            (2.0, "Đây là bản đồ loại cây trồng thực tế: vùng xanh là ngô, vùng vàng là đậu nành."),
            (3.0, "Nhưng cơ chế tạo ra năng suất thay đổi mạnh theo loại cây trồng. Ban đầu, ta không hề có nhãn loại cây."),
            (4.0, "Predictive heterogeneity có thể học ra subpopulation ẩn này chỉ thông qua dự đoán."),
            (5.0, "Bản đồ phân tách học được khớp gần như hoàn hảo với loại cây trồng thực tế, dù biến này hoàn toàn bị ẩn."),
            (6.0, "Cơ chế ẩn có thể được phát hiện thông qua dự đoán."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 32 – COVID Mortality
    # ──────────────────────────────────────────────────────────────────────────
    32: {
        "class":    "COVIDMortalityScene",
        "file":     "scene_32_covid_mortality.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 32: COVID Mortality. Một mô hình trung bình có thể che giấu những cơ chế rủi ro nào?"),
            (1.0, "Với bài toán tử vong do COVID, mô hình ERM chỉ thấy các đặc trưng rủi ro trung bình của toàn bộ dữ liệu."),
            (2.0, "Đây là các đặc trưng quan trọng theo góc nhìn trung bình: tuổi, bệnh nền và triệu chứng."),
            (3.0, "Nhưng khi phân tách thành các subpopulation, hai cơ chế rủi ro hoàn toàn khác biệt lộ ra."),
            (4.0, "Nhóm thứ nhất là người cao tuổi, rủi ro bị chi phối mạnh bởi bệnh nền. Nhóm thứ hai trải rộng nhiều độ tuổi, nhưng nhạy cảm với triệu chứng hô hấp nghiêm trọng."),
            (5.0, "Mỗi nhóm có một đặc trưng chủ đạo riêng. Mô hình trung bình đã trộn lẫn và làm mờ cả hai cơ chế này."),
            (6.0, "Một tập dữ liệu có thể chứa nhiều cơ chế rủi ro khác nhau."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 33 – No Environment Labels
    # ──────────────────────────────────────────────────────────────────────────
    33: {
        "class":    "NoEnvLabelsScene",
        "file":     "scene_33_no_env_labels.py",
        "duration": 65,
        "voice_segments": [
            (0.0, "Phần 33: No Environment Labels. Nếu nhãn nguồn dữ liệu bị mất, IRM sẽ làm gì?"),
            (1.0, "Các dataset hiện đại thường gộp dữ liệu từ rất nhiều nguồn khác nhau."),
            (2.0, "Đây là ba nguồn dữ liệu riêng biệt, mỗi nguồn có một environment label riêng."),
            (3.0, "Nhưng khi tích hợp lại thành một tập gộp, các nhãn môi trường đều bị xóa mất."),
            (4.0, "Giờ chỉ còn dữ liệu gộp màu xám. Invariant learning không còn biết phải so sánh qua những environment nào."),
            (5.0, "Đôi khi, các environment buộc phải được tự học từ chính dữ liệu."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 34 – HRM Loop
    # ──────────────────────────────────────────────────────────────────────────
    34: {
        "class":    "HRMLoopScene",
        "file":     "scene_34_hrm_loop.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 34: HRM Loop. Liệu ta có thể vừa học environment, vừa học predictor cùng lúc?"),
            (1.0, "Heterogeneous Risk Minimization giải quyết điều này bằng một chu trình đồng tiến hóa gồm hai module."),
            (2.0, "Module thứ nhất là heterogeneity identification, module thứ hai là invariant prediction."),
            (3.0, "Identification học cách phân nhóm dữ liệu thành các environment nhân tạo, dựa trên các variant feature."),
            (4.0, "Invariant prediction học một predictor ổn định từ chính các environment vừa được tìm ra."),
            (5.0, "Ban đầu, worst-group accuracy chỉ đạt 55 phần trăm."),
            (6.0, "Qua mỗi vòng lặp, hai module bổ trợ lẫn nhau: accuracy tăng dần lên 72, rồi 89 phần trăm."),
            (7.0, "Phát hiện environment và invariant learning có thể đồng tiến hóa cùng nhau."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 35 – ColoredMNIST
    # ──────────────────────────────────────────────────────────────────────────
    35: {
        "class":    "ColoredMNISTScene",
        "file":     "scene_35_colored_mnist.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 35: Colored MNIST. Màu sắc hay hình dạng mới là tín hiệu ổn định?"),
            (1.0, "ColoredMNIST là một benchmark kinh điển để minh họa rõ ràng về spurious correlation."),
            (2.0, "Trong tập train, 90 phần trăm chữ số 5 có màu xanh lá. Màu sắc giúp dự đoán rất dễ."),
            (3.0, "Mô hình nhanh chóng học một shortcut: cứ thấy màu xanh lá thì đoán là số 5."),
            (4.0, "Nhưng ở tập test, tương quan màu sắc bị đảo ngược: số 5 giờ có màu đỏ."),
            (5.0, "Shortcut màu sắc sụp đổ. Mô hình dựa vào màu dự đoán sai hoàn toàn."),
            (6.0, "Chỉ khi học được đặc trưng hình dạng bất biến, mô hình mới thực sự robust."),
            (7.0, "Đặc trưng màu sắc giả sẽ thất bại khi environment thay đổi."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 36 – Hard vs Noisy Samples
    # ──────────────────────────────────────────────────────────────────────────
    36: {
        "class":    "HardNoisySamplesScene",
        "file":     "scene_36_hard_noisy_samples.py",
        "duration": 70,
        "voice_segments": [
            (0.0, "Phần 36: Hard và Noisy Samples. Loss cao có luôn đáng để upweight không?"),
            (1.0, "Trong robust learning, ta thường tập trung vào các mẫu có loss cao, như cách DRO làm."),
            (2.0, "Đây là nhóm đa số, loss thấp, mô hình dự đoán tốt."),
            (3.0, "Nhưng các điểm có loss cao có thể đến từ hai nguồn gốc rất khác nhau."),
            (4.0, "Cả cụm thiểu số lẫn điểm ngoại lai cô lập đều có loss cao như nhau."),
            (5.0, "Trường hợp thứ nhất là hard samples: nhóm thiểu số quan trọng, thực sự đáng tối ưu."),
            (6.0, "Trường hợp thứ hai chỉ là noisy samples cô lập. Nếu cố fit, mô hình sẽ học phải nhiễu."),
            (7.0, "Loss cao là một tín hiệu không rõ ràng."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 37 – Geometric Wasserstein
    # ──────────────────────────────────────────────────────────────────────────
    37: {
        "class":    "GeometricWassersteinScene",
        "file":     "scene_37_geometric_wasserstein.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 37: Geometric Wasserstein. Hình học giúp phân biệt hard và noise như thế nào?"),
            (1.0, "Geometric Wasserstein đưa cấu trúc hình học của manifold dữ liệu vào trong DRO."),
            (2.0, "Đây là manifold dữ liệu: bề mặt mà các điểm dữ liệu thực sự nằm trên đó."),
            (3.0, "Các mẫu hợp lệ nằm dọc theo manifold, còn mẫu nhiễu thì bị cô lập, nằm xa khỏi cấu trúc."),
            (4.0, "Hard samples thường nằm trong vùng lân cận có cấu trúc; còn noisy samples thì cô lập."),
            (5.0, "Standard Wasserstein vận chuyển xác suất theo đường thẳng, nên dễ bị hút thẳng vào mẫu nhiễu."),
            (6.0, "Geometric Wasserstein buộc dòng vận chuyển phải chạy dọc theo manifold, nên bỏ qua được điểm ngoại lai."),
            (7.0, "Độ robust nên tôn trọng hình học của dữ liệu."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 38 – Error Slices
    # ──────────────────────────────────────────────────────────────────────────
    38: {
        "class":    "ErrorSlicesScene",
        "file":     "scene_38_error_slices.py",
        "duration": 70,
        "voice_segments": [
            (0.0, "Phần 38: Error Slices. Mô hình yếu nhất ở vùng dữ liệu nào?"),
            (1.0, "Độ chính xác trung bình 95 phần trăm nghe có vẻ tốt, nhưng nó có thể che giấu những lỗi cực kỳ nghiêm trọng."),
            (2.0, "Đây là độ chính xác tổng thể của mô hình: 95 phần trăm."),
            (3.0, "Ta cần phân tách hiệu suất thành các error slice: nhóm A đạt 99, nhóm B đạt 93, nhưng nhóm C chỉ đạt 43 phần trăm."),
            (4.0, "Nhóm C là một thiểu số chỉ chiếm 5 phần trăm, nhưng mô hình thất bại nặng nề ở đó. Đây chính là lát cắt tệ nhất."),
            (5.0, "Hãy tìm ra nơi mô hình thất bại, chứ không chỉ tần suất thất bại."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 39 – Stability + Feature Sensitivity
    # ──────────────────────────────────────────────────────────────────────────
    39: {
        "class":    "StabilityFeatureScene",
        "file":     "scene_39_stability_feature.py",
        "duration": 75,
        "voice_segments": [
            (0.0, "Phần 39: Stability và Feature Sensitivity. Mô hình nhạy cảm với loại shift nào, và với feature nào?"),
            (1.0, "Để đánh giá stability, ta đo khoảng cách từ phân phối hiện tại đến vùng lỗi."),
            (2.0, "Đây là mô hình tại phân phối train, và đây là tập lỗi, nơi độ chính xác sụt giảm."),
            (3.0, "Khoảng cách giữa chúng chính là stability margin: phải dịch phân phối đi bao xa mới chạm tới vùng lỗi."),
            (4.0, "Ta cũng kiểm tra độ nhạy của từng feature: dịch chuyển tuổi rất nhạy cảm, còn trình độ học vấn thì ổn định hơn."),
            (5.0, "Khi dịch chuyển một biến nhạy cảm như tuổi, biên an toàn co hẹp thảm hại, mô hình tiến sát vùng lỗi."),
            (6.0, "Một mô hình robust phải nói rõ: nó chống lại loại shift nào, trên những feature nào."),
            (7.0, "Độ robust phải chỉ rõ loại dịch chuyển và các đặc trưng nhạy cảm."),
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # SCENE 40 – Deployment Attribution + Conclusion
    # ──────────────────────────────────────────────────────────────────────────
    40: {
        "class":    "DeploymentConclusionScene",
        "file":     "scene_40_deployment_conclusion.py",
        "duration": 100,
        "voice_segments": [
            (0.0, "Phần 40: Deployment và Kết luận. Khi hiệu năng sụt giảm, ta sửa bằng cách nào?"),
            (1.0, "Sau khi triển khai, hiệu năng sụt giảm có thể do X-shift, do Y given X shift, hoặc cả hai."),
            (2.0, "Ta có phân phối nguồn P và phân phối đích Q."),
            (3.0, "Bằng cách tập trung vào phần phân phối chung S, vùng chồng lấn giữa P và Q, ta tách được thay đổi do lấy mẫu khỏi thay đổi do cơ chế. Chỉ khi hiểu đúng shift, ta mới chọn đúng can thiệp."),
            (4.0, "Và đây là thông điệp cuối cùng. OOD generalization không phải là một thuật toán đơn lẻ. Từ ERM, DRO, IRM, đến HRM, tất cả chỉ là các mảnh ghép."),
            (5.0, "Nó là cả một workflow nhận biết sự không đồng nhất. Không phải cứ mô hình lớn hơn là generalize tốt hơn; không phải cứ nhiều dữ liệu hơn là robust hơn."),
            (6.0, "Điểm khởi đầu đúng đắn luôn là thấu hiểu sự không đồng nhất của dữ liệu."),
            (7.0, "Hãy thấu hiểu sự không đồng nhất, trước khi đối phó với dịch chuyển."),
            (8.0, "Cảm ơn các bạn đã lắng nghe. Hẹn gặp lại trong những hành trình khám phá tiếp theo."),
        ],
    },
}


# ─────────────────────────── HÀM TIỆN ÍCH ──────────────────────────────────

def find_manim_video(scene_num: int, scene_class: str) -> Path | None:
    """Tìm file video Manim đã render cho scene, tìm đệ quy trong cả project."""
    search_roots = [PROJECT_ROOT / "media", SRC_DIR / "media", PROJECT_ROOT / "output"]
    for root in search_roots:
        if not root.exists():
            continue
        for path in root.rglob(f"{scene_class}.mp4"):
            return path   # trả về file đầu tiên tìm được
    return None


def get_audio_duration(path: Path) -> float:
    """Lấy thời lượng của file audio (giây) bằng ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        str(path)
    ]
    try:
        out = subprocess.check_output(cmd, text=True).strip()
        return float(out)
    except Exception:
        return 3.0  # fallback

def generate_tts_segment(text: str, out_path: Path) -> bool:
    """Tạo audio bằng ElevenLabs API và lưu ra file MP3."""
    if out_path.exists() and out_path.stat().st_size > 1000:
        print(f"  [SKIP] Đã có: {out_path.name} ({get_audio_duration(out_path):.1f}s)")
        return True
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    data = {
        "text": text,
        "model_id": TTS_MODEL,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    
    import time
    for attempt in range(3):
        try:
            if attempt == 0:
                print(f"  [TTS ] {out_path.stem[:45]} (ElevenLabs)...")
            else:
                print(f"  [RETRY] Lần {attempt+1} cho {out_path.name}...")
                
            response = requests.post(url, json=data, headers=headers, timeout=60)
            
            if response.status_code == 200:
                with open(out_path, "wb") as f:
                    f.write(response.content)
                dur = get_audio_duration(out_path)
                print(f"  [OK  ] {out_path.stat().st_size // 1024} KB ({dur:.1f}s)")
                time.sleep(1.0)
                return True
            else:
                print(f"  [ERR ] API Error {response.status_code}: {response.text}")
                time.sleep(2.0)
        except Exception as exc:
            print(f"  [ERR ] Lỗi gọi TTS: {exc}")
            time.sleep(2.0)
            
    print(f"  [ERR ] Thất bại sau 3 lần thử.")
    return False


def build_audio_track(scene_num: int, info: dict) -> Path | None:
    """
    Ghép tất cả segment TTS thành một audio track đồng bộ với video.
    Dùng ffmpeg adelay để đặt mỗi segment đúng vị trí thời gian (ms).
    """
    seg_dir = AUDIO_DIR / f"scene_{scene_num:02d}"
    seg_dir.mkdir(parents=True, exist_ok=True)

    segments    = info["voice_segments"]   # list of (start_sec, text)
    duration    = info["duration"]

    # ── Đọc thời gian thực từ timings.txt (do voice_sync.py ghi khi render) ─
    # Nếu có, dùng thay cho mốc ước đoán trong SCENE_NARRATIONS
    timing_map: dict[int, float] = {}
    timing_file = seg_dir / "timings.txt"
    if timing_file.exists():
        for line in timing_file.read_text(encoding="utf-8").strip().splitlines():
            if "," in line:
                idx_str, t_str = line.split(",", 1)
                timing_map[int(idx_str.strip())] = float(t_str.strip())
        if timing_map:
            print(f"  [TIMING] Dùng thời gian thực từ timings.txt ({len(timing_map)} mốc)")

    print(f"\n[Scene {scene_num}] Tạo {len(segments)} TTS segments...")

    # ── Bước 1: tạo từng MP3 segment ───────────────────────────────────────
    mp3_list = []
    prev_end_sec = 0.0
    for idx, (scheduled_start, text) in enumerate(segments):
        mp3_path = seg_dir / f"seg_{idx:02d}_t{int(scheduled_start):04d}.mp3"
        ok = generate_tts_segment(text, mp3_path)
        if not ok:
            return None

        duration_seg = get_audio_duration(mp3_path)
        # Ưu tiên dùng thời gian thực; fallback về scheduled_start
        base_start = timing_map.get(idx, scheduled_start)
        actual_start = max(base_start, prev_end_sec + 0.2)
        mp3_list.append((actual_start, mp3_path))
        prev_end_sec = actual_start + duration_seg

    # ── Độ dài track: phủ hết segment cuối (tránh cắt insight) ─────────────
    # prev_end_sec = thời điểm kết thúc segment cuối cùng.
    track_len = max(duration, prev_end_sec + 0.5)

    # ── Bước 2: ghép bằng ffmpeg với adelay ────────────────────────────────
    print(f"\n[Scene {scene_num}] Ghép audio track ({track_len:.1f}s)...")

    input_args   : list[str] = []
    filter_parts : list[str] = []
    stream_labels: list[str] = []

    for i, (start_sec, mp3_path) in enumerate(mp3_list):
        input_args += ["-i", str(mp3_path)]
        delay_ms = int(start_sec * 1000)
        filter_parts.append(f"[{i}]adelay={delay_ms}|{delay_ms}[a{i}]")
        stream_labels.append(f"[a{i}]")

    n = len(mp3_list)
    filter_complex = (
        ";".join(filter_parts)
        + f";{''.join(stream_labels)}amix=inputs={n}"
          f":duration=longest:normalize=0[out]"
    )

    track_path = seg_dir / f"scene_{scene_num:02d}_audio_track.mp3"
    cmd = (
        ["ffmpeg", "-y"]
        + input_args
        + [
            "-filter_complex", filter_complex,
            "-map",  "[out]",
            "-t",    f"{track_len:.3f}",
            "-ar",   "44100",
            "-b:a",  "192k",
            str(track_path),
        ]
    )

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            size_kb = track_path.stat().st_size // 1024
            print(f"  [OK  ] Track: {track_path.name} ({size_kb} KB)")
            return track_path
        else:
            print(f"  [ERR ] ffmpeg failed:\n{result.stderr[-800:]}")
            return None
    except FileNotFoundError:
        print("  [ERR ] ffmpeg không tìm thấy trong PATH!\n"
              "         Tải tại: https://ffmpeg.org/download.html")
        return None
    except subprocess.TimeoutExpired:
        print("  [ERR ] ffmpeg timeout (>120s)")
        return None


def merge_video_audio(video_path: Path, audio_path: Path, out_path: Path) -> bool:
    """Ghép video Manim + audio track thành file MP4 cuối cùng."""
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-i", str(audio_path),
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar",  "44100",
        "-shortest",
        "-movflags", "+faststart",
        str(out_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            size_mb = out_path.stat().st_size / (1024 * 1024)
            print(f"  [OK  ] {out_path.name} ({size_mb:.1f} MB)")
            return True
        else:
            print(f"  [ERR ] merge failed:\n{result.stderr[-500:]}")
            return False
    except FileNotFoundError:
        print("  [ERR ] ffmpeg không tìm thấy!")
        return False


def process_scene(scene_num: int, audio_only: bool = False) -> bool:
    """Xử lý toàn bộ pipeline (TTS → track → merge) cho một scene."""
    info = SCENE_NARRATIONS.get(scene_num)
    if not info:
        print(f"[SKIP] Không có narration cho scene {scene_num}")
        return False

    print(f"\n{'='*62}")
    print(f"  SCENE {scene_num:02d}: {info['class']}  ({info['duration']}s)")
    print(f"{'='*62}")

    # Tạo audio track
    audio_track = build_audio_track(scene_num, info)
    if not audio_track:
        return False

    if audio_only:
        print(f"  [INFO] Audio-only mode: bỏ qua merge. Track: {audio_track}")
        return True

    # Tìm video
    video_path = find_manim_video(scene_num, info["class"])
    if not video_path:
        print(f"\n  [WARN] Chưa tìm thấy video cho Scene {scene_num}.")
        print(f"         Render bằng:")
        print(f"           cd src")
        print(f"           python -m manim -ql scenes/{info['file']} {info['class']}")
        print(f"         Audio track đã lưu: {audio_track}")
        return True   # audio OK

    print(f"  [INFO] Video: {video_path.name}")
    out_path = FINAL_DIR / f"scene_{scene_num:02d}_with_voice.mp4"
    return merge_video_audio(video_path, audio_track, out_path)


# ─────────────────────────────── MAIN ───────────────────────────────────────

def parse_scene_range(s: str) -> list[int]:
    result = []
    for part in s.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            result.extend(range(int(a), int(b) + 1))
        elif part:
            result.append(int(part))
    return sorted(set(result))


def main() -> None:
    global TTS_VOICE, TTS_MODEL
    parser = argparse.ArgumentParser(
        description="Tạo voiceover OpenAI TTS và ghép vào video Manim (scenes 21-30).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--scenes", default="21-30",
        help="Dải scene cần xử lý. VD: 21-30 | 21,22,25 | 21  (mặc định: 21-30)",
    )
    parser.add_argument(
        "--audio-only", action="store_true",
        help="Chỉ tạo audio track, không ghép video (dùng khi chưa render Manim).",
    )
    parser.add_argument(
        "--key", default="",
        help="Không dùng (giữ để tương thích argument).",
    )
    parser.add_argument(
        "--voice", default=TTS_VOICE,
        help=f"Giọng TTS (voice_id).",
    )
    parser.add_argument(
        "--model", default=TTS_MODEL,
        help=f"Model TTS (mặc định: {TTS_MODEL}).",
    )
    args = parser.parse_args()

    # Override globals nếu user cung cấp
    TTS_VOICE = args.voice
    TTS_MODEL = args.model

    scenes = parse_scene_range(args.scenes)
    print(f"\n>>> Scenes  : {scenes}")
    print(f">>> Model   : {TTS_MODEL}")
    print(f">>> Voice   : {TTS_VOICE}")
    print(f">>> Audio   : {AUDIO_DIR}")
    print(f">>> Final   : {FINAL_DIR}")
    print(f">>> Audio-only: {args.audio_only}")

    results: dict[int, bool] = {}
    for scene_num in scenes:
        if scene_num not in SCENE_NARRATIONS:
            print(f"\n[SKIP] Scene {scene_num}: chưa có narration script")
            results[scene_num] = False
            continue
        results[scene_num] = process_scene(scene_num, audio_only=args.audio_only)

    # ── Tổng kết ────────────────────────────────────────────────────────────
    print(f"\n{'='*62}")
    print("KẾT QUẢ CUỐI:")
    success = sum(v for v in results.values())
    for num in sorted(results):
        ok   = results[num]
        mark = "✓" if ok else "✗"
        name = SCENE_NARRATIONS.get(num, {}).get("class", "?")
        print(f"  {mark} Scene {num:02d}: {name}")
    print(f"\n  Thành công: {success}/{len(results)} scene(s)")
    if not args.audio_only:
        print(f"  Output   : {FINAL_DIR}")
    print(f"{'='*62}\n")


if __name__ == "__main__":
    main()
