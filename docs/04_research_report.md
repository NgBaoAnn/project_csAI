# Research Report: Data Heterogeneity & OOD Generalization

> **Mục đích:** Tài liệu nghiên cứu sâu để team hiểu đúng nội dung học thuật trước khi code scenes.  
> **Nguồn:** Tổng hợp từ tutorial CoLLAs 2024 + papers gốc IRM, DRO, Stable Learning.

---

## 1. Bức Tranh Tổng Thể

Vấn đề OOD Generalization có thể được nhìn qua **Stable Learning trilogy** — ba góc nhìn bổ sung nhau:

| Góc nhìn | Framework | Giả định | Phương pháp |
|----------|-----------|---------|------------|
| **Invariance** | IRM, IRM-variants | Biết environment labels | Tìm invariant predictor |
| **Robustness** | DRO, Group DRO | Biết groups / uncertainty set | Optimize worst-case |
| **Causality** | Stable Learning, StableNet | Có causal graph / decorrelation | Sample reweighting |

Ba hướng cùng nhắm đến: **model không bị lừa bởi spurious correlations**.

---

## 2. ERM — Baseline Và Giới Hạn

### Formulation
```
min_θ  R̂(θ) = (1/n) Σᵢ L(f_θ(xᵢ), yᵢ)
```

### Tại Sao ERM Fail Với Heterogeneous Data?

ERM minimize **average** loss. Khi data heterogeneous (đến từ nhiều environments), nó hấp thụ **tất cả** correlations — causal lẫn spurious — miễn là chúng giảm average loss. Ví dụ:

Giả sử 90% training data có correlation "cỏ → bò". ERM sẽ:
- Học correlation này → giảm loss trên 90% data
- Bỏ qua việc "shape → label" ổn định hơn
- Kết quả: hoạt động tốt trên training distribution, fail khi test distribution thay đổi

**Metrics đánh giá tốt hơn average accuracy:**
- **Worst-group accuracy**: accuracy trên nhóm tệ nhất → phát hiện unfairness
- **OOD accuracy**: accuracy trên test distribution khác training

---

## 3. Invariant Risk Minimization (IRM)

### Nguồn gốc
- **Paper:** Arjovsky, M., Bottou, L., Gulrajani, I., Lopez-Paz, D. (2019). *Invariant Risk Minimization.* arXiv:1907.02893
- **Key idea:** Features causal là features **invariant** qua environments — bất kể environment nào, causal relationship giữa feature và label không thay đổi.

### Formulation Chính Xác

**Định nghĩa (Invariant Predictor):** Predictor `w ∘ Φ` là invariant across environments E nếu:
```
∃ w:  w ∈ argmin_{w̃} R^e(w̃ ∘ Φ)   ∀e ∈ E
```
(Tồn tại classifier `w` tối ưu đồng thời ở *mọi* environment e)

**IRM Optimization Problem:**
```
min_{Φ, w}   Σ_{e∈E_train} R^e(w ∘ Φ)
subject to:  w ∈ argmin_{w̃} R^e(w̃ ∘ Φ)    ∀e ∈ E_train
```

Đây là bi-level optimization — khó solve trực tiếp.

**IRMv1 (Practical Approximation):**
```
min_{Φ, w}   Σ_e R^e(w ∘ Φ) + λ · Σ_e ‖∇_{w|w=1} R^e(w ∘ Φ)‖²
```
- **λ**: trade-off hyperparameter giữa ERM term và invariance penalty
- **Gradient penalty**: nếu `Φ` đã elicit invariant predictor, gradient tại `w=1.0` sẽ ≈ 0 ở mọi environment
- **Khi λ→∞**: model buộc phải satisfy invariance constraint hoàn toàn
- **Khi λ=0**: ERM thông thường

### Intuition Cho Video (3B1B Style)
> *"Hãy tưởng tượng 3 phòng học khác nhau. Thầy giáo giỏi nhất phải dạy hiệu quả ở cả 3 phòng — không thể rely vào điều gì đặc biệt của phòng này mà không có ở phòng kia. IRM tìm features có tính chất đó."*

### Hạn Chế (Quan Trọng Cho Scene 7)
- Cần environment labels (không phải lúc nào cũng có)
- Về lý thuyết, cần số environments ≥ số spurious features + 1
- Trong thực tế, IRMv1 có thể không converge khi λ quá lớn

---

## 4. Distributionally Robust Optimization (DRO)

### Nguồn gốc
- **Paper (Group DRO):** Sagawa, S., Koh, P.W., Hashimoto, T., Liang, P. (2020). *Distributionally Robust Neural Networks.* ICLR 2020. arXiv:1911.08731
- **Key idea:** Thay vì average, optimize cho **worst-case distribution** trong một uncertainty set.

### Formulation

**General DRO:**
```
min_θ  max_{Q ∈ U}  E_Q[L(f_θ(x), y)]
```
Trong đó U là uncertainty set (ví dụ: Wasserstein ball xung quanh P_train).

**Group DRO (Sagawa et al.):**
```
min_θ  max_{g ∈ G}  R_g(θ)
```
Trong đó `R_g(θ) = E_{(x,y)∼P_g}[L(f_θ(x), y)]` là loss trên group g.

**Algorithm (Online reweighting):**
```python
# Khởi tạo group weights đều nhau
q = [1/|G|] * |G|

for batch in training:
    # Forward pass, tính loss theo group
    group_losses = compute_group_losses(batch)
    
    # Upweight group có loss cao nhất
    q = q * exp(η * group_losses)
    q = q / q.sum()  # Normalize
    
    # Weighted loss
    loss = sum(q[g] * group_losses[g] for g in G)
    loss.backward()
```

### Clarification: Wasserstein vs Group DRO
- **Group DRO** (Sagawa 2020): uncertainty set = simplex over predefined groups. **Không dùng Wasserstein.**
- **Wasserstein DRO**: uncertainty set = ball in Wasserstein metric space — extension sau, dùng khi không có group labels.
- Cho video của nhóm: tập trung vào **Group DRO** (đơn giản hơn, benchmark rõ ràng hơn).

### Intuition Cho Video
> *"ERM như học sinh ôn thi theo đề trung bình. DRO như học sinh ôn cho đề KHÓ NHẤT trong history — dù không biết đề năm nay là gì, nhưng chắc chắn không bị bất ngờ."*

### Worst-Group Accuracy Metric
- **Waterbirds benchmark:** 4 groups = {Waterbird, Landbird} × {Water bg, Land bg}
- ERM: avg accuracy ~97%, but worst-group accuracy ~63%
- Group DRO: avg accuracy ~91%, worst-group accuracy ~91%
- Đây là **trade-off**: DRO hy sinh average để nâng worst-group

---

## 5. Stable Learning

### Nguồn gốc
- **Kuang et al. (2018):** *Stable Prediction across Unknown Environments.* KDD 2018. arXiv:1905.11374
- **Shen et al. (2020):** *Stable Learning via Sample Reweighting.* AAAI 2020.
- **StableNet:** Deep learning extension dùng Random Fourier Features.
- **Nhóm tác giả:** Kun Kuang, Peng Cui (chính là speaker của tutorial!)

### Core Idea: Feature Decorrelation

Vấn đề: Trong training data, features thường **correlated** nhau (do confounders). Điều này khiến model khó phân biệt causal features và spurious features.

**Giải pháp:** Tìm weights `{wᵢ}` cho mỗi sample i sao cho trong **weighted distribution**, tất cả feature pairs trở nên **independent**:

```
Cov_{weighted}(Xₖ, Xₗ) ≈ 0    ∀k ≠ l
```

Khi features independent, model buộc phải đánh giá contribution của từng feature riêng lẻ → dễ identify causal features hơn.

### Causal Graph Perspective

```
        Z (Confounder — Season, Location, ...)
       ↗              ↘
X_causal              X_spurious
(size, shape)         (color, background)
      ↘              ↙
           Y (Label)
```

- `Z` tạo ra spurious correlation: `X_spurious ↔ X_causal` trong training
- Sample reweighting "cancel" ảnh hưởng của Z, làm X features trở nên independent
- Model sau đó chỉ có thể rely vào features có direct causal path đến Y

### Connection IRM-DRO-Stable Learning
```
             Muốn: Model chỉ dùng CAUSAL FEATURES
                         /         \
               Invariance          Causality
                   |                   |
                  IRM            Stable Learning
                   \               /
                   Trong environments khác nhau,
                   causal relationships invariant
                         |
                      Robustness
                         |
                        DRO
                   (không cần biết causal structure)
```

---

## 6. Benchmarks & Evaluation

### Cách Đánh Giá OOD Generalization (DomainBed)

**DomainBed** (Gulrajani & Lopez-Paz, 2021) standardize đánh giá bằng cách:
1. Fix hyperparameter selection protocol (không dùng test data để select)
2. Multiple random seeds
3. Nhiều datasets trong cùng suite

**Kết quả đáng chú ý:** Nhiều bài paper claim "IRM beats ERM" nhưng khi DomainBed evaluate lại với fair protocol, ERM với đúng regularization competitive với nhiều OOD methods.

### Dataset Reference

#### ColoredMNIST (IRM paper)
- **Spurious:** Màu chữ số (red/green) correlated 90% với label
- **Causal:** Hình dạng chữ số (invariant)
- **Environments:** E1 (90% correlation), E2 (80% correlation), E3 (10% correlation = test)
- **ERM result:** ~17% test accuracy (gần random)
- **IRM result:** ~70% test accuracy

#### Waterbirds (Group DRO paper)
- **Setup:** CUB bird images + Places background (synthetic paste)
- **Spurious:** Background (water/land) correlated với bird type (waterbird/landbird) = 95%
- **Groups:** 4 groups = 2 bird types × 2 background types
- **ERM:** Worst-group acc ~63%, avg ~97%
- **Group DRO:** Worst-group acc ~91%, avg ~91%

#### NICO++ (Peng Cui's lab — tutorial speakers)
- **Scale:** 80 categories, 230K+ images
- **Dual label:** Main concept (dog, cat) + Context (on grass, in water, in snow...)
- **Controllable shift:** Adjust context distribution in train/test splits
- **Novel metrics:** Quantifies both covariate shift AND concept shift separately
- **GitHub:** https://github.com/xxgege/NICO

---

## 7. Open Problems (Cho Scene 10)

### Chính Thức Từ Tutorial
1. **Environment labeling without supervision:** IRM cần env labels — làm sao tự động discover environments?
2. **Sample efficiency:** Các methods OOD thường cần nhiều data hơn ERM
3. **Theoretical guarantees:** IRM/DRO có converge với finite envs/groups không? Đến đâu?

### Từ Cộng Đồng Nghiên Cứu (2023-2024)
4. **When does IRM work?** — "Risks of IRM" (Rosenfeld et al.) show IRM fails khi số environments không đủ
5. **Unlabeled OOD data:** Test-time adaptation — adapt model ngay khi gặp OOD data
6. **Foundation models & OOD:** Large pretrained models (CLIP, GPT-4) đã robust với distribution shift chưa?
7. **Causal discovery at scale:** Tự động tìm causal graph từ data — bottleneck của Stable Learning

---

## 8. Bibliography (Đầy Đủ)

| Ref | Citation |
|-----|---------|
| [1] | Arjovsky, M., Bottou, L., Gulrajani, I., & Lopez-Paz, D. (2019). *Invariant Risk Minimization.* arXiv:1907.02893 |
| [2] | Sagawa, S., Koh, P. W., Hashimoto, T. B., & Liang, P. (2020). *Distributionally Robust Neural Networks for Group Shifts.* ICLR 2020. arXiv:1911.08731 |
| [3] | Kuang, K., Cui, P., Athey, S., Xiong, R., & Li, B. (2018). *Stable Prediction across Unknown Environments.* KDD 2018. arXiv:1905.11374 |
| [4] | Shen, Z., Cui, P., Zhang, T., & Kuang, K. (2020). *Stable Learning via Sample Reweighting.* AAAI 2020 |
| [5] | Shen, J., et al. (2021). *Towards Out-of-Distribution Generalization: A Survey.* arXiv:2108.13624 |
| [6] | Gulrajani, I., & Lopez-Paz, D. (2021). *In Search of Lost Domain Generalization.* ICLR 2021 (DomainBed) |
| [7] | He, Y., Shen, Z., & Cui, P. (2021). *Towards Non-I.I.D. Image Classification: A Dataset and Baselines (NICO).* Pattern Recognition |
| [8] | Zhang, X., et al. (2022). *NICO++: Towards Better Benchmarking for Domain Generalization.* CVPR 2022 |
| [9] | Rosenfeld, E., Ravikumar, P., & Risteski, A. (2021). *The Risks of Invariant Risk Minimization.* ICLR 2021. arXiv:2010.05761 |
| [10] | Zhang, H., et al. (2021). *Deep Stable Learning for Out-of-Distribution Generalization (StableNet).* CVPR 2021 |
