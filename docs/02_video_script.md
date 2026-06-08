# Kịch Bản Video Animation Manim - Bản 40 Scene

> **Chủ đề:** Data Heterogeneity Analysis for Distribution Shifts  
> **Nguồn chính:** `collas_2024_tutorial_part_1_tong_ket_chi_tiet_vi.md` và `collas_2024_tutorial_part_2_tong_ket_chi_tiet_vi.md`  
> **Mục tiêu:** video giáo dục bằng Manim, dễ theo dõi, nhiều micro-scene ngắn  
> **Thời lượng mục tiêu:** khoảng **65-68 phút**  
> **Nhịp scene:** scene thường 85-100 giây; scene có công thức hoặc ví dụ quan trọng 100-110 giây; scene kết luận dài hơn một chút.  

---

## 0. Nguyên Tắc Bản 40 Scene

Bản 18 scene đã ổn về cấu trúc lớn, nhưng mỗi scene vẫn chứa nhiều ý. Với video Manim giáo dục, cách tốt hơn là tách mỗi nội dung lớn thành nhiều micro-scene:

```text
Một scene = một câu hỏi nhỏ + một visual chính + một takeaway.
```

Lợi ích:

- Người xem không phải giữ quá nhiều khái niệm trong một cảnh.
- Mỗi công thức có scene riêng để xây trực giác trước khi viết ký hiệu.
- Nhóm dễ chia việc hơn: mỗi file Manim chỉ cần polish một visual.
- Tổng thời lượng có buffer an toàn trên 60 phút, kể cả khi voiceover đọc nhanh hoặc cắt bớt pause.

---

## 1. Scene Map 40 Scene

| Scene | File gợi ý | Micro-topic | Thời lượng |
|---|---|---|---|
| 01 | `scene_01_accuracy_fail.py` | Accuracy cao nhưng fail ngoài đời | 1:25 |
| 02 | `scene_02_failure_montage.py` | Robot, camera bóng đá, y tế, tự lái | 1:30 |
| 03 | `scene_03_model_or_data.py` | Model problem hay data problem? | 1:25 |
| 04 | `scene_04_iid_box.py` | i.i.d. bằng chiếc hộp phân phối | 1:45 |
| 05 | `scene_05_train_test_split.py` | Train/test clouds tách nhau | 1:30 |
| 06 | `scene_06_shift_taxonomy.py` | Distribution shift taxonomy | 1:25 |
| 07 | `scene_07_x_shift.py` | `X-shift`: input distribution đổi | 1:30 |
| 08 | `scene_08_yx_shift.py` | `Y|X-shift`: mechanism đổi | 1:45 |
| 09 | `scene_09_data_sources.py` | Data đến từ nhiều sources | 1:25 |
| 10 | `scene_10_pooled_illusion.py` | Pooled dataset illusion | 1:30 |
| 11 | `scene_11_hidden_subpopulations.py` | Subpopulations có `Y|X` khác nhau | 1:45 |
| 12 | `scene_12_pipeline_view.py` | Pipeline: collection -> deployment | 1:30 |
| 13 | `scene_13_erm_formula.py` | ERM formula | 1:45 |
| 14 | `scene_14_average_risk.py` | Average risk che giấu worst groups | 1:40 |
| 15 | `scene_15_spurious_cow_camel.py` | Spurious correlation bò/lạc đà | 1:50 |
| 16 | `scene_16_dro_intuition.py` | DRO: worst-case mindset | 1:30 |
| 17 | `scene_17_uncertainty_set.py` | Uncertainty set và `rho` | 1:40 |
| 18 | `scene_18_f_divergence.py` | f-divergence: reweight support | 1:45 |
| 19 | `scene_19_wasserstein.py` | Wasserstein: optimal transport | 1:45 |
| 20 | `scene_20_dro_limits.py` | Over-pessimism và mismatch | 1:40 |
| 21 | `scene_21_invariant_features.py` | Invariant feature intuition | 1:30 |
| 22 | `scene_22_irm_objective.py` | IRM objective và same classifier `w` | 1:50 |
| 23 | `scene_23_irm_limits.py` | IRM cần environments đủ tốt | 1:40 |
| 24 | `scene_24_clip_contrastive.py` | CLIP contrastive learning | 1:45 |
| 25 | `scene_25_more_data_not_right_data.py` | More data != right data | 1:30 |
| 26 | `scene_26_deductive_inductive.py` | Deductive vs inductive | 1:30 |
| 27 | `scene_27_income_ca_pr.py` | Income prediction CA -> PR | 1:45 |
| 28 | `scene_28_ambiguity_variables.py` | Ambiguity set theo biến shift | 1:40 |
| 29 | `scene_29_mutual_information.py` | Mutual information trực giác | 1:50 |
| 30 | `scene_30_predictive_heterogeneity.py` | Predictive heterogeneity split | 1:50 |
| 31 | `scene_31_crop_yield.py` | Crop yield và crop type ẩn | 1:45 |
| 32 | `scene_32_covid_mortality.py` | COVID mortality: nhiều cơ chế rủi ro | 1:50 |
| 33 | `scene_33_no_env_labels.py` | Pooled data không có env labels | 1:25 |
| 34 | `scene_34_hrm_loop.py` | Heterogeneous Risk Minimization loop | 1:50 |
| 35 | `scene_35_colored_mnist.py` | ColoredMNIST: color vs shape | 1:45 |
| 36 | `scene_36_hard_noisy_samples.py` | Hard samples vs noisy samples | 1:40 |
| 37 | `scene_37_geometric_wasserstein.py` | Data geometry + Geometric Wasserstein | 1:50 |
| 38 | `scene_38_error_slices.py` | Error slices, worst groups | 1:40 |
| 39 | `scene_39_stability_feature.py` | Stability + feature sensitivity | 1:50 |
| 40 | `scene_40_deployment_conclusion.py` | Shift attribution + conclusion | 3:00 |
| **Tổng** |  |  | **~67:25** |

---

## 2. Kịch Bản Theo Scene

### Scene 01 - Accuracy Cao Nhưng Fail Ngoài Đời

**Câu hỏi:** "99% accuracy có đủ để tin model chưa?"  
**Narration:**  
"Hãy bắt đầu bằng một nghịch lý. Một model có test accuracy gần 99%. Dashboard đẹp, loss giảm, validation ổn. Nhưng khi đưa ra ngoài đời, nó vẫn có thể sai trong những tình huống rất bình thường. Nếu chỉ nhìn một con số, ta dễ tưởng model đã hiểu vấn đề. Nhưng có thể nó chỉ hiểu đúng dữ liệu trong phòng thí nghiệm."  
**Manim:** counter `Test accuracy: 99.1%`, chuyển từ xanh sang nứt đỏ.  
**Takeaway:** `High test accuracy is not deployment reliability.`

### Scene 02 - Failure Montage

**Câu hỏi:** "Những failure rất khác nhau có điểm chung gì?"  
**Narration:**  
"Robot hút bụi bị kẹt. Camera bóng đá theo nhầm đầu trọc của trọng tài. Medical AI trong COVID học nhầm tín hiệu bệnh viện. Hệ thống hỗ trợ lái xe phanh sai vì hiểu nhầm bối cảnh. Các lỗi này khác domain, nhưng đều gợi ý cùng một chuyện: dữ liệu deployment không giống dữ liệu training."  
**Manim:** bốn mini-card tự dựng bằng shapes, flash nhanh rồi gom vào `What changed?`  
**Takeaway:** `Failures often begin with a data mismatch.`

### Scene 03 - Model Problem Hay Data Problem?

**Câu hỏi:** "Ta nên sửa model trước hay nhìn lại data trước?"  
**Narration:**  
"Phản xạ thường gặp là thêm layer, thêm data, thêm regularization. Nhưng tutorial nhấn mạnh một góc nhìn data-centric: nhiều model problems thực chất là data problems. Dữ liệu đến từ đâu, có nhóm nào ẩn bên trong, và khi deployment thì nhóm nào thay đổi?"  
**Manim:** hai hộp `Model problem?` và `Data problem?`, zoom vào data box, hiện `sources`, `subpopulations`, `mechanisms`, `shifts`.  
**Takeaway:** `Before changing the model, inspect the data-generating process.`

### Scene 04 - i.i.d. Bằng Chiếc Hộp Phân Phối

**Câu hỏi:** "ML đang tin vào chiếc hộp nào?"  
**Narration:**  
"Trong thế giới i.i.d., train và test được rút độc lập từ cùng một phân phối. Tưởng tượng có một chiếc hộp `P(X,Y)` sinh ra samples. Một phần rơi vào train, một phần rơi vào test. Chúng không giống từng điểm, nhưng giống về luật sinh dữ liệu."  
**Manim:** hộp `P(X,Y)` sinh dots sang hai rổ `train`, `test`; formula `P_train(X,Y)=P_test(X,Y)`.  
**Takeaway:** `i.i.d. means same data-generating distribution.`

### Scene 05 - Train/Test Clouds Tách Nhau

**Câu hỏi:** "Điều gì xảy ra khi chiếc hộp thay đổi?"  
**Narration:**  
"Ngoài đời, người dùng, thiết bị, bệnh viện, quốc gia, mùa vụ đều có thể thay đổi. Khi test cloud tách khỏi train cloud, validation cũ không còn đảm bảo. Model vẫn có thể tự tin, nhưng sự tự tin đó được học từ một thế giới khác."  
**Manim:** train cloud cố định, test cloud dịch xa; accuracy `96% -> 84% -> 69%`; formula đổi sang `P_train != P_target`.  
**Takeaway:** `Distribution shift begins when train and target diverge.`

### Scene 06 - Distribution Shift Taxonomy

**Câu hỏi:** "'Shift' có phải chỉ là một vấn đề không?"  
**Narration:**  
"Distribution shift là tên chung cho nhiều kiểu thay đổi. Có shift ở input, shift ở tỷ lệ label, và shift ở cơ chế `Y|X`. Nếu không phân biệt loại shift, ta rất dễ chọn sai phương pháp robust."  
**Manim:** tree root `Distribution Shift` chia `X-shift`, `Label shift`, `Y|X-shift`.  
**Takeaway:** `Robust to what shift?`

### Scene 07 - X-shift

**Câu hỏi:** "Nếu input distribution đổi nhưng rule vẫn giống thì sao?"  
**Narration:**  
"`X-shift` nghĩa là `P(X)` thay đổi. Ảnh ban ngày sang ban đêm. Người trẻ sang người già. California sang Puerto Rico. Quy luật `Y|X` có thể vẫn giữ, nhưng model chưa thấy đủ vùng input mới."  
**Manim:** density `P_X` màu xanh và `Q_X` màu vàng dịch nhau; boundary giữ nguyên.  
**Takeaway:** `X-shift changes where data appears.`

### Scene 08 - Y|X-shift

**Câu hỏi:** "Nếu cùng input nhưng ý nghĩa label đổi thì sao?"  
**Narration:**  
"`Y|X-shift` nguy hiểm hơn vì cơ chế dự đoán thay đổi. Cùng triệu chứng có thể có ý nghĩa khác ở nhóm tuổi khác. Cùng climate feature ảnh hưởng khác theo crop type. Cùng occupation có ý nghĩa khác trong hai xã hội. Khi mechanism đổi, một single model có thể không còn đúng."  
**Manim:** hai panels có scatter tương tự nhưng decision boundary xoay; highlight `P(Y|X) changes`.  
**Takeaway:** `Y|X-shift changes what the data means.`

### Scene 09 - Data Đến Từ Nhiều Sources

**Câu hỏi:** "Training data có thật sự là một khối không?"  
**Narration:**  
"Dataset hiện đại thường là kết quả merge nhiều nguồn: hospitals, users, regions, sensors, annotators, periods. Sau khi merge, file chỉ còn một bảng, nhưng nguồn gốc khác nhau vẫn để lại cấu trúc bên trong."  
**Manim:** nhiều `Source A/B/C/D` đổ vào `Training data`.  
**Takeaway:** `A dataset is often a mixture.`

### Scene 10 - Pooled Dataset Illusion

**Câu hỏi:** "Điều gì bị mất khi ta pool data?"  
**Narration:**  
"Khi mọi điểm bị tô cùng màu xám, ta train như thể chúng đến từ một cơ chế. Nhưng nếu zoom vào, các clusters có thể tương ứng với bệnh viện, vùng địa lý, nhóm người dùng, hoặc data-generating processes khác nhau."  
**Manim:** dots xám, kính lúp tách thành clusters màu.  
**Takeaway:** `Pooling can hide environments.`

### Scene 11 - Hidden Subpopulations

**Câu hỏi:** "Nếu các nhóm có `Y|X` khác nhau thì sao?"  
**Narration:**  
"Heterogeneity trở nên quan trọng nhất khi các subpopulations có quan hệ `Y|X` khác nhau. Một đường trung bình có thể fit tệ cả hai nhóm. Biết sample thuộc nhóm nào không phải metadata phụ; nó có thể là thông tin dự đoán."  
**Manim:** hai subgroup có hai đường regression khác slope; một line trung bình màu xám fit tệ.  
**Takeaway:** `One average model can hide multiple mechanisms.`

### Scene 12 - Pipeline View

**Câu hỏi:** "Heterogeneity nên được xử lý ở đâu trong pipeline?"  
**Narration:**  
"Tutorial Part 2 đề xuất nhìn toàn bộ pipeline: trước training phát hiện subpopulations; trong training học environments; evaluation đo stability và slices; deployment quy lỗi performance drop cho đúng loại shift."  
**Manim:** pipeline `Collection -> Training -> Evaluation -> Deployment`, mỗi stage có câu hỏi nhỏ.  
**Takeaway:** `OOD generalization is a workflow, not one algorithm.`

### Scene 13 - ERM Formula

**Câu hỏi:** "ERM thật sự tối ưu cái gì?"  
**Narration:**  
"ERM tối thiểu hóa loss trung bình trên training data. Công thức quen thuộc này là nền tảng của ML hiện đại, nhưng chữ quan trọng nhất là average."  
**Manim:** build formula `min_theta (1/n) sum_i L(f_theta(x_i), y_i)`, highlight `(1/n) sum`.  
**Takeaway:** `ERM optimizes average training risk.`

### Scene 14 - Average Risk Che Giấu Worst Groups

**Câu hỏi:** "Average cao có che giấu nhóm yếu không?"  
**Narration:**  
"Nếu majority group chiếm 85% và accuracy 99%, average vẫn đẹp ngay cả khi minority group chỉ đạt 43%. Trong y tế, tín dụng, tuyển dụng, nhóm nhỏ có thể là nhóm quan trọng nhất."  
**Manim:** bar chart majority/minority/worst; big `95% average` vỡ ra thành slices.  
**Takeaway:** `Average performance can hide local failure.`

### Scene 15 - Spurious Cow/Camel

**Câu hỏi:** "Model đã học con vật hay học background?"  
**Narration:**  
"Nếu bò thường ở cỏ và lạc đà thường ở sa mạc, ERM có thể học background. Trên test, bò ở bãi biển có thể bị dự đoán sai. Đây là spurious correlation: pattern đúng trong training nhưng không ổn định khi environment đổi."  
**Manim:** cow/grass, camel/desert, feature importance background sáng đỏ, shape sáng xanh.  
**Takeaway:** `Spurious correlations exploit the training environment.`

### Scene 16 - DRO Intuition

**Câu hỏi:** "Nếu average không đủ, ta tối ưu worst-case được không?"  
**Narration:**  
"DRO đổi câu hỏi từ tốt trên training distribution sang tốt trên phân phối xấu nhất trong một tập phân phối. Model chọn `theta`, adversary chọn `Q` làm loss cao nhất."  
**Manim:** transform ERM objective sang `min_theta sup_Q E_Q[loss]`; two-player min-max.  
**Takeaway:** `DRO prepares for a chosen family of bad shifts.`

### Scene 17 - Uncertainty Set

**Câu hỏi:** "Worst-case được chọn trong vùng nào?"  
**Narration:**  
"DRO cần uncertainty set: mọi distribution `Q` cách `P_train` không quá `rho`. Nếu `rho` quá nhỏ, shift thật nằm ngoài. Nếu quá lớn, worst-case có thể quá cực đoan."  
**Manim:** point `P_train`, ball radius `rho`, slider tăng/giảm.  
**Takeaway:** `The uncertainty set is the core assumption of DRO.`

### Scene 18 - f-divergence

**Câu hỏi:** "Nếu shift chỉ là đổi trọng số nhóm thì sao?"  
**Narration:**  
"f-divergence so sánh phân phối qua density ratio `dQ/dP`. Trực giác là reweight support đã có: training 70% người già, 30% người trẻ; target có thể đổi tỷ lệ này."  
**Manim:** age groups 70/30 chuyển sang 40/60; label `reweight existing support`.  
**Takeaway:** `f-divergence imagines shifts by reweighting.`

### Scene 19 - Wasserstein

**Câu hỏi:** "Nếu shift có geometry thì sao?"  
**Narration:**  
"Wasserstein distance đo chi phí vận chuyển khối lượng xác suất. Nó không chỉ hỏi trọng số khác bao nhiêu, mà hỏi mass phải di chuyển xa thế nào. Vì vậy nó phù hợp khi geometry của dữ liệu quan trọng."  
**Manim:** two distributions, arrows transport mass, cost labels.  
**Takeaway:** `Wasserstein sees geometry through transport cost.`

### Scene 20 - DRO Limits

**Câu hỏi:** "Worst-case có giống target thật không?"  
**Narration:**  
"DRO giả định worst-case trong uncertainty set đại diện cho real shifts. Nếu mismatch, model tối ưu cho một distribution không xảy ra. Nếu quá bi quan, model học một bài toán khó không cần thiết."  
**Manim:** `Q*` trong ball hướng khác `Q_real`; red mismatch arrow.  
**Takeaway:** `Good DRO needs realistic shifts.`

### Scene 21 - Invariant Features

**Câu hỏi:** "Feature nào còn đúng khi environment đổi?"  
**Narration:**  
"Invariant learning bắt đầu từ ý tưởng: causal hoặc stable features nên hữu ích qua nhiều environments. Background của ảnh có thể đổi, nhưng shape của vật thể ổn định hơn."  
**Manim:** cow/camel qua ba environments, background đổi, shape glow xanh.  
**Takeaway:** `Stable features survive environment changes.`

### Scene 22 - IRM Objective

**Câu hỏi:** "Làm sao ép representation học feature invariant?"  
**Narration:**  
"IRM học representation `Phi(X)` sao cho cùng một classifier `w` là tối ưu trên mọi training environment. Nếu `w` phải dùng được ở mọi nơi, representation không nên giữ feature chỉ hữu ích cục bộ."  
**Manim:** `X -> Phi(X) -> w -> Y`; three panels share same decision boundary; formula IRM.  
**Takeaway:** `IRM asks for one optimal classifier across environments.`

### Scene 23 - IRM Limits

**Câu hỏi:** "Điều gì xảy ra nếu environments không đủ tốt?"  
**Narration:**  
"Nếu environment labels không có, hoặc mọi training environment đều có cùng spurious correlation, feature spurious cũng trông invariant. IRM cần environments đủ đa dạng để lộ ra sự không ổn định."  
**Manim:** three train envs đều grass->cow, test đảo; label `Looks invariant in train`.  
**Takeaway:** `Bad environments produce bad invariance.`

### Scene 24 - CLIP Contrastive Learning

**Câu hỏi:** "Model lớn và data lớn giúp gì?"  
**Narration:**  
"CLIP học từ image-caption pairs. Image encoder và text encoder đưa ảnh và text vào cùng embedding space, kéo cặp đúng lại gần và đẩy cặp sai ra xa. Nhờ đó model có khả năng zero-shot."  
**Manim:** image/text encoders -> vectors -> embedding space.  
**Takeaway:** `Pretraining can learn broad representations.`

### Scene 25 - More Data != Right Data

**Câu hỏi:** "Thêm data có luôn robust hơn không?"  
**Narration:**  
"Tutorial nhấn mạnh: số lượng data không đảm bảo robustness. Trong y tế, tự lái, khoa học và chính sách công, dữ liệu đúng rất đắt. Câu hỏi là cần thu thêm loại data nào, ở vùng nào, cho nhóm nào."  
**Manim:** large data mountain, target shift outside coverage; warning text.  
**Takeaway:** `More data is not the same as the right data.`

### Scene 26 - Deductive vs Inductive

**Câu hỏi:** "Ta nên bắt đầu từ method hay từ hiện tượng thật?"  
**Narration:**  
"Deductive bắt đầu từ giả định rồi suy ra method. Inductive bắt đầu từ dữ liệu thật, lỗi thật, shift pattern thật, rồi mới thiết kế giả định hoặc chọn method phù hợp."  
**Manim:** two-column flow: assumption->method->data vs data->shift->assumption->method.  
**Takeaway:** `Start from observed shifts.`

### Scene 27 - Income CA -> PR

**Câu hỏi:** "Performance drop đến từ input hay mechanism?"  
**Narration:**  
"Trong income prediction, source là California và target là Puerto Rico. Drop có thể đến từ `X-shift`: work hours, education, occupation khác phân phối. Nhưng cũng có thể đến từ `Y|X-shift`: cùng occupation có ý nghĩa khác do bối cảnh xã hội và ngôn ngữ."  
**Manim:** California -> Puerto Rico, feature chips bay qua, source-target accuracy plot lệch line.  
**Takeaway:** `Target drop can mix X-shift and Y|X-shift.`

### Scene 28 - Ambiguity Set Theo Biến

**Câu hỏi:** "DRO nên robust trên biến nào?"  
**Narration:**  
"Thay vì chọn ambiguity set trừu tượng, ta có thể chọn theo biến có subgroup differences lớn: age, education, occupation, income. Performance thay đổi mạnh tùy biến được chọn."  
**Manim:** feature selector, ambiguity set đổi shape, bar chart performance theo selected variables.  
**Takeaway:** `Robustness must be tied to the variables that shift.`

### Scene 29 - Mutual Information

**Câu hỏi:** "X giúp giảm bất định của Y bao nhiêu?"  
**Narration:**  
"Mutual information đo lượng thông tin `X` cung cấp về `Y`. `H(Y)` là bất định ban đầu. `H(Y|X)` là bất định còn lại sau khi biết `X`. Phần giảm đi là `I(X;Y)`."  
**Manim:** entropy bar shrinking; formula `I(X;Y)=H(Y)-H(Y|X)`.  
**Takeaway:** `Information is uncertainty reduction.`

### Scene 30 - Predictive Heterogeneity

**Câu hỏi:** "Khi nào một split subgroup giúp prediction?"  
**Narration:**  
"Predictive heterogeneity tìm split `E` sao cho biết `E` làm tăng thông tin dự đoán của `X` về `Y`. Nếu split làm `I_v(Y;X|E)-I_v(Y;X)` lớn, groups đó phản ánh cơ chế dự đoán khác nhau."  
**Manim:** formula `sup_E I_v(Y;X|E)-I_v(Y;X)`, bad split vs good split.  
**Takeaway:** `Useful groups change the predictive relationship.`

### Scene 31 - Crop Yield

**Câu hỏi:** "Một biến ẩn có thể lộ ra qua prediction không?"  
**Narration:**  
"Trong crop yield, climate features dự đoán năng suất, nhưng crop type ảnh hưởng cơ chế. Predictive heterogeneity có thể học ra subpopulations tương ứng với hai crop types dù biến này bị ẩn."  
**Manim:** true crop map vs learned split map, alignment highlight.  
**Takeaway:** `Hidden mechanisms can be discovered through prediction.`

### Scene 32 - COVID Mortality

**Câu hỏi:** "Một average model che giấu cơ chế rủi ro nào?"  
**Narration:**  
"Với COVID mortality, ERM thấy các top features trung bình. Nhưng split subpopulations cho thấy một nhóm lớn tuổi bị chi phối bởi underlying diseases, nhóm khác trải rộng tuổi nhưng có triệu chứng COVID nghiêm trọng."  
**Manim:** ERM feature chart -> split into two feature charts.  
**Takeaway:** `One dataset can contain multiple risk mechanisms.`

### Scene 33 - No Environment Labels

**Câu hỏi:** "Nếu source labels bị mất thì IRM làm sao?"  
**Narration:**  
"Modern datasets thường merge nhiều nguồn mà không lưu environment labels. Khi chỉ có pooled data, invariant learning không biết phải so sánh qua environments nào."  
**Manim:** sources with tags -> funnel -> tags disappear.  
**Takeaway:** `Sometimes environments must be learned.`

### Scene 34 - HRM Loop

**Câu hỏi:** "Có thể vừa học environments vừa học predictor không?"  
**Narration:**  
"Heterogeneous Risk Minimization có hai module: heterogeneity identification học environments từ variant features, invariant prediction học predictor ổn định từ learned environments. Hai module boost lẫn nhau qua nhiều iteration."  
**Manim:** loop `Identification <-> Invariant prediction`, group separation and accuracy increase.  
**Takeaway:** `Environment discovery and invariant learning can co-evolve.`

### Scene 35 - ColoredMNIST

**Câu hỏi:** "Màu hay hình dạng mới là signal ổn định?"  
**Narration:**  
"ColoredMNIST minh họa rõ spurious feature. Màu sắc tương quan với label trong train nhưng có thể đảo ở test. Hình dạng chữ số mới là signal ổn định hơn."  
**Manim:** digits colored red/green, train correlation, test inversion, shape outline glow.  
**Takeaway:** `Spurious color fails when environments change.`

### Scene 36 - Hard vs Noisy Samples

**Câu hỏi:** "Loss cao có luôn đáng upweight không?"  
**Narration:**  
"DRO tập trung vào loss cao, nhưng loss cao có thể là hard sample có ý nghĩa hoặc noisy sample cô lập. Nếu không phân biệt, model có thể học noise."  
**Manim:** scatter: minority cluster and isolated outlier both high loss, labels split hard/noisy.  
**Takeaway:** `High loss is ambiguous.`

### Scene 37 - Geometric Wasserstein

**Câu hỏi:** "Geometry giúp phân biệt hard và noise thế nào?"  
**Narration:**  
"Hard samples thường nằm trong neighborhood có cấu trúc; noisy samples thường cô lập. Geometric Wasserstein đưa manifold geometry vào DRO để density transfer mượt theo cấu trúc dữ liệu, không tập trung quá mức vào outliers."  
**Manim:** manifold curve, graph edges, transport arrows follow manifold and avoid outlier.  
**Takeaway:** `Robustness should respect data geometry.`

### Scene 38 - Error Slices

**Câu hỏi:** "Model yếu ở vùng dữ liệu nào?"  
**Narration:**  
"Average accuracy không đủ. Ta cần error slice discovery: tìm subgroups hoặc regions mà model perform poorly. Điều này giúp biết nên thu thêm data, patch model, hoặc giới hạn deployment ở đâu."  
**Manim:** `Accuracy 95%` breaks into slices, worst slice 43% highlighted.  
**Takeaway:** `Find where the model fails, not only how often.`

### Scene 39 - Stability + Feature Sensitivity

**Câu hỏi:** "Model nhạy cảm với shift nào và feature nào?"  
**Narration:**  
"Stability evaluation hỏi phải dịch distribution bao xa mới chạm failure set. Feature stability hỏi perturb feature nào làm performance giảm. Một model robust với corruption chưa chắc robust với subpopulation shift."  
**Manim:** distance to failure set, two shift panels, feature sliders with performance drop.  
**Takeaway:** `Robustness must name the shift and the sensitive features.`

### Scene 40 - Deployment Attribution + Conclusion

**Câu hỏi:** "Khi performance giảm, sửa bằng cách nào?"  
**Narration:**  
"Sau deployment, performance drop có thể do `X-shift`, `Y|X-shift`, hoặc cả hai. Shared distribution giữa `P` và `Q` tập trung vào vùng overlap để tách sampling change khỏi mechanism change. Chỉ khi hiểu shift, ta mới chọn đúng can thiệp: reweight, adapt, thu target data, hay thu feature mới."

"Thông điệp cuối: OOD generalization không phải một thuật toán đơn lẻ. Nó là workflow heterogeneity-aware. Không phải cứ model lớn hơn là generalize tốt hơn. Không phải cứ nhiều data hơn là robust hơn. Điểm bắt đầu đúng là hiểu data heterogeneity."  
**Manim:** shared distribution formula, path `P -> S -> Q`, recap cards, final title.  
**Takeaway:** `Learn the heterogeneity before fighting the shift.`

---

## 3. Phân Công Đề Xuất Cho 4 Thành Viên

| Thành viên | Scenes | Trọng tâm |
|---|---|---|
| TV1 | 01-10 | Hook, i.i.d., shift taxonomy, heterogeneity foundations |
| TV2 | 11-20 | Subpopulation intuition, ERM, spurious, DRO foundations |
| TV3 | 21-30 | IRM, CLIP, inductive approach, predictive heterogeneity |
| TV4 | 31-40 | Case studies, learned environments, geometry, evaluation, conclusion |

---

## 4. Checklist Bao Phủ Tutorial

- [x] Failure cases và data perspective.
- [x] i.i.d., distribution shift, `X-shift`, `Y|X-shift`.
- [x] Data heterogeneity, hidden subpopulations, pipeline view.
- [x] ERM, average risk, spurious correlations.
- [x] DRO, uncertainty set, f-divergence, Wasserstein, limitations.
- [x] IRM, invariant learning, environment limitations.
- [x] CLIP/pretrained big models, more data != right data.
- [x] Deductive vs inductive, CA -> PR, ambiguity set theo biến.
- [x] Mutual information, predictive heterogeneity.
- [x] Crop yield, COVID mortality.
- [x] No environment labels, HRM, ColoredMNIST.
- [x] Hard/noisy samples, data geometry, Geometric Wasserstein.
- [x] Error slices, stability, feature sensitivity.
- [x] Shared distribution, shift attribution, future directions.
