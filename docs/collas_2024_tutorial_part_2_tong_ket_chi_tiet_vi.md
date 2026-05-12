# Tổng kết chi tiết Video 2 - Towards Heterogeneity-Aware Machine Learning

Nguồn video: https://www.youtube.com/watch?v=vHfv2ZXSWvU

Tài liệu nền đã dùng trong workspace:

- Transcript lời nói: `collas_2024_tutorial_part_2_transcript.md`
- Ghi chú học tập: `collas_2024_tutorial_part_2_study_notes_vi.md`
- Ghi chú hình ảnh/slide: `collas_2024_tutorial_part_2_visual_notes_vi.md`
- Contact sheets: `contact_sheets/part_2_sheet_01.jpg` đến `contact_sheets/part_2_sheet_06.jpg`

> Lưu ý: transcript gốc lấy từ phụ đề tự động của YouTube nên có lỗi nhận dạng. Trong bản tổng kết này, các thuật ngữ đã được chuẩn hóa theo nội dung slide và bối cảnh học thuật: `hyrogen/hydrogen` được hiểu là `heterogeneity`, `ships` là `shifts`, `DR/DRL` là `DRO`, `inance` là `invariance`.

## 1. Mục tiêu chính của video

Video 2 tiếp nối Video 1. Nếu Video 1 review các hướng tiếp cận hiện có và chỉ ra giới hạn của chúng, thì Video 2 đi vào phần quan trọng hơn: **làm thế nào để xây dựng machine learning có nhận thức về data heterogeneity**.

Ý tưởng trung tâm là:

> Trước khi chọn thuật toán, ta cần hiểu dữ liệu của mình heterogeneous như thế nào, shift xảy ra ở đâu, và loại heterogeneity nào đang làm model thất bại.

Video tổ chức nội dung theo toàn bộ pipeline ML:

```text
Data collection -> Model training -> Model evaluation -> Deployment
```

Mỗi giai đoạn đều có một câu hỏi chính:

- Trước training: dữ liệu có các subpopulation khác nhau không?
- Trong training: có thể học hoặc khai thác environments như thế nào?
- Khi evaluation: model yếu ở vùng dữ liệu nào và nhạy cảm với shift nào?
- Sau deployment: khi performance giảm, ta quy lỗi cho loại shift nào và nên can thiệp ra sao?

## 2. 00:00-02:00 - Recap và câu hỏi còn thiếu

Video bắt đầu bằng recap từ phần trước:

- **Shift** là sự không khớp giữa training distribution `P` và target/deployment distribution `Q`.
- **Robustness** là việc performance không xấu đi nhiều khi target distribution khác training distribution.
- **Heterogeneity** là việc dữ liệu được sinh ra từ một mixture đa dạng của nhiều distributions, sources, subpopulations hoặc mechanisms.

Sau khi đã biết các method như DRO, IRM và pretrained models, tutorial đặt ra hai câu hỏi còn thiếu:

1. Làm sao đo lường data heterogeneity?
2. Làm sao phân tích pattern của distribution shift?

Đây là hai câu hỏi dẫn đến heterogeneity-aware machine learning.

## 3. 02:00-09:00 - Stage 1: Phân tích heterogeneous subpopulations trước khi training

### 3.1. Vì sao phải kiểm tra subpopulations?

Slide "Perspective 1" nói rõ: sau khi thu thập dữ liệu, ta cần biết training data có chứa các subpopulation với `Y|X` khác nhau hay không.

Điều này quan trọng vì nhiều method invariance giả định rằng quan hệ `X -> Y` là giống nhau trên toàn bộ population. Nhưng trong thực tế, giả định này có thể sai.

Ví dụ:

- Trong y tế, triệu chứng giống nhau có thể mang ý nghĩa khác nhau ở các nhóm tuổi khác nhau.
- Trong nông nghiệp, cùng một climate feature có thể ảnh hưởng khác nhau đến crop yield tùy loại cây trồng.
- Trong tài chính hoặc xã hội, cùng một feature có thể có ý nghĩa khác nhau giữa các vùng địa lý hoặc nhóm dân cư.

Nếu `Y|X` thật sự khác nhau giữa các subpopulation, ép một model invariant chung cho tất cả có thể làm mất thông tin quan trọng.

### 3.2. Predictive heterogeneity

Method đầu tiên được giới thiệu là **predictive heterogeneity**.

Mục tiêu:

> Chia dataset thành các subpopulation có quan hệ dự đoán `Y|X` khác nhau, sao cho việc chia này tạo thêm thông tin hữu ích cho prediction.

Slide đưa công thức dạng:

```text
sup_{E is a split} I_v(Y; X | E) - I_v(Y; X)
```

Ý nghĩa:

- `E` là cách chia dữ liệu thành các groups/environments.
- `I_v(Y; X)` là lượng thông tin mà `X` cung cấp để dự đoán `Y` khi xem toàn bộ dữ liệu là một khối.
- `I_v(Y; X | E)` là lượng thông tin khi biết thêm dữ liệu thuộc subgroup nào.
- Nếu chênh lệch lớn, việc chia subgroup giúp dự đoán tốt hơn, nghĩa là dữ liệu có predictive heterogeneity.

### 3.3. Mutual information - trực giác cần nắm

Video nhắc lại mutual information:

```text
I(X;Y) = H(Y) - H(Y|X)
```

Trong đó:

- `H(Y)` đo độ bất định của label `Y`. Có thể hiểu là độ khó ban đầu của bài toán.
- `H(Y|X)` đo độ bất định còn lại của `Y` sau khi đã biết `X`.
- `I(X;Y)` đo `X` giúp giảm bất định của `Y` được bao nhiêu.

Nếu chia dữ liệu thành subgroups làm mutual information tăng, tức là subgroup label/environment cung cấp thêm thông tin dự đoán.

### 3.4. Ví dụ nông nghiệp

Bài toán: dự đoán crop yield từ climate features như nhiệt độ, gió, mưa, điều kiện khí hậu.

Vấn đề: crop type ảnh hưởng đến cơ chế dự đoán, nhưng model ban đầu không có feature crop type.

Slide so sánh:

- Bản đồ chia thật theo hai loại cây.
- Bản đồ hai subpopulation học được bằng predictive heterogeneity.

Kết quả: hai subpopulation học được tương ứng khá tốt với hai crop types. Điều này cho thấy method có thể phát hiện một biến ẩn quan trọng ảnh hưởng đến prediction mechanism.

Bài học: nếu data có các cơ chế sinh khác nhau, ta không nên vội trộn tất cả vào một model chung.

### 3.5. Ví dụ COVID-19 mortality

Bài toán: dự đoán mortality từ symptoms và underlying diseases của bệnh nhân COVID-19.

Nếu dùng ERM trên toàn bộ data, top features có thể là:

- SPO2.
- Renal disease.
- Neurologic disease.
- Diabetes.

Nhưng khi chia thành subpopulations, ta thấy các nhóm có nguyên nhân tử vong khác nhau:

- Một nhóm tập trung nhiều người lớn tuổi; top features chủ yếu là underlying diseases.
- Một nhóm trải rộng qua nhiều độ tuổi; top features là các triệu chứng COVID nghiêm trọng như fever, cough, vomiting/diarrhea.

Điểm quan trọng:

- Người lớn tuổi có thể tử vong nhiều do bệnh nền.
- Người trẻ hơn cũng có thể tử vong nếu triệu chứng COVID đủ nghiêm trọng.
- Nếu chỉ dùng một model trung bình, ta có thể bỏ qua cơ chế thứ hai.

Bài học: phân tích heterogeneity có thể giúp ta hiểu các cơ chế rủi ro khác nhau trong cùng một dataset.

### 3.6. Giới hạn của predictive heterogeneity

Video thừa nhận đây mới là bước đầu. Cần thêm nghiên cứu để:

- Phát hiện subpopulation hiệu quả hơn.
- Scale lên task lớn hơn và model lớn hơn.
- Hiểu vì sao các subpopulation có `Y|X` shifts: do confounders không quan sát được, do data generating processes khác nhau, hoặc do feature bị thiếu.

## 4. 10:00-24:00 - Stage 2: Khai thác heterogeneity trong model training

Sau khi hiểu data có heterogeneity, câu hỏi tiếp theo là: đưa hiểu biết đó vào training như thế nào?

### 4.1. Chất lượng training environments quyết định hiệu quả của invariance

Video quay lại invariant learning/IRM và chỉ ra một vấn đề nền tảng: invariant set phụ thuộc vào environments.

Nếu ta thay ideal environment set `E` bằng training environments `E_tr`, có thể xảy ra:

- Training environments không bao phủ đủ các môi trường có thể xảy ra.
- Support của `E_tr` quá nhỏ.
- Feature học được trông có vẻ invariant trong training environments nhưng không invariant trong môi trường thật.

Nói dễ hiểu: nếu tất cả environments trong train đều có cùng spurious correlation, model không thể biết correlation đó là spurious.

### 4.2. Không có environment labels

Slide "No Training Environments!" nêu một vấn đề rất thực tế:

> Modern datasets are frequently assembled by merging data from multiple sources without explicit source labels.

Nghĩa là:

- Dữ liệu có thể đến từ nhiều nguồn.
- Nhưng sau khi gộp, source label bị mất hoặc không được lưu.
- Kết quả là ta chỉ có một pooled dataset.
- Khi đó IRM/invariance learning không có environment labels rõ ràng để dùng.

Vì vậy, một hướng quan trọng là **học environments từ chính dữ liệu**.

### 4.3. Heterogeneous Risk Minimization

Video giới thiệu một hướng trong nhóm tác giả: **Heterogeneous Risk Minimization**.

Kiến trúc gồm hai module chính:

1. **Heterogeneity identification module**:
   - Tìm hoặc học các environments/subgroups từ pooled data.
   - Dùng unstable/variant features để tách dữ liệu.

2. **Invariant prediction module**:
   - Dùng learned environments để học invariant predictor.
   - Tìm feature ổn định hơn cho prediction.

Hai module hỗ trợ nhau:

- Nếu tách environments tốt hơn, invariant predictor học tốt hơn.
- Nếu invariant predictor tốt hơn, phần variant/unstable còn lại giúp tách environments tốt hơn.

Slide biểu diễn vòng lặp "boosting/converge" giữa hai module.

### 4.4. Ví dụ ColoredMNIST

Slide kết quả trên ColoredMNIST cho thấy:

- Khi hai module tương tác qua nhiều iteration, mức độ heterogeneity/discrepancy giữa learned groups tăng.
- Target accuracy cũng tăng theo.

Điều này cho thấy việc khám phá environments đúng có thể giúp generalization tốt hơn.

### 4.5. Follow-up works

Video liệt kê các hướng mở rộng:

- Recommendation:
  - InvPref.
  - InvRL.
- Graph data:
  - EERM.
  - LECI.
  - GALA.

Thông điệp: ý tưởng học hoặc khai thác heterogeneous environments không chỉ dùng cho ảnh, mà có thể mở rộng sang recommendation, graph learning và các bài toán khác.

### 4.6. DRO và vấn đề noisy samples

Video chuyển sang một giới hạn khác của DRO: over-pessimism và noisy samples.

DRO tập trung vào các sample/group có loss cao. Nhưng loss cao có thể đến từ hai nguồn:

- **Hard samples**: mẫu khó nhưng có ý nghĩa, ví dụ minority group thật.
- **Noisy samples**: mẫu lỗi, label sai, outlier hoặc dữ liệu bị nhiễu.

Nếu DRO không phân biệt hai loại này, nó có thể gán trọng số quá lớn cho noisy samples. Khi đó model học nhiễu thay vì học signal.

Slide minh họa KL-DRO và chi-square DRO đều focus quá nhiều vào noisy samples.

### 4.7. Data geometry matters

Để phân biệt hard samples và noisy samples, video đề xuất dùng thông tin hình học của dữ liệu:

- Dữ liệu high-dimensional thường nằm gần low-dimensional manifolds.
- Noisy samples thường là isolated points.
- Hard samples hoặc minority samples thường có cấu trúc liên tục trong một neighborhood.

Ý tưởng:

- Không chỉ nhìn loss.
- Cần nhìn vị trí của sample trong không gian dữ liệu.
- Sample có loss cao nhưng nằm trong một vùng có cấu trúc có thể là hard/minority sample.
- Sample có loss cao nhưng cô lập có thể là noise.

### 4.8. Geometric Wasserstein Distance

Video giới thiệu Geometric Wasserstein Distance như một cách đưa geometry vào DRO.

Trực giác:

- Density transfer nên diễn ra mượt mà theo data manifold.
- Không nên cho phép distribution worst-case tập trung quá mạnh vào các điểm cô lập.

Slide cũng nhắc đến calibration terms và graph total variation để penalize noisy samples.

### 4.9. DRO tailored for specific shifts

Perspective 4 nói rằng DRO nên được thiết kế theo shift cụ thể, không nên dùng một uncertainty set chung chung.

Ví dụ X-shifts:

- Xét shifts theo age groups: `[20,25), [25,30), ..., [75,100)`.
- Chọn subset covariates có subgroup differences lớn nhất.
- Hiệu năng thay đổi nhiều tùy biến nào được chọn.

Ví dụ `Y|X` shifts:

- Public coverage task từ NE sang LA.
- Xét shifts trên subset covariates và `Y`.
- Biến `Y | income` chịu shift lớn.
- Performance cũng thay đổi theo selected variables.

Bài học: muốn DRO hiệu quả, phải biết shift đang xảy ra trên biến nào và theo dạng nào.

## 5. 25:00-35:00 - Stage 3: Model evaluation và stability

Sau khi train xong model, không đủ để chỉ báo cáo average accuracy. Ta cần biết model thất bại ở đâu và nhạy cảm với shift nào.

### 5.1. Perspective 5: model yếu ở vùng dữ liệu nào?

Slide đặt câu hỏi:

> On what training data does the model perform poorly?

Nếu trả lời được câu hỏi này, ta có thể:

- Thu thập thêm dữ liệu đúng vùng yếu.
- Patch hoặc retrain model.
- Tránh dùng model trên những vùng rủi ro.

Đây là tư duy error slice discovery: tìm các slices/subgroups mà model có lỗi cao.

### 5.2. Perspective 6: beyond accuracy, evaluate stability

Video đặt câu hỏi tiếp:

> What kind of data distribution is the model most sensitive to?

Hai kiểu shift được phân biệt:

1. **Data corruptions**:
   - Thay đổi support hoặc observed data samples.
   - Ví dụ blur, noise, occlusion, perturbation.

2. **Sub-population shifts**:
   - Thay đổi probability density hoặc mass function.
   - Support giữ nguyên nhưng tỷ trọng nhóm thay đổi.

Một model có thể robust với corruption nhưng không robust với subpopulation shift, hoặc ngược lại.

### 5.3. Stability evaluation bằng OT

Slide giới thiệu một tiêu chí stability dựa trên optimal transport:

- Xác định tập distribution mà tại đó risk/performance của model vượt quá một threshold xấu.
- Đo khoảng cách chiếu từ distribution hiện tại đến tập failure đó.
- Khoảng cách càng lớn, model càng stable.

Trực giác:

```text
Model ổn định hơn nếu phải shift dữ liệu rất nhiều mới làm performance rơi xuống dưới ngưỡng.
```

### 5.4. Toy visualization

Slide trực quan hóa most sensitive distribution `Q*`:

- Dữ liệu ban đầu là các cụm điểm hai lớp.
- Khi thay đổi các tham số chi phí/constraint, distribution nhạy cảm nhất khác nhau.
- Kích thước điểm thể hiện sample weight trong `Q*`.

Điều này giúp ta nhìn thấy model sợ loại shift nào.

### 5.5. Một method robust với shift này chưa chắc robust với shift khác

Slide model stability analysis nêu:

- Adversarial training không nhất thiết stable dưới subpopulation shifts.
- Tilted ERM không nhất thiết stable dưới data corruptions.

Bài học: "robust" không phải một khái niệm chung chung. Cần nói rõ robust với loại shift nào.

### 5.6. Feature stability analysis

Video tiếp tục với câu hỏi: perturb feature nào sẽ làm model performance giảm?

Ý nghĩa:

- Giúp chẩn đoán model ở mức feature.
- Biết model đang dựa quá nhiều vào feature nào.
- Phát hiện shortcut hoặc spurious reliance.

Ví dụ COVID mortality:

- Feature "Age" rất quan trọng.
- Accuracy theo age group có thể trông cao.
- Nhưng macro-F1 thấp, nghĩa là model không cân bằng tốt giữa các lớp/nhóm.
- Model có thể đơn giản dựa vào tuổi thay vì học cơ chế bệnh đầy đủ.

Kết luận: average accuracy có thể che giấu vấn đề. Cần metrics và phân tích sâu hơn.

## 6. 36:00-44:00 - Stage 4: Sau deployment, vì sao performance giảm?

Giai đoạn cuối là deployment. Khi model đã chạy ngoài thực tế và performance giảm, ta cần biết nguyên nhân giảm đến từ đâu.

### 6.1. Perspective 7: hiểu shift trước khi chọn can thiệp

Slide nêu nhiều lựa chọn can thiệp:

- Domain adaptation.
- DRO.
- Invariant learning.
- Thu thêm target data.
- Thu thêm features.

Nhưng không có lựa chọn nào luôn đúng. Ta phải hiểu shift trước:

```text
Understand distribution shift to determine next steps.
```

### 6.2. Attribute performance change to distribution shifts

Video chia shift thành hai nhóm lớn:

| Loại shift | Diễn giải |
|---|---|
| X-shifts | Thay đổi sampling, population shifts, minority groups. |
| Y|X-shifts | Thay đổi labeling, mechanism, hoặc chọn thiếu feature quan trọng. |

Trong thực tế, performance drop có thể là kết hợp của cả hai. Không phải shift nào cũng quan trọng như nhau. Vì vậy cần attribution: phần giảm performance nào đến từ X-shift, phần nào đến từ `Y|X`-shift.

### 6.3. Shared distribution

Để phân rã performance change, video giới thiệu ý tưởng shared distribution giữa training distribution `P` và target distribution `Q`.

Slide minh họa bằng biến age:

- `P_X` là density của age trong training.
- `Q_X` là density của age trong target.
- `S_X` là shared distribution, tập trung vào vùng mà cả hai distribution có overlap.

Công thức trực giác trên slide:

```text
s_X(x) proportional to p_X(x) q_X(x) / (p_X(x) + q_X(x))
```

Shared distribution giúp so sánh cơ chế `Y|X` trên cùng một vùng `X`, tránh nhầm lẫn giữa thay đổi input distribution và thay đổi mechanism.

### 6.4. Decompose change in performance

Slide "Decompose change in performance" biểu diễn một lưới so sánh:

- Di chuyển từ training `P` sang shared `S`: phần liên quan đến X-shift.
- So sánh cơ chế dự đoán/loss giữa `P` và `Q` trên shared distribution: phần liên quan đến `Y|X`-shift.
- Di chuyển từ shared `S` sang target `Q`: phần X-shift còn lại.

Mục tiêu là tách tổng performance drop thành các thành phần có ý nghĩa, để biết nên sửa bằng cách nào.

### 6.5. Employment prediction case study

Ví dụ: dự đoán employment, `P = West Virginia`, `Q = Maryland`.

Slide nói:

- Model ở West Virginia không dùng education.
- Nhưng ở Maryland, education ảnh hưởng đến employment.
- Do đó có `Y|X` shift vì thiếu hoặc không dùng đúng covariate.

Bài học: nếu performance giảm do thiếu feature quan trọng, chỉ reweight data có thể không đủ. Cần thu thêm feature hoặc thay đổi representation/modeling.

### 6.6. Identify covariate regions with Y|X-shifts

Video trình bày một workflow:

1. Construct shared distribution từ training và target.
2. Model `Y` riêng trên training và target:

```text
f_p, f_q
```

3. Model sự khác biệt:

```text
f_p(x) - f_q(x)
```

trên shared distribution bằng một interpretable tree-based model.

Mục tiêu: tìm covariate regions có `Y|X` shift mạnh.

Ví dụ income prediction CA -> PR:

- Region có `Y|X` shift gồm các occupations requiring language.
- Lý do: official languages khác nhau giữa California và Puerto Rico.

Bài học: shift không chỉ là thống kê trừu tượng. Nó có thể gắn với một lý do xã hội/ngữ cảnh rất cụ thể.

## 7. 44:00-52:00 - Recap và future directions

### 7.1. Recap

Video tổng kết:

- Heterogeneity rất quan trọng.
- Hai hướng phổ biến hiện nay:
  - Make modeling assumptions: có nguyên lý, nhưng giả định có thể không đúng.
  - Scale up data: hiệu quả với Internet-scale data, nhưng dữ liệu đúng trong nhiều bài toán rất đắt.
- Heterogeneity-aware approach:
  - Phát triển công cụ để hiểu heterogeneity trong từng setting.
  - Dùng hiểu biết đó xuyên suốt toàn bộ modeling process.

### 7.2. Future directions

Slide future directions nêu các hướng mở:

- Cần system-level view cho AI, giống "industrial engineering" cho toàn bộ workflow.
- Thiết kế workflow tốt hơn, không chỉ thiết kế model.
- Phát triển công cụ để mô hình hóa data heterogeneity.
- Xây dựng model biết điều nó không biết.
- Vì ta chỉ quan sát được outcomes/actions mà ta đã đo, cần chủ động quyết định thu thập dữ liệu nào.
- Agent phải biết active data collection để giảm uncertainty.
- Có liên hệ với reinforcement learning và active learning.

Kết luận: đây là một không gian nghiên cứu còn rất nhiều bài toán mở.

## 8. Kết luận của Video 2

Video 2 đưa ra thông điệp rõ hơn Video 1:

```text
OOD generalization không chỉ là chọn một thuật toán robust.
Nó là một quy trình phân tích dữ liệu xuyên suốt pipeline ML.
```

Ta cần:

- Phát hiện subpopulations.
- Hiểu `Y|X` có khác nhau giữa các groups không.
- Học hoặc khám phá environments khi labels không có.
- Phân biệt hard samples và noisy samples.
- Thiết kế DRO/IRM theo shift thật.
- Đánh giá model theo slices, stability và feature sensitivity.
- Sau deployment, phân rã performance drop để chọn can thiệp đúng.

Nói ngắn gọn:

```text
Hiểu heterogeneity trước.
Chọn method sau.
Đánh giá và sửa model theo đúng loại shift.
```

## 9. Các khái niệm quan trọng cần nhớ

| Khái niệm | Ý nghĩa dễ hiểu |
|---|---|
| Predictive heterogeneity | Việc chia dữ liệu thành subgroups làm tăng thông tin dự đoán. |
| Mutual information | Đo lượng thông tin mà X cung cấp để giảm bất định của Y. |
| Heterogeneous subpopulation | Nhóm dữ liệu có cơ chế `Y|X` khác nhóm khác. |
| Learned environments | Environments được học từ dữ liệu khi không có labels sẵn. |
| Heterogeneous Risk Minimization | Vừa học environments, vừa học invariant predictor. |
| Hard sample | Mẫu khó nhưng có ý nghĩa học. |
| Noisy sample | Mẫu lỗi/nhiễu/outlier, không nên được upweight quá mức. |
| Data geometry | Cấu trúc hình học của dữ liệu, giúp phân biệt hard samples và noise. |
| Geometric Wasserstein Distance | Biến thể Wasserstein có xét manifold/geometry để tránh tập trung vào noise. |
| Error slice discovery | Tìm vùng dữ liệu mà model có lỗi cao. |
| Stability evaluation | Đo model nhạy cảm với loại distribution shift nào. |
| Feature stability | Xem perturb feature nào làm performance giảm. |
| Shift attribution | Phân rã performance drop thành X-shift và `Y|X`-shift. |
| Shared distribution | Distribution trung gian giúp so sánh training và target trên vùng overlap. |
| Active data collection | Chủ động thu thập dữ liệu để giảm uncertainty và cải thiện generalization. |

## 10. Liên hệ trực tiếp với project video Manim

Nội dung Video 2 đặc biệt hữu ích cho việc làm rõ chiều sâu học thuật của các scene:

- Scene 4: data heterogeneity không chỉ là nhiều nguồn data, mà còn là subpopulations với `Y|X` khác nhau.
- Scene 5: spurious correlation có thể được hiểu là một dạng signal không ổn định giữa subgroups/environments.
- Scene 6: ERM che giấu lỗi vì nó tối ưu average, không phân tích slices.
- Scene 7: IRM cần environment labels tốt; nếu không có, phải học hoặc khám phá environments.
- Scene 8: DRO có thể bị over-pessimism và học noise; cần thiết kế theo shift cụ thể.
- Scene 9: Stable/causal learning nên được trình bày như một phần của heterogeneity-aware approach.
- Scene 10: future directions nên nhấn mạnh environment discovery, stability, uncertainty, active data collection và label-free methods.

## 11. Cách học video này hiệu quả

Để hiểu Video 2, nên đọc theo thứ tự:

1. Đọc file tổng kết này để nắm toàn bộ logic pipeline.
2. Mở `collas_2024_tutorial_part_2_visual_notes_vi.md` để xem nội dung slide, công thức và ví dụ.
3. Mở `collas_2024_tutorial_part_2_transcript.md` khi cần đối chiếu lời nói theo timestamp.
4. Khi đưa vào kịch bản Manim, nên ưu tiên phần trực quan:
   - Pipeline 4 stages.
   - Predictive heterogeneity.
   - Hard samples vs noisy samples.
   - Stability beyond accuracy.
   - X-shift vs `Y|X`-shift attribution.
