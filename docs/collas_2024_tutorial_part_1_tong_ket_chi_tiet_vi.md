# Tổng kết chi tiết Video 1 - Data Heterogeneity Analysis for Distribution Shifts

Nguồn video: https://www.youtube.com/watch?v=_kJtrMFfSJc

Tài liệu nền đã dùng trong workspace:

- Transcript lời nói: `collas_2024_tutorial_part_1_transcript.md`
- Ghi chú học tập: `collas_2024_tutorial_part_1_study_notes_vi.md`
- Ghi chú hình ảnh/slide: `collas_2024_tutorial_part_1_visual_notes_vi.md`
- Contact sheets: `contact_sheets/part_1_sheet_01.jpg` đến `contact_sheets/part_1_sheet_06.jpg`

> Lưu ý: transcript gốc lấy từ phụ đề tự động của YouTube nên có lỗi nhận dạng. Trong bản tổng kết này, các thuật ngữ đã được chuẩn hóa theo nội dung slide và bối cảnh học thuật: `hyrogen/hydrogen` được hiểu là `heterogeneity`, `ships` là `shifts`, `DR/DRL` là `DRO`, `inance` là `invariance`, `click` là `CLIP`.

## 1. Mục tiêu chính của video

Video 1 đặt nền tảng cho toàn bộ tutorial. Nội dung không đi thẳng vào thuật toán, mà bắt đầu từ câu hỏi thực tế: vì sao một mô hình AI có thể hoạt động tốt trong phòng thí nghiệm nhưng lại thất bại khi triển khai ngoài đời?

Thông điệp trung tâm là: nhiều thất bại của AI không chỉ đến từ việc model yếu, thiếu dữ liệu, hay code sai. Chúng thường đến từ việc dữ liệu thực tế không đồng nhất, không i.i.d., và phân phối dữ liệu khi triển khai khác với phân phối dữ liệu khi huấn luyện. Nói cách khác, ta phải nhìn vấn đề từ góc độ dữ liệu: **data heterogeneity** và **distribution shift**.

Video này có ba nhiệm vụ lớn:

1. Giới thiệu các rủi ro thực tế của AI dưới distribution shift.
2. Review ba hướng tiếp cận phổ biến: DRO, invariant learning/IRM, và pretrained big models như CLIP.
3. Chỉ ra rằng các hướng này đều có giới hạn nếu ta không hiểu dữ liệu và không kiểm tra giả định của chúng trong từng ứng dụng cụ thể.

## 2. 00:00-08:00 - Từ thất bại AI đến data heterogeneity

Phần mở đầu dùng nhiều ví dụ trực quan để chứng minh rằng AI có thể sai trong những tình huống tưởng như đơn giản:

- Robot hút bụi bị kẹt trong một cấu trúc giống lưới.
- Camera AI trong trận bóng đá theo nhầm đầu trọc của trọng tài thay vì theo bóng hoặc cầu thủ.
- Hệ thống y tế trong giai đoạn COVID có thể học nhầm tín hiệu liên quan đến bệnh viện hoặc quy trình thu thập dữ liệu, thay vì học đúng dấu hiệu bệnh.
- Xe tự lái hoặc hệ thống hỗ trợ lái có thể phanh sai vì hiểu nhầm vật thể hoặc ngữ cảnh phía trước.

Những ví dụ này dẫn đến vấn đề cốt lõi: trước khi triển khai AI trong thế giới thực, ta phải hỏi liệu hệ thống có **generalize** tốt trong những tình huống khác với dữ liệu huấn luyện hay không.

### 2.1. Vấn đề không chỉ nằm ở model

Slide "From a DATA Perspective" nhấn mạnh rằng các vấn đề của model dưới distribution shift gồm:

- Generalization kém khi gặp dữ liệu mới.
- Không công bằng với nhóm thiểu số hoặc nhóm ít xuất hiện.
- Nhạy cảm với nhiễu, corruption, hoặc thay đổi bối cảnh.

Tutorial lập luận rằng nhiều "model problems" thực chất có gốc từ "data problems":

- Dữ liệu có nhiều nguồn khác nhau.
- Có các subpopulation ẩn.
- Có nhóm khó, mẫu nhiễu, mẫu hiếm.
- Có sự khác biệt giữa training distribution và target/deployment distribution.

### 2.2. Data heterogeneity là gì?

Trong video, data heterogeneity được hiểu là bản chất phức tạp và không đồng nhất của dữ liệu. Dữ liệu hiện đại thường không đến từ một nguồn duy nhất, mà là kết quả của việc gộp nhiều nguồn:

- Nhiều môi trường thu thập dữ liệu khác nhau.
- Nhiều nhóm người dùng, nhóm bệnh nhân, nhóm địa lý.
- Nhiều cơ chế sinh dữ liệu khác nhau.
- Nhiều kích thước mẫu khác nhau giữa các nhóm.
- Nhiều dạng dữ liệu khác nhau: ảnh, bảng, văn bản, cảm biến.

Slide minh họa cho thấy nhiều nguồn dữ liệu được gộp vào một tập training data. Sau khi gộp, ta thường train model như thể đây là một khối đồng nhất. Nhưng thực ra bên trong có thể tồn tại:

- Multiple environments.
- Different `Y|X` distributions.
- Different data sizes.

Đây là điểm rất quan trọng: heterogeneity không nhất thiết là "nhiễu" cần loại bỏ. Nó có thể là **thông tin ẩn** giúp ta hiểu vì sao model thất bại và nên sửa model/dữ liệu theo hướng nào.

### 2.3. X-shifts và Y|X-shifts

Video phân biệt hai kiểu shift lớn:

- **X-shift**: phân phối input `X` thay đổi. Ví dụ ảnh ban ngày sang ban đêm, người dùng trẻ sang người dùng già, vùng địa lý này sang vùng địa lý khác.
- **Y|X-shift**: cơ chế gán nhãn hoặc quan hệ dự đoán giữa `X` và `Y` thay đổi. Đây là loại shift khó hơn vì cùng một input hoặc cùng một nhóm feature có thể dẫn đến label khác trong môi trường khác.

Slide nhấn mạnh:

- Con người có thể robust với nhiều thay đổi phân phối.
- Machine learning truyền thống thường tập trung vào covariate shift, tức X-shift.
- Causal inference quan tâm nhiều hơn đến `Y|X` shift vì nó liên quan đến cơ chế sinh nhãn và các yếu tố không quan sát được.
- Nếu `Y|X` thay đổi mạnh, ta không nên mặc định rằng một single model có thể hoạt động tốt cho mọi distribution.

### 2.4. Cần một cách nhìn hệ thống

Tutorial không chỉ xem data heterogeneity như một vấn đề trong training. Nó đề xuất nhìn toàn bộ pipeline ML:

```text
Data collection -> Model training -> Model evaluation -> Deployment
```

Mỗi giai đoạn đều có thể hưởng lợi nếu ta hiểu dữ liệu heterogeneous như thế nào.

## 3. 09:00-19:00 - Distributionally Robust Optimization (DRO)

DRO là hướng tiếp cận đầu tiên được review.

### 3.1. Từ ERM sang DRO

ERM huấn luyện model bằng cách tối thiểu hóa loss trung bình trên training data:

```text
min_theta E_{Z ~ P_train}[ell(theta; Z)]
```

DRO thay đổi mục tiêu: thay vì tối ưu trên phân phối training duy nhất, ta xét một tập các phân phối có thể xảy ra xung quanh training distribution, rồi tối ưu trên phân phối xấu nhất:

```text
min_theta sup_{Q in P} E_{Z ~ Q}[ell(theta; Z)]
```

Trong đó `P` là uncertainty set, tức tập các phân phối mà ta quan tâm.

Trực giác: nếu model vẫn tốt trong trường hợp xấu nhất, nó có thể robust hơn khi gặp shift thật.

### 3.2. Vấn đề then chốt: chọn uncertainty set

DRO phụ thuộc rất mạnh vào cách định nghĩa tập phân phối `P`:

```text
P = {Q : Dist(Q, P_train) <= rho}
```

Tức là ta chọn một metric `Dist` để đo khoảng cách giữa distribution `Q` và training distribution `P_train`. Video trình bày hai metric quan trọng.

### 3.3. f-divergence

f-divergence so sánh hai phân phối thông qua density ratio:

```text
dQ / dP
```

Nếu density ratio gần 1, hai distribution gần nhau. Nếu ratio lệch xa 1, chúng khác nhau nhiều hơn. Slide dùng một hàm convex `f` với `f(1)=0`.

Trực giác của f-divergence là **reweight data**:

- Training data có thể gồm 70% người già, 30% người trẻ.
- Một distribution khác trong uncertainty set có thể thay đổi tỷ lệ hai nhóm này.
- Nó chủ yếu thay đổi trọng số các sample đã có, thay vì tạo sample mới.

### 3.4. Wasserstein distance

Wasserstein distance còn được gọi là optimal transport distance hoặc earth mover's distance. Nó đo chi phí tối thiểu để "vận chuyển" khối lượng xác suất từ distribution này sang distribution khác.

Khác với f-divergence, Wasserstein distance quan tâm đến **geometry của dữ liệu**:

- Không chỉ hỏi density khác nhau bao nhiêu.
- Mà còn hỏi cần di chuyển mass bao xa để biến phân phối này thành phân phối kia.

Slide minh họa bằng hai phân phối `Q` và `P`, cùng chi phí tối thiểu để transport `Q` sang `P`.

Trong ví dụ age distribution:

- f-divergence có xu hướng reweight nhóm tuổi đã có.
- Wasserstein có thể mô phỏng việc perturb tuổi của một số điểm, ví dụ từ 60 xuống 45.

### 3.5. Nhiều biến thể DRO

Video liệt kê nhiều biến thể DRO:

- Marginal DRO.
- Sinkhorn DRO.
- Geometric DRO.
- MMD DRO.
- Holistic DRO.
- Unified OT DRO.

Thông điệp ở đây không phải là nhớ hết mọi method, mà là hiểu rằng mỗi biến thể tương ứng với một cách giả định khác nhau về shift. Nếu metric hoặc uncertainty set không khớp với shift thật, DRO có thể không giúp ích.

### 3.6. Giới hạn của DRO

Slide "DRO makes a strong assumption" tóm tắt logic của DRO:

```text
Carefully choose the set P
        ->
Do well on real distribution shifts
```

Giả định ngầm là: worst-case distribution trong `P` phải đại diện được cho shift thật.

Video đặt câu hỏi: giả định này có đúng trong thực tế không?

Kết quả thực nghiệm được trình bày cho thấy: trên nhiều tabular datasets và nhiều shift patterns, các DRO methods không cho cải thiện đáng kể so với ERM hoặc baseline đơn giản như logistic regression/SVM.

Hai lý do chính:

1. **Over-pessimism**: worst-case distribution quá bảo thủ, quá khó học. Model bị ép tối ưu cho một phân phối cực đoan không giống dữ liệu thật.
2. **Mismatch with target domains**: worst-case distribution được tạo ra bởi DRO không align với các target domains thực tế.

Kết luận: DRO là một ý tưởng mạnh, nhưng chỉ hiệu quả nếu uncertainty set phản ánh đúng loại distribution shift trong ứng dụng.

## 4. 20:00-27:00 - Invariant Learning và IRM

Hướng tiếp cận thứ hai là invariant learning.

### 4.1. Problem setting

Slide minh họa bài toán domain generalization:

- Train: nhiều domains, ví dụ art, cartoon, photo.
- Test: domain mới, ví dụ sketch.

Ký hiệu:

```text
Train: P^1_{X,Y}, P^2_{X,Y}, ..., P^K_{X,Y}
Test: Q_{X,Y}
```

So với DRO, invariant learning có thêm thông tin: nhiều training domains/environments. Ý tưởng là dùng sự khác biệt giữa các environments để tìm ra cơ chế nào ổn định.

### 4.2. Trực giác của invariant learning

Invariant learning giả định rằng có một cơ chế thật sự ổn định qua nhiều môi trường. Nếu ta tìm được cơ chế đó, model sẽ generalize tốt hơn sang environment mới.

Ví dụ:

- Background của ảnh có thể thay đổi giữa environments.
- Nhưng hình dạng con vật vẫn là feature ổn định để phân biệt cow/camel.

Slide cow/camel nhấn mạnh: hãy dùng đặc trưng của con vật `Phi(X)` để dự đoán, không dùng background.

### 4.3. Invariant Causal Prediction

Slide về invariant causal prediction đưa ra ý tưởng:

> Tìm tập con các covariates `X` có quan hệ invariant với `Y` qua các environments.

Ví dụ causal graph về việc đi học muộn:

- Traffic accident, heavy rain, getting up late, traffic jam, long queues.
- Một số biến có quan hệ ổn định hơn với outcome "late for school".

Điểm chính: nếu một feature có quan hệ nhân quả thật với label, quan hệ đó nên ổn định hơn khi môi trường thay đổi.

### 4.4. IRM - Invariant Risk Minimization

IRM formalize ý tưởng trên. Mục tiêu là học representation `Phi(X)` sao cho cùng một classifier `w` là tối ưu trên mọi environment.

Công thức ý tưởng:

```text
min_{Phi,w} sum_{e in E_tr} R^e(w o Phi)
subject to w in argmin_{w_tilde} R^e(w_tilde o Phi), for all e in E_tr
```

Trong thực tế, ràng buộc này khó tối ưu trực tiếp. IRMv1 dùng penalty xấp xỉ:

```text
min_Phi sum_{e in E_tr} R^e(Phi)
       + lambda * ||grad_{w|w=1.0} R^e(w o Phi)||^2
```

Ý nghĩa:

- Nếu representation thật sự invariant, classifier tối ưu sẽ gần như giống nhau ở các environments.
- Gradient penalty giúp ép điều này xảy ra.

### 4.5. Invariance assumption

Slide "Invariance Assumption" nêu hai tính chất:

1. **Invariance property**: quan hệ giữa `Phi*(X)` và `Y` giữ nguyên qua environments.
2. **Sufficiency property**: `Phi*(X)` chứa đủ thông tin cần thiết để dự đoán `Y`.

Nếu cả hai đúng, `Phi*(X)` có thể được xem là causally invariant predictor.

### 4.6. Maximal Invariant Predictor

Video cũng nhắc đến maximal invariant predictor, tức tìm predictor invariant nhưng vẫn giữ nhiều thông tin dự đoán nhất có thể. Trực giác:

- Không chỉ invariant là đủ.
- Predictor còn phải có thông tin mạnh để dự đoán `Y`.
- Vì vậy có sự kết hợp giữa invariance và mutual information.

### 4.7. Giới hạn của invariant learning

Slide so sánh assumptions:

- DRO cần predefined set of distributions gần training distribution.
- Invariant learning cần predefined set of environments.

Vấn đề là các giả định này không tự động đúng:

- Environment labels có thể không có.
- Environment labels có thể không phản ánh đúng cơ chế shift.
- Nếu training environments không đủ đa dạng, model không thể nhận ra feature nào thật sự invariant.
- Nếu mọi environment giống nhau, không có tín hiệu để tách causal và spurious features.

Kết luận: invariant learning chỉ có ý nghĩa khi environments đủ tốt và giả định invariance phù hợp với dữ liệu.

## 5. 28:00-35:00 - Pretrained Big Models và CLIP

Hướng tiếp cận thứ ba không bắt đầu từ một giả định phân phối cụ thể, mà scale up model và data.

### 5.1. CLIP học từ image-caption

CLIP được dùng làm ví dụ đại diện. Nó học quan hệ giữa ảnh và caption bằng contrastive learning:

- Image encoder biến ảnh thành vector.
- Text encoder biến caption/text label thành vector.
- Model học để ảnh và text tương ứng nằm gần nhau trong embedding space.

Nhờ vậy CLIP có thể làm zero-shot prediction: tạo classifier từ label text thay vì phải train classifier supervised truyền thống.

### 5.2. Vì sao CLIP có lợi thế?

Slide so sánh:

Supervised ImageNet:

- Khoảng 1 triệu cặp image-label.
- Dữ liệu từ một nguồn tương đối hẹp.
- Cần người gán nhãn.

CLIP:

- Khoảng 400 triệu cặp image-caption.
- Dữ liệu từ Internet, đa dạng hơn.
- Không cần gán nhãn thủ công kiểu ImageNet vì image-caption đã tồn tại tự nhiên.

Thông điệp: một phần lớn gains của CLIP đến từ dữ liệu.

### 5.3. Nhưng thêm dữ liệu không đồng nghĩa robust hơn

Slide "Just adding more data != better" nhấn mạnh rằng số lượng dữ liệu không đảm bảo robustness. Chất lượng, độ bao phủ, và sự phù hợp của training distribution quan trọng hơn số lượng đơn thuần.

Điểm này đặc biệt quan trọng với các ứng dụng như:

- Y tế.
- Lái xe tự động.
- Thí nghiệm khoa học.
- Chính sách công.
- Can thiệp kinh tế/xã hội.

Trong các lĩnh vực này, dữ liệu đúng thường đắt và khó thu thập. Không thể chỉ nói "thu thêm thật nhiều data". Ta phải biết **cần thu thêm loại data nào**.

## 6. 36:00-46:00 - Chuyển sang tư duy inductive/data-centric

Sau khi review ba hướng tiếp cận, video kết luận rằng cả ba đều có giới hạn nếu ta không hiểu dữ liệu.

### 6.1. Đừng chỉ làm hai việc quen thuộc

Slide "Can we do better?" đối chiếu hai cách làm:

Không nên chỉ:

- Make modeling assumptions.
- Scale up data and models.

Nên:

- Hiểu ứng dụng và dữ liệu trước, rồi mới đặt giả định modeling phù hợp.
- Hiểu cần dữ liệu ở đâu, nhất là khi dữ liệu đắt.

### 6.2. Takeaways

Các ý rút ra:

- Nhiều method hiện tại như DRO và invariant learning không luôn tạo ra gains lớn trong thực nghiệm.
- Chúng dựa vào giả định về quan hệ giữa các distributions nhưng thường không kiểm tra kỹ giả định đó.
- Ta cần mô hình hóa distribution shifts thật trong từng ứng dụng, không chỉ dùng shift giả định.
- Với pretrained models, cần hiểu training data distribution, không chỉ scale model/data.
- Mỗi ứng dụng cần phân tích shift pattern riêng.

### 6.3. Inductive vs. deductive

Slide "Inductive vs. Deductive" phân biệt:

- Deductive: bắt đầu từ giả thuyết lý tưởng, sau đó suy ra phương pháp.
- Inductive: bắt đầu từ quan sát thực tế, dữ liệu thực tế, rồi xây dựng giả định/mô hình phù hợp.

Tutorial cho rằng lĩnh vực distribution shift còn thiếu:

- Một modeling language đủ tốt để mô tả shift thật.
- Empirical foundations đủ mạnh để kiểm tra giả định.

### 6.4. Motivated example: income prediction CA -> PR

Video đưa ví dụ income prediction với source là California và target là Puerto Rico.

Slide cho thấy:

- Performance drop khi chuyển domain.
- Sự khác biệt có thể đến từ `X-shift` hoặc `Y|X-shift`.
- Một số covariate regions liên quan đến work hours, education, occupation, risk region.

Điểm quan trọng: source accuracy và target accuracy chỉ tương quan tốt khi X-shifts chiếm ưu thế. Khi `Y|X` shifts mạnh, hiện tượng "accuracy-on-the-line" không còn đáng tin cậy.

### 6.5. Inductive approach to ambiguity sets

Video đề xuất thay vì chọn ambiguity set một cách trừu tượng, ta có thể thiết kế nó dựa trên dữ liệu và ứng dụng:

- Xét shifts theo nhóm tuổi.
- Chọn subset covariates có subgroup differences lớn.
- Dùng variable selection để xác định ambiguity set.

Slide cho thấy performance thay đổi rất nhiều tùy biến nào được chọn. Điều này củng cố luận điểm: chọn đúng nguồn heterogeneity là cực kỳ quan trọng.

## 7. Kết luận của Video 1

Video 1 kết luận rằng:

- Data heterogeneity là yếu tố trung tâm khi nói về distribution shift.
- DRO, IRM/invariant learning và pretrained big models đều hữu ích, nhưng đều dựa vào giả định.
- Các giả định này phải được kiểm tra bằng dữ liệu thật.
- Không nên áp dụng method một cách máy móc.
- Cần chuyển sang cách tiếp cận data-centric/inductive: hiểu dữ liệu, hiểu shift pattern, rồi mới chọn hoặc thiết kế method.

Nói ngắn gọn:

```text
Không phải cứ model mạnh hơn là generalize tốt hơn.
Không phải cứ nhiều data hơn là robust hơn.
Không phải cứ dùng DRO/IRM là chống shift tốt hơn.

Điểm bắt đầu đúng là: phân tích data heterogeneity.
```

## 8. Các khái niệm quan trọng cần nhớ

| Khái niệm | Ý nghĩa dễ hiểu |
|---|---|
| IID assumption | Train và test đến từ cùng một phân phối. |
| OOD generalization | Model vẫn hoạt động tốt khi test/deployment distribution khác training distribution. |
| Data heterogeneity | Dữ liệu không đồng nhất, gồm nhiều nguồn, nhóm, môi trường, cơ chế sinh dữ liệu. |
| X-shift | Phân phối input thay đổi. |
| Y|X-shift | Cơ chế dự đoán/quan hệ giữa input và label thay đổi. |
| ERM | Tối ưu loss trung bình trên training data. |
| DRO | Tối ưu loss trong worst-case distribution thuộc một uncertainty set. |
| f-divergence | Đo khác biệt distribution qua density ratio. |
| Wasserstein distance | Đo chi phí vận chuyển mass giữa distributions, có xét geometry. |
| Invariant learning | Tìm cơ chế/feature ổn định qua environments. |
| IRM | Học representation sao cho cùng một classifier tối ưu ở mọi environment. |
| CLIP | Pretrained model học từ image-caption pairs ở quy mô lớn. |
| Inductive approach | Bắt đầu từ dữ liệu và hiện tượng thực tế để xây dựng giả định phù hợp. |

## 9. Liên hệ trực tiếp với project video Manim

Nội dung Video 1 hỗ trợ trực tiếp cho các scene trong project:

- Scene 1: dùng failure cases để mở đầu câu hỏi "vì sao AI fail ngoài thực tế?"
- Scene 2: giải thích i.i.d. assumption.
- Scene 3: giới thiệu distribution shift, đặc biệt X-shift và Y|X-shift.
- Scene 4: trình bày data heterogeneity là thông tin ẩn.
- Scene 5: dẫn sang spurious correlation.
- Scene 6: giải thích vì sao ERM không đủ.
- Scene 7: dùng IRM/invariant learning để minh họa hướng invariance.
- Scene 8: dùng DRO để minh họa hướng robustness.
- Scene 10: kết luận rằng cần data-centric và heterogeneity-aware ML.

## 10. Cách học video này hiệu quả

Để hiểu Video 1, nên đọc theo thứ tự:

1. Đọc file tổng kết này để nắm flow.
2. Mở `collas_2024_tutorial_part_1_visual_notes_vi.md` để xem chi tiết các slide.
3. Mở `collas_2024_tutorial_part_1_transcript.md` khi cần đối chiếu lời nói theo timestamp.
4. Với công thức IRM/DRO, đối chiếu thêm `docs/04_research_report.md` vì transcript tự động có thể nhận dạng sai ký hiệu.
