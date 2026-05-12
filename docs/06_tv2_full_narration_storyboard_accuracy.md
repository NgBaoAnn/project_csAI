# TV2 Full Narration, Storyboard, and Accuracy Review

Tài liệu này là deliverable hoàn chỉnh cho vai trò **TV2 - Content Lead**:

- Viết narration script chi tiết cho toàn bộ 10 scene.
- Vẽ storyboard sơ bộ cho tất cả scenes.
- Kiểm tra tính chính xác nội dung so với tutorial gốc.


Lưu ý về transcript: phụ đề tự động có lỗi nhận dạng thuật ngữ. Khi có mâu thuẫn, dùng visual notes, study notes, và `docs/04_research_report.md` để chuẩn hóa thuật ngữ như `heterogeneity`, `distribution shift`, `DRO`, `invariance`, `IRM`, `CLIP`.

## 1. Đánh Giá Vai Trò TV2

 TV2 có đủ ba deliverable chính:

| Nhiệm vụ TV2 | File đáp ứng | Trạng thái |
|---|---|---|
| Narration script hoàn chỉnh toàn video | File này, mục 3 | Đủ chi tiết để thu voiceover nháp |
| Storyboard sơ bộ toàn scenes | File này, mục 4 | Đủ để animator chia shot và code scene |
| Accuracy review với tutorial gốc | File này, mục 5 | Có mapping theo transcript/visual notes |

## 2. Narrative Principle

Video không nên kể theo kiểu "đây là danh sách method chống OOD". Tutorial gốc nhấn mạnh một thông điệp tinh tế hơn:

```text
OOD generalization không bắt đầu bằng việc chọn IRM hay DRO.
Nó bắt đầu bằng việc hiểu data heterogeneity trong ứng dụng cụ thể.
```

Mạch đúng:

```text
AI failures
-> i.i.d. assumption breaks
-> distribution shifts happen
-> shifts come from data heterogeneity
-> pooled data hides subpopulations and Y|X changes
-> model learns spurious correlations
-> ERM optimizes average and hides group failures
-> IRM, DRO, Stable Learning are possible responses
-> but every method has assumptions
-> heterogeneity-aware ML = analyze, train, evaluate, deploy with data understanding
```

## 3. Full Narration Script

Các đoạn dưới đây là narration nháp đầy đủ. Khi thu âm, có thể rút 10-15% chữ để khớp timing, nhưng không nên bỏ các insight chính.

### Scene 1 - Intro: Cái Bẫy Của Sự Thành Công

**Duration target:** ~1.5 phút  
**Mystery:** 99% accuracy nhưng tại sao vẫn sai ngoài đời?

**Narration:**

> "Một hệ thống AI có thể trông rất thông minh trong phòng thí nghiệm. Nó đạt accuracy cao, vượt benchmark, và có vẻ sẵn sàng để triển khai. Nhưng khi đi ra thế giới thật, mọi thứ thay đổi."

> "Một robot hút bụi có thể bị kẹt trong một cấu trúc lạ. Một camera AI trong trận bóng đá có thể theo nhầm đầu trọng tài thay vì theo bóng. Một hệ thống y tế trong COVID có thể học tín hiệu từ bệnh viện hoặc quy trình thu thập dữ liệu, thay vì học đúng dấu hiệu bệnh. Một xe tự lái có thể hiểu nhầm vật thể trước mặt."

> "Những lỗi này không nhất thiết xảy ra vì model yếu, code sai, hay thiếu dữ liệu. Chúng thường xảy ra vì training data và thế giới thật không giống nhau."

> "Video này nói về một câu hỏi nền tảng: khi dữ liệu thực tế không đồng nhất, không i.i.d., và luôn thay đổi, làm sao ta xây dựng AI vẫn đáng tin cậy?"

**Closing insight:**

> "Câu trả lời bắt đầu từ một giả định mà ML truyền thống thường đặt ở nền móng: i.i.d."

### Scene 2 - i.i.d.: Giả Định Mà Chúng Ta Quên Kiểm Tra

**Duration target:** ~2.0 phút  
**Mystery:** Tại sao model tốt trong lab lại fail ngoài thực tế?

**Narration:**

> "Trong machine learning truyền thống, ta thường giả định training data và test data được lấy từ cùng một phân phối. Nói ngắn gọn: dữ liệu trong lab và dữ liệu ngoài đời trông giống nhau về mặt xác suất."

> "Đó là giả định i.i.d.: independent and identically distributed. Independent nghĩa là các sample không phụ thuộc trực tiếp vào nhau. Identically distributed nghĩa là chúng đến từ cùng một distribution."

> "Khi giả định này đúng, loss trên training set là một chỉ báo hợp lý cho performance ngoài thực tế. Ta train bằng gradient descent, giảm loss, và hy vọng model generalize."

> "Nhưng nếu test distribution dịch đi thì sao? Nếu ảnh deployment đến từ camera khác, bệnh nhân đến từ vùng khác, người dùng thuộc nhóm khác, hoặc cách gán nhãn đã thay đổi thì sao?"

> "Lúc đó, training accuracy cao không còn đảm bảo model sẽ hoạt động tốt. Điều bị vỡ không phải chỉ là một con số accuracy. Điều bị vỡ là giả định rằng train và test đến từ cùng một thế giới."

**Definition:**

> "i.i.d. là điều kiện lý tưởng: `P_train(X,Y) = P_test(X,Y)`. OOD bắt đầu khi điều kiện này không còn đúng."

### Scene 3 - Distribution Shift: Ba Kiểu Thay Đổi

**Duration target:** ~2.5 phút  
**Mystery:** "Distribution thay đổi" cụ thể là thay đổi cái gì?

**Narration:**

> "Distribution shift nghe như một khái niệm đơn giản: train distribution khác test distribution. Nhưng trong tutorial, điểm quan trọng là phải hỏi shift xảy ra ở đâu."

> "Trường hợp quen thuộc nhất là `X-shift`: phân phối input thay đổi. Ví dụ ảnh ban ngày chuyển sang ban đêm, người dùng trẻ chuyển sang người dùng lớn tuổi, hoặc dữ liệu từ California chuyển sang Puerto Rico. Input khác đi, nhưng ta vẫn hy vọng quan hệ giữa input và label giữ nguyên."

> "Một dạng khác là label shift: tỷ lệ nhãn thay đổi. Ví dụ trong một bệnh viện, bệnh hiếm chỉ chiếm 5%, nhưng ở một trung tâm chuyên khoa, nó chiếm 40%."

> "Khó nhất là `Y|X-shift`: quan hệ giữa feature và label thay đổi. Cùng một triệu chứng có thể mang ý nghĩa khác ở hai nhóm bệnh nhân. Cùng một occupation có thể liên quan khác đến income ở hai vùng có ngôn ngữ và thị trường lao động khác nhau."

> "Tutorial nhấn mạnh rằng ML truyền thống thường tập trung vào `X-shift`, còn causal inference và heterogeneity analysis quan tâm nhiều đến `Y|X-shift`, vì đó là lúc một model chung có thể không còn phù hợp."

**Definition:**

> "Distribution shift không phải một loại lỗi duy nhất. Nó có thể là shift trong `X`, shift trong `Y`, hoặc shift trong cơ chế `Y|X`."

**Transition:**

> "Vậy vì sao những shift này xuất hiện? Vì dữ liệu thực tế không phải một khối đồng nhất."

### Scene 4 - Data Heterogeneity: Thông Tin Bị Ẩn

**Duration target:** ~2.7 phút  
**Mystery:** Tại sao trộn tất cả dữ liệu lại có thể làm ta hiểu ít hơn?

**Narration:**

> "Dữ liệu hiện đại thường được tạo ra bằng cách gộp nhiều nguồn. Một dataset y tế có thể đến từ nhiều bệnh viện. Một dataset người dùng có thể đến từ nhiều vùng địa lý. Một dataset ảnh có thể đến từ nhiều camera, nhiều bối cảnh, nhiều cách gán nhãn."

> "Khi nhìn từ xa, ta thấy một tập training data duy nhất. Nhưng tutorial gọi đây là data heterogeneity: bên trong tập dữ liệu có nhiều subpopulations, nhiều environments, nhiều data generating processes, nhiều hard samples và noisy samples."

> "Nếu ta gộp tất cả thành một đám điểm màu xám rồi train như thể chúng đến từ cùng một distribution, ta đã làm mất thông tin về nguồn gốc của từng điểm."

> "Quan trọng hơn, heterogeneity không chỉ là các cụm `X` khác nhau. Có những trường hợp hai nhóm có cùng vùng feature, nhưng quan hệ `Y|X` khác nhau. Trong y tế, cùng một triệu chứng có thể có ý nghĩa khác giữa người trẻ và người lớn tuổi. Trong nông nghiệp, cùng một đặc điểm khí hậu có thể ảnh hưởng khác nhau tùy loại cây trồng."

> "Part 2 của tutorial gọi đây là câu hỏi trước khi training: data có chứa heterogeneous subpopulations với different `Y|X` hay không? Nếu có, ép một invariant predictor chung cho tất cả có thể làm mất thông tin quan trọng."

> "Vì vậy, heterogeneity không phải thứ nên xóa đi quá sớm. Nó là thông tin bị ẩn: thông tin về nhóm nào khó, cơ chế nào khác, và thay đổi nào có thể làm model thất bại."

**Definition:**

> "Data heterogeneity là việc dữ liệu được sinh ra từ nhiều nguồn, nhóm, môi trường hoặc cơ chế khác nhau. Trong OOD generalization, sự khác biệt đó là manh mối."

**Transition:**

> "Nhưng nếu model không nhìn thấy các môi trường này, nó sẽ bám vào signal dễ nhất trong dữ liệu gộp. Và signal dễ nhất có thể là signal sai."

### Scene 5 - Spurious Correlations: Cái Bẫy Của Model

**Duration target:** ~2.7 phút  
**Mystery:** Model đạt accuracy cao, nhưng nó đang học cái gì?

**Narration:**

> "Hãy tưởng tượng ta train một classifier phân biệt bò và lạc đà. Trong training data, phần lớn ảnh bò nằm trên cỏ xanh. Phần lớn ảnh lạc đà nằm trên sa mạc. Model đạt 98% accuracy."

> "Nhưng bây giờ ta hỏi câu quan trọng hơn: model đang nhìn hình dạng con vật, hay đang nhìn background?"

> "Nếu cỏ xanh xuất hiện cùng nhãn bò trong hầu hết training cases, thì `grass -> cow` là một shortcut rất rẻ để giảm loss. Model không tự biết đây là shortcut. Nó chỉ thấy rằng shortcut này dự đoán đúng trên nhiều sample."

> "Vấn đề xuất hiện khi environment đổi. Một con bò trên bãi biển, hoặc một con lạc đà trên cỏ, phá vỡ shortcut đó. Lúc này high training accuracy biến thành OOD failure."

> "Đây là spurious correlation: một pattern có ích trong training distribution, nhưng không ổn định qua environments và không phản ánh quan hệ nhân quả bền vững với label."

> "Điểm quan trọng là heterogeneity có thể giúp phát hiện shortcut. Nếu ở environment này bò đi với cỏ, environment khác bò đi với tuyết, environment khác nữa background bị đảo ngược, thì background không còn là signal ổn định. Shape của con vật mới là feature đáng tin hơn."

**Definition:**

> "Spurious correlation là correlation dự đoán đúng trong training environments, nhưng không ổn định khi environment thay đổi."

**Transition:**

> "Nếu shortcut đó giảm loss, thuật toán chuẩn có lý do gì để bỏ qua nó? Để trả lời, ta nhìn vào ERM."

### Scene 6 - ERM: Tại Sao Baseline Không Đủ

**Duration target:** ~2.6 phút  
**Mystery:** ERM làm điều hợp lý là giảm loss, vậy vì sao vẫn fail?

**Narration:**

> "ERM, Empirical Risk Minimization, là nền tảng của rất nhiều thuật toán học máy. Ý tưởng rất hợp lý: chọn model làm cho loss trung bình trên training data nhỏ nhất."

> "Công thức nhìn rất sạch: lấy loss của từng sample, cộng lại, chia trung bình, rồi tối ưu. Nhưng chính chữ trung bình tạo ra điểm mù."

> "Nếu 85% dữ liệu thuộc majority group, group này sẽ kéo objective mạnh nhất. Model có thể làm rất tốt trên majority group, đạt average accuracy rất đẹp, nhưng vẫn thất bại nặng trên minority group."

> "Trong ví dụ bò và lạc đà, nếu majority data ủng hộ shortcut `grass -> cow`, shortcut đó giúp giảm loss nhanh. ERM không phân biệt correlation nào là causal, correlation nào là spurious. Nó dùng bất kỳ signal nào làm objective giảm."

> "Vì vậy, vấn đề không phải ERM bị lỗi. ERM đang làm đúng điều ta yêu cầu: tối ưu performance trung bình trên training distribution. Vấn đề là khi dữ liệu heterogeneous, trung bình đó có thể che giấu đúng phần quan trọng nhất: worst group, rare subpopulation, và failure khi deployment."

> "Tutorial Part 2 nhấn mạnh điều này trong model evaluation: không đủ để hỏi average accuracy là bao nhiêu. Ta phải hỏi model yếu ở slice nào, nhạy với loại shift nào, và performance drop đến từ `X-shift` hay `Y|X-shift`."

**Definition:**

> "ERM tối ưu average risk. Khi dữ liệu heterogeneous, average risk có thể che giấu shortcut và worst-group failure."

**Transition:**

> "Muốn vượt qua điểm mù này, ta có hai hướng tự nhiên: học signal ổn định qua environments, hoặc tối ưu cho worst-case. Đầu tiên là IRM."

### Scene 7 - IRM: Học Những Gì Không Đổi

**Duration target:** ~3.0 phút  
**Mystery:** Nếu shortcut thay đổi, feature nào không thay đổi?

**Narration:**

> "Invariant learning bắt đầu từ một trực giác mạnh: nếu một feature thật sự liên quan causal đến label, quan hệ đó nên ổn định hơn qua nhiều environments."

> "Trong ví dụ bò và lạc đà, background có thể thay đổi: cỏ, tuyết, bãi biển, đường nhựa. Nhưng hình dạng con vật vẫn giữ ý nghĩa dự đoán. Nếu ta có nhiều environments đủ đa dạng, ta có thể dùng sự khác biệt giữa chúng để tìm ra feature ổn định."

> "IRM formalize ý tưởng này. Ta học một representation `Phi(X)`, rồi yêu cầu cùng một classifier `w` phải là classifier tối ưu trên mọi environment. Nếu một representation chỉ hoạt động trong một environment, nó không đạt constraint này."

> "Trực giác hình học là: trong feature space, ta muốn một decision boundary dùng được cho tất cả environments, không phải mỗi environment phải có một boundary khác nhau."

> "Nhưng tutorial cũng nhắc rõ limitation. IRM cần environment labels tốt, và training environments phải đủ đa dạng. Nếu tất cả environments đều có cùng shortcut, model không có tín hiệu để biết shortcut đó là spurious. Nếu dataset đã bị gộp mà mất source labels, ta thậm chí không có environments để dùng."

> "Đây là lý do Part 2 nói đến việc học hoặc khám phá heterogeneous environments từ pooled data, ví dụ Heterogeneous Risk Minimization."

**Definition:**

> "IRM tìm representation sao cho cùng một predictor là tối ưu qua nhiều environments. Nó mạnh khi environments thật sự giúp lộ ra điều gì ổn định."

**Transition:**

> "Một hướng khác không hỏi feature nào invariant. Nó hỏi: nếu điều tệ nhất xảy ra, model có còn ổn không?"

### Scene 8 - DRO: Học Từ Trường Hợp Xấu Nhất

**Duration target:** ~2.8 phút  
**Mystery:** Nếu không biết target shift, ta tối ưu cho ai?

**Narration:**

> "DRO, Distributionally Robust Optimization, thay đổi objective của ERM. Thay vì tối ưu loss trên training distribution duy nhất, ta xét một tập các distributions có thể xảy ra, rồi tối ưu cho distribution xấu nhất trong tập đó."

> "Công thức trực giác là: `min_theta max_Q E_Q[L(theta)]`. Model phải làm tốt ngay cả khi adversary chọn distribution gây loss cao nhất."

> "Điểm mấu chốt là uncertainty set: tập `Q` nào được xem là khả dĩ? Tutorial Part 1 nói nhiều về f-divergence và Wasserstein distance. f-divergence giống như reweight các sample đã có. Wasserstein distance còn tính đến geometry: cần di chuyển probability mass bao xa."

> "Nhưng cũng chính ở đây DRO có giả định mạnh. Nếu uncertainty set không phản ánh shift thật, worst-case distribution có thể quá bảo thủ hoặc không giống target domain. Tutorial cho thấy trên nhiều tabular datasets, nhiều DRO methods không cải thiện đáng kể so với ERM hoặc baseline đơn giản."

> "Part 2 bổ sung một vấn đề khác: high loss sample không phải lúc nào cũng là hard sample đáng học. Nó có thể là noisy sample, label sai, hoặc outlier. Nếu DRO upweight noise quá nhiều, model học nhiễu thay vì học signal."

> "Vì vậy, DRO không phải nút bấm magic. Nó hữu ích khi worst-case set, group definition, hoặc geometry thật sự phù hợp với shift trong ứng dụng."

**Definition:**

> "DRO tối ưu performance trong trường hợp xấu nhất thuộc một uncertainty set. Sức mạnh của nó phụ thuộc vào việc set đó có mô tả đúng shift thật hay không."

**Transition:**

> "IRM nói về invariance. DRO nói về robustness. Còn một góc nhìn thứ ba hỏi thẳng hơn: đâu là quan hệ nhân quả ổn định?"

### Scene 9 - Stable Learning: Nhìn Từ Góc Nhân Quả

**Duration target:** ~2.5 phút  
**Mystery:** Nếu hiểu cấu trúc nhân quả, ta có thể loại shortcut trực tiếp không?

**Narration:**

> "Stable Learning nhìn vấn đề từ phía causality. Nếu spurious correlation xuất hiện do confounders, ta không chỉ muốn model robust hơn; ta muốn làm yếu đi ảnh hưởng của confounder trong dữ liệu huấn luyện."

> "Ví dụ một biến ẩn như season, location, hoặc hospital protocol có thể ảnh hưởng đến cả feature và label. Khi đó model thấy một correlation rất mạnh, nhưng correlation này không ổn định khi environment đổi."

> "Một hướng stable learning là sample reweighting: gán trọng số cho các sample sao cho trong weighted distribution, các features bớt phụ thuộc nhau hơn. Khi spurious feature không còn đi kèm causal feature quá chặt, model buộc phải đánh giá contribution của từng feature rõ hơn."

> "Điều này nối với thông điệp chung của tutorial: invariance, robustness, và causality là ba góc nhìn khác nhau, nhưng đều cố tránh việc model dựa vào shortcut không ổn định."

> "Trong thực tế, stable learning cũng cần domain knowledge hoặc assumptions về causal structure. Vì vậy nó không thay thế việc phân tích dữ liệu. Nó là một công cụ trong pipeline heterogeneity-aware."

**Definition:**

> "Stable Learning cố học signal ổn định bằng cách giảm ảnh hưởng của confounders và khuyến khích model dựa vào causal features."

**Transition:**

> "Bây giờ ta có thể tổng kết: vấn đề không chỉ nằm ở một thuật toán, mà nằm ở cách ta nhìn toàn bộ workflow ML."

### Scene 10 - Conclusion: Heterogeneity Là Thông Tin

**Duration target:** ~2.2 phút  
**Mystery:** Bài học cuối cùng là chọn method nào?

**Narration:**

> "Ta bắt đầu từ một câu hỏi: tại sao AI có thể thành công trong lab nhưng thất bại ngoài đời? Câu trả lời không phải chỉ là model yếu. Câu trả lời là training data và deployment data thường không đến từ cùng một thế giới."

> "i.i.d. là điều kiện lý tưởng. Distribution shift là điều xảy ra khi điều kiện đó vỡ. Data heterogeneity là lý do sâu hơn: dữ liệu thực tế là mixture của nhiều sources, subpopulations, mechanisms, hard samples và noisy samples."

> "Nếu ta bỏ qua heterogeneity, model có thể học spurious correlations. ERM có thể đạt average accuracy cao nhưng che giấu worst-group failure."

> "IRM cố tìm invariant features qua environments. DRO cố tối ưu cho worst-case distribution hoặc group. Stable Learning cố loại ảnh hưởng confounders và giữ causal signal."

> "Nhưng tutorial nhấn mạnh: không có method nào là silver bullet. IRM cần environments tốt. DRO cần uncertainty set phù hợp và phải tránh noisy samples. Stable Learning cần giả định nhân quả hợp lý. Pretrained models có lợi từ dữ liệu lớn, nhưng thêm nhiều data không tự động tạo robustness."

> "Heterogeneity-aware ML nghĩa là dùng hiểu biết về dữ liệu xuyên suốt pipeline: trước training, phát hiện subpopulations; trong training, học hoặc khai thác environments; khi evaluation, tìm error slices và stability; sau deployment, phân rã performance drop thành `X-shift` và `Y|X-shift` để chọn can thiệp đúng."

**Final message:**

> "Data heterogeneity is not a bug in your dataset. It is a feature of the real world. Và học cách nhìn thấy nó là bước đầu để xây dựng AI đáng tin cậy hơn."

## 4. Storyboard Sơ Bộ Toàn Bộ Scenes

Storyboard này đủ chi tiết để chia việc animation. Mỗi dòng là một beat hình ảnh chính, không phải từng animation nhỏ. Câu mô tả dùng tiếng Việt có dấu; thuật ngữ chuyên ngành giữ tiếng Anh khi cần, ví dụ `distribution shift`, `OOD`, `spurious correlation`, `worst-group accuracy`.

### Scene 1 - Intro

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 1.1 | Màn hình tối, tiêu đề hiện dần | `Data Heterogeneity & OOD Generalization` | Định vị chủ đề chính của video |
| 1.2 | Montage nhanh: robot hút bụi bị kẹt, camera bóng đá theo nhầm trọng tài, medical AI, self-driving | `Thành công trong lab != đáng tin ngoài đời` | Mở hook bằng các failure cases có trong transcript |
| 1.3 | Thẻ `99% accuracy` xuất hiện rồi nứt vỡ | `99% accuracy... vẫn sai ngoài đời?` | Tạo câu hỏi mở đầu cho người xem |
| 1.4 | Hai vùng "train world" và "real world" tách xa nhau | `Train distribution != Deployment distribution` | Dẫn sang giả định `i.i.d.` |

### Scene 2 - i.i.d.

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 2.1 | Hai đám điểm `training data` và `test data` chồng lên nhau | `Training data`, `Test data` | Giải thích trực quan giả định `i.i.d.` |
| 2.2 | Công thức hiện ở giữa màn hình | `P_train(X,Y) = P_test(X,Y)` | Đưa định nghĩa xác suất vào sau trực giác |
| 2.3 | Đám điểm test dịch sang phải, không còn trùng training | `Distribution shift` | Cho thấy điều kiện lý tưởng bị phá vỡ |
| 2.4 | Bộ đếm accuracy giảm dần | `95% -> 74% -> 62%` | Minh họa hậu quả khi test distribution đổi |
| 2.5 | Hộp kết luận cuối scene | `i.i.d. là điều kiện lý tưởng` | Chốt insight bằng tiếng Việt dễ hiểu |

### Scene 3 - Distribution Shift

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 3.1 | Ba panel xuất hiện cạnh nhau | `Điều gì đang thay đổi?` | Đặt câu hỏi phân loại shift |
| 3.2 | Panel 1: input cloud dịch/chuyển hình, decision boundary giữ nguyên | `X-shift` | Giải thích input distribution thay đổi |
| 3.3 | Panel 2: tỷ lệ class thay đổi bằng pie chart/bar chart | `Label shift` | Giải thích label prior thay đổi |
| 3.4 | Panel 3: decision boundary xoay hoặc đổi vị trí | `Y|X-shift` | Giải thích prediction mechanism thay đổi |
| 3.5 | Cây tổng kết ba nhánh shift | `Shift pattern rất quan trọng` | Dẫn sang câu hỏi: shift đến từ heterogeneity nào? |

### Scene 4 - Data Heterogeneity

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 4.1 | Nhiều nguồn dữ liệu chảy vào một đám điểm xám | `Pooled training data` | Cho thấy dữ liệu đã bị merge thành một khối |
| 4.2 | Đám điểm xám tách thành ba cụm màu | `Hospital A`, `Hospital B`, `Hospital C` | Minh họa nhiều `environments` trong cùng dataset |
| 4.3 | Mỗi cụm có nhãn nguyên nhân khác biệt | `Device`, `Demographics`, `Protocol` | Chỉ ra nguồn gốc cụ thể của `data heterogeneity` |
| 4.4 | Split-screen: cùng vùng `X`, nhưng hai nhóm có hai xu hướng `Y|X` khác nhau | `Same X, different Y|X` | Đưa ý chính từ Part 2: subpopulation có cơ chế dự đoán khác nhau |
| 4.5 | Ghi chú nhỏ về thông tin dự đoán khi chia nhóm | `Grouping can add predictive information` | Gợi trực giác `predictive heterogeneity` |
| 4.6 | Hộp insight cuối scene | `Heterogeneity = hidden information` | Chốt rằng heterogeneity là thông tin ẩn, không chỉ là noise |

### Scene 5 - Spurious Correlations

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 5.1 | Bò trên cỏ và lạc đà trên sa mạc | `Training accuracy: 98%` | Thiết lập shortcut có vẻ hiệu quả |
| 5.2 | Feature importance làm sáng background, làm mờ shape | `Model learned: grass -> cow` | Cho thấy model học shortcut thay vì causal feature |
| 5.3 | Bò trên bãi biển bị dự đoán sai | `OOD failure` | Cho thấy shortcut vỡ khi environment thay đổi |
| 5.4 | Ba environments với background khác nhau | `Variation làm lộ shortcut` | Giải thích heterogeneity giúp phát hiện spurious signal |
| 5.5 | Causal graph phân biệt shape và background | `Shape: stable`, `Background: spurious` | Định nghĩa `spurious correlation` bằng hình ảnh |

### Scene 6 - ERM

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 6.1 | Công thức ERM hiện từng phần | `min average loss` | Giới thiệu objective của `ERM` |
| 6.2 | Quả bóng lăn xuống loss landscape | `ERM tìm một minimum` | Minh họa quá trình optimization |
| 6.3 | Công thức group-weighted risk | `0.85 R_majority + 0.10 R_A + 0.05 R_B` | Cho thấy majority group chi phối average risk |
| 6.4 | Bar chart accuracy theo từng group | `Average: 95%`, `Worst group: 43%` | Cho thấy average accuracy che giấu worst-group failure |
| 6.5 | Tách hai luồng causal signal và spurious signal | `Signal nào giảm loss thì ERM có thể dùng` | Giải thích vì sao ERM dễ học shortcut |
| 6.6 | Cảnh báo metric cuối scene | `Average accuracy là chưa đủ` | Dẫn sang IRM/DRO và evaluation theo slices |

### Scene 7 - IRM

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 7.1 | Ba environments có background khác nhau | `Feature nào hữu ích ở mọi environment?` | Đặt trực giác về invariance |
| 7.2 | Raw data đi qua feature extractor `Phi` | `Representation` | Giới thiệu representation `Phi(X)` |
| 7.3 | Một decision boundary được copy qua cả ba panel | `Cùng classifier w` | Minh họa ý tưởng cốt lõi của `IRM` |
| 7.4 | Công thức objective và constraint của IRM | `w optimal ở mọi environment` | Neo kỹ thuật để không chỉ kể bằng ví dụ |
| 7.5 | Huy hiệu cảnh báo limitation | `Cần environment labels tốt` | Nói rõ IRM cần environment labels tốt |
| 7.6 | Pooled data không có nhãn nguồn | `No training environments?` | Dẫn sang bài toán environment discovery |

### Scene 8 - DRO

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 8.1 | Bar chart so sánh ERM average và DRO worst-case | `Average vs worst-case` | Phân biệt ERM và `DRO` |
| 8.2 | Quả cầu distribution quanh `P_train` | `Uncertainty set` | Giải thích tập phân phối mà DRO xét |
| 8.3 | `f-divergence` như việc đổi trọng số sample | `Đổi sample weights` | Tóm trực giác từ tutorial Part 1 |
| 8.4 | `Wasserstein distance` như việc di chuyển probability mass | `Di chuyển probability mass` | Thêm yếu tố geometry của dữ liệu |
| 8.5 | Một noisy sample cô lập nhưng có loss cao | `Hard sample hay noise?` | Nêu limitation từ Part 2: DRO có thể upweight noise |
| 8.6 | Hộp cảnh báo cuối scene | `DRO works only if the set matches the shift` | Tránh overclaim rằng DRO luôn tốt hơn ERM |

### Scene 9 - Stable Learning

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 9.1 | Causal graph có confounder `Z` | `Confounder tạo shortcut` | Thiết lập góc nhìn causal |
| 9.2 | Các data points đổi kích thước theo trọng số | `Sample reweighting` | Minh họa cơ chế của Stable Learning |
| 9.3 | Các đường correlation giữa features mờ dần | `Decorrelate features` | Cho thấy mục tiêu giảm ảnh hưởng của confounding |
| 9.4 | Tam giác ba hướng tiếp cận | `Invariance - Robustness - Causality` | Kết nối IRM, DRO, Stable Learning |
| 9.5 | Pipeline tổng hợp | `Analyze -> Train -> Evaluate -> Deploy` | Đưa về thông điệp `heterogeneity-aware ML` |

### Scene 10 - Conclusion

| Beat | Visual | On-screen text | Content note |
|---|---|---|---|
| 10.1 | Chuỗi recap chạy nhanh | `i.i.d. -> Shift -> Heterogeneity -> ERM fails` | Tóm lại hành trình khái niệm |
| 10.2 | Bảng so sánh methods | `ERM / IRM / DRO / Stable Learning` | So sánh vai trò và limitation của từng method |
| 10.3 | Pipeline bốn giai đoạn từ Part 2 | `Data collection -> Training -> Evaluation -> Deployment` | Nhấn mạnh system-level view của tutorial |
| 10.4 | Các open problems hiện tuần tự | `Environment discovery`, `Uncertainty`, `Active data collection` | Kết nối với future directions |
| 10.5 | Final message ở giữa màn hình | `Heterogeneity là feature của thế giới thực` | Đóng video bằng thông điệp chính |

## 5. Kiểm Tra Độ Chính Xác So Với Tutorial Transcript

### Mapping Theo Từng Scene

| Scene | Bằng chứng từ tutorial | Quyết định trong script | Trạng thái kiểm chứng |
|---|---|---|---|
| 1 | Part 1 mở bằng failure cases: robot hút bụi, camera thể thao, medical/COVID shortcut, self-driving | Dùng montage failure cases, không mở bằng ví dụ AI chung chung | Đúng với tutorial |
| 2 | Part 1 giới thiệu `OOD` như train/deployment mismatch và poor generalization | Giải thích `i.i.d.` là điều kiện lý tưởng, sau đó cho test distribution dịch đi | Đúng với tutorial |
| 3 | Part 1 phân biệt `X-shift` và `Y|X-shift`; visual notes nói ML truyền thống thường tập trung vào `X-shift` | Đưa `X-shift`, `label shift`, `Y|X-shift`; nhấn mạnh mechanism shift | Đúng; `label shift` là taxonomy chuẩn được thêm để dễ hiểu |
| 4 | Part 1 nói data có nhiều sources, environments, different `Y|X`, different data sizes. Part 2 nói cần kiểm tra subpopulations có different `Y|X` trước training | Mở rộng scene 4 từ "nhiều nguồn data" sang `Y|X heterogeneity` và trực giác `predictive heterogeneity` | Đúng và sát tutorial hơn |
| 5 | Part 1 dùng cow/camel/background trong phần IRM; tutorial nhấn mạnh stable mechanism so với spurious context | Dùng shortcut cow/camel/background và nhiều environments để làm lộ background instability | Đúng với tutorial |
| 6 | Part 1 đặt ERM đối lập với DRO; Part 2 nói ERM over all data che giấu subgroup mechanisms và evaluation cần slices | Dùng ERM average objective, group-weighted risk, `worst-group failure` | Đúng với tutorial |
| 7 | Part 1: IRM yêu cầu cùng classifier tối ưu qua environments. Part 2: chất lượng environment quan trọng và nhiều dataset mất source labels | Đưa công thức IRM và limitation về `environment labels` | Đúng với tutorial |
| 8 | Part 1: DRO có `f-divergence`, `Wasserstein`, uncertainty set, over-pessimism, mismatch. Part 2: noisy samples và data geometry | Đưa uncertainty set, trực giác f-div/Wasserstein, limitation over-pessimism/noise | Đúng với tutorial |
| 9 | Tutorial và research report nối stable learning với causality, sample reweighting, confounders | Trình bày Stable Learning như causal/decorrelation approach, không nói là silver bullet | Đúng với tutorial |
| 10 | Part 2 recap `heterogeneity-aware ML` xuyên suốt collection, training, evaluation, deployment; future directions có active collection và uncertainty | Kết bằng system-level pipeline và open problems | Đúng với tutorial |

### Danh Sách Không Được Overclaim

- Không nói `IRM` luôn tìm được causal features. Cách nói đúng: `IRM` khuyến khích invariance khi environments đủ informative.
- Không nói `DRO` luôn tốt hơn `ERM`. Transcript/visual notes cho thấy nhiều DRO methods không cải thiện đáng kể so với ERM trên real tabular shifts.
- Không nói thêm nhiều data luôn làm model robust hơn. Phần `CLIP` của Part 1 nói gains đến từ data, nhưng cũng nhấn mạnh "just adding more data != better".
- Không nói mọi heterogeneity đều hữu ích. Cách nói đúng: heterogeneity có thể là hidden information nếu được phân tích đúng.
- Không gộp `Y|X-shift` vào `covariate shift`. Tutorial xem thay đổi `Y|X` là trung tâm và khó hơn.
- Không gọi mọi correlation là `spurious correlation`. Một correlation là spurious khi nó không stable/causal cho deployment setting.
- Không xem average accuracy là đủ. Tutorial Part 2 nhấn mạnh error slices, stability, và shift attribution.

### Các Khái Niệm Bắt Buộc Phải Có Trên Màn Hình

| Khái niệm | Yêu cầu hình ảnh tối thiểu |
|---|---|
| `i.i.d.` | Công thức `P_train(X,Y) = P_test(X,Y)` |
| `X-shift` vs `Y|X-shift` | Ít nhất một panel input dịch chuyển và một panel decision boundary/mechanism thay đổi |
| `Data heterogeneity` | Pooled data tách thành environments/subpopulations |
| `Predictive heterogeneity` | Có công thức tùy chọn hoặc dòng chữ: `Grouping can add predictive information` |
| `Spurious correlation` | Background shortcut bị phá vỡ ở environment mới |
| `ERM` | Average loss formula và ví dụ group-risk/worst-group |
| `IRM` | Cùng classifier `w` tối ưu qua nhiều environments |
| `DRO` | Objective dạng `min max` và `uncertainty set` |
| `Stable Learning` | Confounder graph và sample reweighting/decorrelation |
| `Heterogeneity-aware ML` | Pipeline đầy đủ: collection, training, evaluation, deployment |

## 6. Checklist Cuối Cho TV2

TV2 có thể xem vai trò đã hoàn thành khi các điều kiện sau đều đúng:

- [x] Scene 4-6 đã có narration và animation beats mở rộng trong `docs/02_video_script.md`.
- [x] File này đã có full narration draft cho toàn bộ 10 scenes.
- [x] File này đã có storyboard sơ bộ cho toàn bộ 10 scenes.
- [x] Các limitation của `IRM`, `DRO`, `ERM`, `Stable Learning` đã được viết rõ.
- [x] Kết luận đi đúng thông điệp data-centric của tutorial: hiểu heterogeneity trước, chọn method sau.
