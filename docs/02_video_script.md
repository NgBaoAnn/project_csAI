# Kịch Bản Video Chi Tiết

> **Tổng thời lượng:** ~22-25 phút | **Ngôn ngữ:** Tiếng Việt | **Style:** 3Blue1Brown
>
> **Nguyên tắc kịch bản 3B1B:** *Bắt đầu bằng một mystery, kết thúc bằng một definition.*  
> Mỗi scene phải có **câu hỏi mở đầu** và **câu trả lời kết thúc** — không bao giờ ngược lại.

---

## Scene 1 — Intro: Cái Bẫy Của Sự Thành Công `TV1` | ~1.5 phút

**Mystery mở đầu:** *"99% accuracy — nhưng tại sao nó vẫn sai?"*

**Narration:**
> "Năm 2015, một model phân loại ảnh huấn luyện trên ImageNet đạt độ chính xác vượt con người. Nhưng cùng năm đó, Google Photos tự động gán nhãn ảnh người da đen với từ 'gorilla'. Không phải vì code sai. Không phải vì thiếu dữ liệu. Mà vì có một giả định ẩn mà chúng ta chưa bao giờ đặt câu hỏi — một giả định mà hôm nay chúng ta sẽ phá vỡ."

**Animation:**
1. Dark screen → Title: *"Data Heterogeneity & OOD Generalization"*
2. Ba flash examples nối tiếp (0.5s mỗi cái, tone nghiêm túc):
   - Xe tự lái fail khi gặp biển báo bị dán sticker
   - Medical AI chẩn đoán sai trên bệnh nhân từ vùng khác
   - Face recognition sai với người da màu
3. Tất cả fade → câu hỏi lớn xuất hiện: *"Vấn đề là gì?"*
4. Transition: *"Câu trả lời bắt đầu từ một giả định..."*

---

## Scene 2 — i.i.d.: Giả Định Mà Chúng Ta Quên Kiểm Tra `TV1` | ~2 phút

**Mystery:** *"Tại sao một model hoàn hảo trong lab lại thất bại ngoài thực tế?"*

**Narration:**
> "Mọi thuật toán ML đều bắt đầu với một giả định không nói ra: dữ liệu train và test đến từ **cùng một phân phối**. Các nhà thống kê gọi đây là giả định i.i.d. — *independent and identically distributed*. Khi nó đúng, gradient descent tìm được model tốt. Nhưng khi nó sai?"

**Animation:**
1. **Bước 1:** 2D plane, scatter 200 điểm xanh *"Training Data"* và 200 điểm xanh lá *"Test Data"* — hai đám chồng lên nhau hoàn toàn
2. **Bước 2:** Equation xuất hiện: `P_train(X, Y) = P_test(X, Y)` — tick xanh ✓
3. **Bước 3:** Test cloud dần **dịch chuyển** sang phải, xa dần training cloud
4. **Bước 4:** Accuracy counter animate: `95.2% → 74.3% → 61.8%` — màu đỏ dần
5. **Kết:** Box highlight: *"i.i.d. là điều kiện lý tưởng — không phải thực tế"*

**Transition:** *"Vậy thực tế là gì? Distribution shift — và nó đến từ nhiều dạng khác nhau..."*

---

## Scene 3 — Distribution Shift: Ba Kẻ Phá Hoại `TV1` | ~2.5 phút

**Mystery:** *"'Phân phối thay đổi' — nghe đơn giản, nhưng có mấy cách nó có thể xảy ra?"*

**Narration:**
> "Khi train distribution ≠ test distribution, ta gọi đó là distribution shift. Nhưng 'shift' không phải một kiểu — có **ba dạng khác nhau**, với hậu quả và giải pháp khác nhau."

**Animation — 3 panels xuất hiện tuần tự, mỗi panel có mini-animation:**

**Panel 1: Covariate Shift** (màu xanh)
- `P(X)` thay đổi, `P(Y|X)` giữ nguyên
- Visual: scatter plot của X thay đổi shape (kéo dài, xoay) nhưng decision boundary giữ nguyên ý nghĩa
- Ví dụ: *"Ảnh chụp ban ngày → ban đêm: cùng con mèo, khác lighting"*

**Panel 2: Label Shift** (màu vàng)
- `P(Y)` thay đổi, `P(X|Y)` giữ nguyên
- Visual: pie chart tỷ lệ class thay đổi (class 0: 80% → 20%)
- Ví dụ: *"Bệnh hiếm ở quốc gia A → phổ biến ở quốc gia B"*

**Panel 3: Concept Drift** (màu đỏ) ← nguy hiểm nhất
- `P(Y|X)` thay đổi
- Visual: decision boundary tự di chuyển/xoay — cùng X nhưng label khác
- Ví dụ: *"Email 'Chúc mừng trúng thưởng' năm 2010 là spam. Năm 2025, nó là marketing hợp lệ."*

**Summary tree:** Ba nhánh gộp lại → *"Distribution Shift"* → *"OOD Generalization Problem"*

**Transition:** *"Nhưng tại sao những shift này xảy ra? Vì dữ liệu trong thực tế không bao giờ là một khối đồng nhất — nó **heterogeneous**."*

---

## Scene 4 — Data Heterogeneity: Thông Tin Bị Ẩn `TV2` | ~2.5 phút

**Mystery:** *"Tại sao 'trộn tất cả dữ liệu vào nhau' lại là sai lầm?"*

**Narration:**
> "Data heterogeneity — đa dạng dữ liệu — thường bị xem là noise. Nhưng thực ra, nó là **thông tin bị ẩn**. Nếu ta nhận ra rằng dữ liệu đến từ các environments khác nhau — và khai thác sự khác biệt đó — ta có thể học được thứ mà ERM không bao giờ học được."

**Animation:**
1. **Bước 1:** Pool lớn điểm màu xám *"Raw Data — Unlabeled"*
2. **Bước 2:** Điểm tự nhóm lại thành 3 cluster màu (blue/amber/orange)
   - Label: *"Hospital A"*, *"Hospital B"*, *"Hospital C"*
3. **Bước 3:** Bounding ellipse mỗi cluster xuất hiện
4. **Bước 4:** Arrow chỉ ra sự khác biệt giữa clusters: *"Equipment different"*, *"Patient demographics different"*, *"Protocol different"*
5. **Key insight box:** *"Mỗi cluster = một environment. Sự khác biệt giữa environments = THÔNG TIN."*

**Transition:** *"Nhưng khi model không nhận ra sự khác biệt này, nó mắc vào một cái bẫy tinh vi..."*

---

## Scene 5 — Spurious Correlations: Cái Bẫy Của Model `TV2` | ~2.5 phút

**Mystery:** *"Model đạt 98% accuracy — nhưng nó đã học gì thực sự?"*

**Narration:**
> "Đây là thí nghiệm tư duy. Bạn train một classifier phân biệt bò và lạc đà. Model của bạn đạt 98% accuracy. Bạn rất tự hào. Nhưng hãy nhìn lại data một lần nữa..."

**Animation — "Waterbirds" style walkthrough:**

**Bước 1:** Training data xuất hiện — 2 columns
```
🐄 trên cỏ xanh  →  "COW"   (90% training cases)
🐫 trên sa mạc  →  "CAMEL" (90% training cases)
```
*"Model: learned. Accuracy: 98%"*

**Bước 2:** Model "thinking" visualization
- Feature importance: cỏ xanh sáng lên, hình dạng con bò mờ đi
- Text: *"Điều model thực sự học: CỎ XANH → BÒ"*

**Bước 3:** Test case curveball
```
🐄 trên bãi biển  →  Model dự đoán: "???"
                  →  Kết quả: "CAMEL" ✗
```
Red flash, wrong prediction.

**Bước 4:** Causal graph xuất hiện:
```
    Background (Z)
        ↗       ↘
   Shape (X) ──→ Label (Y)
```
- Highlight: `Z` là **confounder** — nó ảnh hưởng cả X lẫn Y trong training
- `Background → Label`: **SPURIOUS** (đường đứt, màu đỏ)
- `Shape → Label`: **CAUSAL** (đường liền, màu xanh lá)

**Định nghĩa xuất hiện sau visual:** *"Spurious correlation: pattern dự đoán đúng trong training environments nhưng không có quan hệ nhân quả ổn định với label."*

**Transition:** *"Vậy tại sao ERM — thuật toán standard — lại bị lừa bởi spurious correlations?"*

---

## Scene 6 — ERM: Tại Sao Baseline Không Đủ `TV2` | ~2.5 phút

**Mystery:** *"ERM hoạt động hoàn hảo trong lý thuyết — tại sao lại fail trong thực tế?"*

**Narration:**
> "ERM — Empirical Risk Minimization — là nền tảng của hầu hết ML. Ý tưởng: minimize loss trung bình trên training data. Đơn giản, hiệu quả, và... có một điểm mù nguy hiểm."

**Animation:**

**Bước 1:** Formula build-up từng phần (dùng `TransformMatchingTex`):
```
     min_θ
     min_θ (1/n)
     min_θ (1/n) Σᵢ
     min_θ (1/n) Σᵢ L(f_θ(xᵢ), yᵢ)
```
Mỗi phần có label: `minimize` | `average over n samples` | `loss function`

**Bước 2:** Gradient descent visualization — loss landscape 2D contour, ball rolling to minimum
- Label: *"ERM tìm minimum này... nhưng minimum của cái gì?"*

**Bước 3:** Bar chart 3 groups (animate in từng bar):
| Group | % Data | Accuracy |
|-------|--------|---------|
| Majority (cỏ + bò) | 85% | 99% |
| Minority A (bò + beach) | 10% | 71% |
| Minority B (cỏ + lạc đà) | 5% | 43% |
- **ERM average: 95%** → label: *"Looks great! But..."*
- Highlight Group C — flash đỏ: *"Worst group: 43%"*

**Bước 4:** Key insight (2 dòng xuất hiện tuần tự):
> *"ERM hấp thụ TẤT CẢ correlations — causal lẫn spurious."*  
> *"ERM optimize AVERAGE — bỏ qua minority groups."*

**Định nghĩa kết:** *"Vấn đề không phải ERM sai — mà là ERM không được thiết kế để phân biệt correlation và causation."*

**Transition:** *"Vậy ta cần thuật toán được thiết kế để phân biệt điều đó. Đây là IRM."*

---

## Scene 7 — IRM: Học Những Gì Không Đổi `TV3` | ~3 phút

**Mystery:** *"Nếu spurious correlations thay đổi qua environments — feature nào KHÔNG thay đổi?"*

**Narration:**
> "Insight của IRM rất elegant. Nếu một feature thực sự là causal — nó phải hữu ích ở **mọi** environments, không chỉ environment bạn đang train. Ép buộc điều đó là ép buộc model tìm causal features."

**Animation — Step by step:**

**Bước 1:** 3 environments, data points khác màu
- E1 (blue): bò trên cỏ ↔ lạc đà trên cát — background spurious
- E2 (amber): bò trên tuyết ↔ lạc đà trên bãi biển — background khác, spurious vẫn sai
- E3 (orange): bò trên asphalt ↔ lạc đà trên cỏ — background đảo ngược!

**Bước 2:** Feature space representation
```
Raw data x ──→ [Φ: Feature Extractor] ──→ Feature space
```
- Trong feature space: points di chuyển, tách thành 2 cluster rõ ràng

**Bước 3 (KEY ANIMATION):** Classifier `w` trong feature space
- 3 panels cạnh nhau, mỗi panel = 1 environment
- Decision boundary xuất hiện ở panel 1, copy sang panel 2, copy sang panel 3
- **Ràng buộc IRM:** `w` phải GIỐNG NHAU ở cả 3 panels
- Animation: boundary di chuyển tìm vị trí thỏa mãn tất cả
- Spurious features (background): glow đỏ → fade out (chúng không giúp ích đồng đều)
- Causal features (shape): glow xanh lá → bolder (chúng consistent)

**Bước 4:** Formula:
```
min_{Φ, w}  Σ_e R^e(w ∘ Φ)
s.t.    w ∈ argmin_{w̃} R^e(w̃ ∘ Φ)   ∀e ∈ E_train
```
- Highlight `Σ_e`: "tổng qua TẤT CẢ environments"
- Highlight constraint: "w phải optimal ở MỌI env — không chỉ average"

**Bước 5:** IRMv1 practical version (bi-level → gradient penalty):
```
min_{Φ, w}  Σ_e R^e(w ∘ Φ) + λ · Σ_e ‖∇_{w|w=1} R^e(w ∘ Φ)‖²
```
- Explain penalty: *"Nếu Φ đã invariant, gradient này sẽ ≈ 0 ở mọi environment"*

**Limitation note:** *"IRM cần biết environment labels — điều không phải lúc nào cũng có."*

---

## Scene 8 — DRO: Học Từ Trường Hợp Xấu Nhất `TV3` | ~2.5 phút

**Mystery:** *"Nếu không có environment labels — ta tối ưu cho ai?"*

**Narration:**
> "DRO chọn một hướng khác. Thay vì tìm invariant features, nó đặt câu hỏi: 'Điều tệ nhất có thể xảy ra là gì — và ta có thể đảm bảo làm tốt ngay cả trong trường hợp đó không?'"

**Animation:**

**Bước 1:** Contrast ERM vs DRO (side by side):
- ERM: bar chart với average highlight → *"Optimize average risk"*
- DRO: bar chart với **worst bar** highlight → *"Optimize worst-case risk"*

**Bước 2 (KEY):** Uncertainty Set visualization
- Điểm trung tâm P₀ = training distribution
- Vòng tròn `ε`-ball mở rộng xung quanh P₀: *"Tất cả distributions trong phạm vi này đều có thể xảy ra"*
- DRO objective: `min_θ max_{Q: d(Q,P₀) ≤ ε} E_Q[L(θ)]`

**Bước 3:** Min-max game animation
- Một "agent" cố minimize loss (θ, màu xanh)
- Một "adversary" cố maximize loss bằng cách chọn distribution tệ nhất (Q, màu đỏ)
- Equilibrium: *"Robust model"*

**Bước 4:** Group DRO variant (thực tế hơn):
- Các groups predefined (như Waterbirds: 4 groups)
- `min_θ max_g R_g(θ)` — maximize worst-group accuracy
- *"Không cần biết distribution shift cụ thể — chỉ cần biết groups"*

**Bảng So Sánh (animate từng dòng):**

| Phương pháp | Cần gì? | Tối ưu cho | Yếu điểm |
|------------|---------|-----------|---------|
| ERM | Không | Average | Spurious correlations |
| IRM | Environment labels | Invariance | Khó scale, cần nhiều envs |
| Group DRO | Group labels | Worst-group | Conservative, cần group info |

---

## Scene 9 — Stable Learning: Nhìn Từ Góc Nhân Quả `TV4` | ~2.5 phút

**Mystery:** *"Nếu ta biết được cấu trúc nhân quả — ta có thể loại bỏ spurious correlations trực tiếp không?"*

**Narration:**
> "IRM và DRO tiếp cận từ góc optimization. Nhưng còn một cách thứ ba — nhìn thẳng vào cấu trúc **nhân quả** của dữ liệu. Nếu ta hiểu được cái gì gây ra cái gì, ta có thể loại bỏ confounders một cách trực tiếp."

**Animation:**

**Bước 1:** Causal graph xuất hiện từng node:
```
        Z (Season)
       ↗          ↘
X_c (Size)    X_s (Color)
     ↓              ↓
     Y (Label) ←────┘(spurious!)
```
- `X_c → Y`: causal path (stable)
- `Z → X_s → Y`: spurious path qua confounder Z (không stable)

**Bước 2:** Stable Learning approach
- Reweight data points (dot size thay đổi)
- Mục tiêu: làm cho `X_c` và `X_s` trở nên **independent** trong weighted distribution
- *"Nếu X_c và X_s không còn tương quan — model buộc phải dựa vào X_c"*

**Bước 3:** "Triangle of convergence"
```
        Causality (Stable Learning)
           /           \
  Invariance (IRM)  —  Robustness (DRO)
        \           /
      "Ba con đường — một đích đến"
```

**Bước 4:** Full pipeline xuất hiện:
```
Data → Identify Heterogeneity → Partition Environments
     → Learn Invariant/Causal Features
     → Evaluate: Worst-group accuracy, OOD accuracy
```

---

## Scene 10 — Kết Luận: Heterogeneity Là Thông Tin `TV4` | ~2 phút

**Narration:**
> "Hãy cùng nhìn lại. Chúng ta bắt đầu từ một câu hỏi: tại sao AI thất bại ngoài thực tế? Câu trả lời không phải là model không đủ mạnh — mà là chúng ta đã bỏ qua thông tin ẩn trong data: *heterogeneity*."

**Animation:**

**Bước 1:** Rapid recap montage (mỗi concept 1.5s)
```
i.i.d. → Distribution Shift → Heterogeneity → Spurious → ERM Fails
   → IRM → DRO → Stable Learning
```

**Bước 2:** Final comparison (animate từng row):

| | ERM | IRM | Group DRO | Stable Learning |
|--|--|--|--|--|
| **Cần gì** | — | Env labels | Group labels | Causal knowledge |
| **Optimize** | Average | Invariance | Worst-group | Causal features |
| **Điểm mạnh** | Đơn giản | Lý thuyết mạnh | Thực tế | Interpretable |
| **Điểm yếu** | Spurious | Cần envs | Conservative | Domain knowledge |

**Bước 3:** Open problems (fade in tuần tự, mỗi cái kèm icon):
1. 🔍 *Self-aware models* — biết khi nào mình đang OOD
2. 📊 *Uncertainty quantification* — "Tôi không chắc" thay vì confident sai
3. 🏗️ *Scalability* — những kỹ thuật này ở quy mô hàng tỷ samples
4. 🏷️ *Label-free* — IRM/DRO không cần environment/group annotations

**Bước 4:** Final message — lớn, centered, xuất hiện chậm:
> *"Data heterogeneity is not a bug in your dataset —*  
> *it is a feature of the real world.*  
> *And learning to embrace it is how we build AI that actually works."*

**Credits:** Team members + References + CoLLAs 2024 by Peng Cui & Jiashuo Liu

---

## Tổng Thời Lượng Ước Tính

| Scene | TV | Thời lượng |
|-------|----|-----------|
| 1: Intro | TV1 | 1.5 phút |
| 2: i.i.d. | TV1 | 2.0 phút |
| 3: Distribution Shift | TV1 | 2.5 phút |
| 4: Data Heterogeneity | TV2 | 2.5 phút |
| 5: Spurious Correlations | TV2 | 2.5 phút |
| 6: ERM | TV2 | 2.5 phút |
| 7: IRM | TV3 | 3.0 phút |
| 8: DRO | TV3 | 2.5 phút |
| 9: Stable Learning | TV4 | 2.5 phút |
| 10: Conclusion | TV4 | 2.0 phút |
| **Tổng** | | **~24 phút** |
