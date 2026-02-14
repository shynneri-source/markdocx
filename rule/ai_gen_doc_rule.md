# 📐 QUY TẮC VIẾT GIÁO TRÌNH MARKDOWN CHO AI

> **Mục đích**: File này chứa các quy tắc để AI (ChatGPT, Claude, Gemini...) tạo ra file Markdown giáo trình
> đúng chuẩn, dễ dàng chuyển đổi sang DOCX với công thức toán học và code được render hoàn hảo.

---

## 1. CẤU TRÚC TỔNG THỂ

### 1.1 Heading Hierarchy

```markdown
# Chương 1: Tên Chương (H1 - chỉ dùng 1 lần cho tiêu đề chương)

## 1.1 Tên mục lớn (H2)

### 1.1.1 Tên mục con (H3)

#### Tiêu đề nhỏ (H4 - dùng khi cần chia nhỏ thêm)
```

**Quy tắc:**
- Mỗi file chỉ có **1 heading H1** duy nhất (tiêu đề chương)
- Đánh số thứ tự heading: `## 1.1`, `### 1.1.1`, `#### a)` ...
- Không nhảy cấp heading (không từ H1 xuống H3 mà bỏ H2)
- Luôn có 1 dòng trống trước và sau heading

### 1.2 Cấu Trúc Chương

```markdown
# Chương X: Tên Chương

> **Tóm tắt:** Mô tả ngắn gọn nội dung chương.

## Mục tiêu học tập
- Mục tiêu 1
- Mục tiêu 2

## X.1 Nội dung chính

### X.1.1 Phần con

Nội dung...

## Tóm tắt chương

## Bài tập
```

---

## 2. CÔNG THỨC TOÁN HỌC (LATEX)

### 2.1 Công Thức Inline (trong dòng)

Dùng **một dấu dollar** `$...$` cho công thức nhỏ nằm trong câu văn.

```markdown
Phương trình bậc hai $ax^2 + bx + c = 0$ có nghiệm được tính bằng công thức nghiệm.

Đạo hàm của $f(x) = x^n$ là $f'(x) = nx^{n-1}$.

Với $n \geq 1$ và $x \in \mathbb{R}$.
```

**Quy tắc inline math:**
- KHÔNG có khoảng trắng ngay sau `$` mở hoặc trước `$` đóng
- Dùng cho công thức ngắn, đơn giản
- ✅ Đúng: `$x^2 + y^2 = r^2$`
- ❌ Sai: `$ x^2 + y^2 = r^2 $` (có khoảng trắng thừa)

### 2.2 Công Thức Display (khối riêng)

Dùng **hai dấu dollar** `$$...$$` cho công thức lớn, trình bày riêng 1 dòng.

```markdown
Công thức nghiệm phương trình bậc hai:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Tích phân xác định:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$
```

**Quy tắc display math:**
- `$$` phải nằm trên dòng riêng biệt
- Có dòng trống trước và sau khối `$$`
- Dùng cho công thức dài, phức tạp, hoặc cần nhấn mạnh
- Mỗi công thức display chỉ chứa MỘT biểu thức

### 2.3 Danh Sách LaTeX Commands Được Hỗ Trợ

#### Ký hiệu cơ bản:
| Lệnh | Kết quả | Ví dụ |
|-------|---------|-------|
| `\frac{a}{b}` | Phân số | $\frac{a}{b}$ |
| `x^{n}` | Lũy thừa | $x^{n}$ |
| `x_{i}` | Chỉ số dưới | $x_{i}$ |
| `\sqrt{x}` | Căn bậc hai | $\sqrt{x}$ |
| `\sqrt[n]{x}` | Căn bậc n | $\sqrt[n]{x}$ |
| `\sum_{i=1}^{n}` | Tổng | $\sum_{i=1}^{n}$ |
| `\prod_{i=1}^{n}` | Tích | $\prod_{i=1}^{n}$ |
| `\int_a^b` | Tích phân | $\int_a^b$ |
| `\lim_{x \to 0}` | Giới hạn | $\lim_{x \to 0}$ |
| `\infty` | Vô cùng | $\infty$ |

#### Ký hiệu Hy Lạp:
| Lệnh | Kết quả | Lệnh | Kết quả |
|-------|---------|-------|---------|
| `\alpha` | α | `\beta` | β |
| `\gamma` | γ | `\delta` | δ |
| `\epsilon` | ε | `\theta` | θ |
| `\lambda` | λ | `\mu` | μ |
| `\pi` | π | `\sigma` | σ |
| `\omega` | ω | `\phi` | φ |

#### Ký hiệu quan hệ & logic:
| Lệnh | Kết quả | Lệnh | Kết quả |
|-------|---------|-------|---------|
| `\leq` | ≤ | `\geq` | ≥ |
| `\neq` | ≠ | `\approx` | ≈ |
| `\in` | ∈ | `\notin` | ∉ |
| `\subset` | ⊂ | `\forall` | ∀ |
| `\exists` | ∃ | `\Rightarrow` | ⇒ |
| `\Leftrightarrow` | ⇔ | `\cup` | ∪ |
| `\cap` | ∩ | `\mathbb{R}` | ℝ |

### 2.4 Ví Dụ Công Thức Phức Tạp

```markdown
**Định lý Taylor:**

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

**Ma trận:**

$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$

**Hệ phương trình:**

$$\begin{cases} 2x + 3y = 5 \\ 4x - y = 1 \end{cases}$$
```

### 2.5 TRÁNH Sử Dụng

Các lệnh LaTeX sau **KHÔNG nên dùng** vì khó render:

- ❌ `\newcommand` → Không hỗ trợ custom commands
- ❌ `\usepackage` → Không hỗ trợ packages
- ❌ Environments phức tạp: `align`, `gather`, `multline` → Dùng nhiều khối `$$...$$` riêng lẻ thay thế
- ❌ `\tag{}` → Không hỗ trợ đánh số phương trình
- ❌ `\label{}` / `\ref{}` → Không hỗ trợ tham chiếu chéo LaTeX
- ❌ `\color{}` → Không hỗ trợ màu trong công thức

**Được hỗ trợ tốt (dùng thoải mái):**
- ✅ `\text{}`, `\mathrm{}`, `\mathbf{}`, `\mathit{}`
- ✅ `\operatorname{}`
- ✅ `\left` / `\right` (auto-scale ngoặc)
- ✅ `\quad`, `\qquad`, `\,`, `\;`
- ✅ `\begin{pmatrix}`, `\begin{bmatrix}`, `\begin{vmatrix}` (ma trận)
- ✅ `\begin{cases}` (hệ phương trình)
- ✅ `\overline{}`, `\underline{}`, `\hat{}`, `\vec{}`, `\dot{}`

---

## 3. CODE BLOCKS (KHỐI MÃ NGUỒN)

### 3.1 Code Block Có Ngôn Ngữ

**BẮT BUỘC** chỉ định ngôn ngữ sau ` ``` ` để syntax highlighting hoạt động.

````markdown
```python
def fibonacci(n):
    """Tính số Fibonacci thứ n."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ví dụ sử dụng
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```
````

### 3.2 Ngôn Ngữ Được Hỗ Trợ

| Tên ngôn ngữ | Viết sau ``` |
|---------------|--------------|
| Python | `python` |
| JavaScript | `javascript` hoặc `js` |
| TypeScript | `typescript` hoặc `ts` |
| Java | `java` |
| C | `c` |
| C++ | `cpp` |
| C# | `csharp` hoặc `cs` |
| Go | `go` |
| Rust | `rust` hoặc `rs` |
| Ruby | `ruby` hoặc `rb` |
| PHP | `php` |
| Swift | `swift` |
| Kotlin | `kotlin` hoặc `kt` |
| SQL | `sql` |
| HTML | `html` |
| CSS | `css` |
| Bash/Shell | `bash` hoặc `sh` |
| YAML | `yaml` hoặc `yml` |
| JSON | `json` |
| XML | `xml` |
| LaTeX | `latex` hoặc `tex` |
| Markdown | `markdown` hoặc `md` |
| Plain text | `text` hoặc `plaintext` |

### 3.3 Quy Tắc Code

- **Luôn chỉ định ngôn ngữ** sau triple backtick
- Giữ code **ngắn gọn**, tập trung vào ý muốn minh họa
- Thêm **comment giải thích** trong code
- Mỗi code block không quá **30-40 dòng** (chia nhỏ nếu dài)
- Sử dụng **4 spaces** cho indentation (không dùng tab)
- Có dòng trống trước và sau code block

### 3.4 Inline Code

Dùng single backtick cho code trong câu văn:

```markdown
Hàm `print()` trong Python dùng để in ra màn hình.

Biến `x` có kiểu `int`, còn biến `name` có kiểu `str`.

Chạy lệnh `pip install numpy` để cài đặt thư viện NumPy.
```

---

## 4. BẢNG (TABLES)

### 4.1 Cú Pháp Bảng

```markdown
| Thuật toán | Độ phức tạp thời gian | Độ phức tạp không gian |
|:-----------|:---------------------:|----------------------:|
| Bubble Sort | $O(n^2)$ | $O(1)$ |
| Merge Sort | $O(n \log n)$ | $O(n)$ |
| Quick Sort | $O(n \log n)$ | $O(\log n)$ |
```

### 4.2 Quy Tắc Bảng

- **Luôn có header row** (dòng đầu tiên)
- **Luôn có separator row** (dòng `|---|`)
- Căn chỉnh: `:---` (trái), `:---:` (giữa), `---:` (phải)
- Có thể dùng **inline math** trong ô bảng
- Có thể dùng **bold/italic** trong ô bảng
- Không dùng code block bên trong bảng
- Giữ bảng đơn giản, tối đa **5-6 cột**

---

## 5. DANH SÁCH (LISTS)

### 5.1 Unordered List (danh sách không đánh số)

```markdown
- Mục thứ nhất
- Mục thứ hai
  - Mục con 2.1
  - Mục con 2.2
    - Mục con sâu hơn
- Mục thứ ba
```

### 5.2 Ordered List (danh sách đánh số)

```markdown
1. Bước đầu tiên
2. Bước thứ hai
   1. Bước con 2.1
   2. Bước con 2.2
3. Bước thứ ba
```

### 5.3 Quy Tắc List

- Dùng `-` cho unordered list (không dùng `*` hay `+`)
- Dùng `1.`, `2.`, `3.` cho ordered list
- Indent **2 spaces** cho nested list
- Không lồng quá **3 cấp**
- Có dòng trống trước và sau danh sách

---

## 6. ĐỊNH DẠNG VĂN BẢN

### 6.1 Bold, Italic, Strikethrough

```markdown
**Văn bản in đậm** dùng cho thuật ngữ quan trọng.

*Văn bản in nghiêng* dùng cho thuật ngữ tiếng Anh hoặc nhấn mạnh nhẹ.

***Vừa đậm vừa nghiêng*** dùng cho trường hợp đặc biệt.

~~Văn bản gạch ngang~~ dùng để chỉ thông tin cũ/sai.
```

### 6.2 Blockquote (trích dẫn)

```markdown
> **Định nghĩa:** Thuật toán là một tập hợp hữu hạn các bước thực hiện
> rõ ràng nhằm giải quyết một bài toán nào đó.

> **Lưu ý:** Đây là thông tin quan trọng cần ghi nhớ.

> **Ví dụ:** Minh họa cho khái niệm vừa nêu.
```

### 6.3 Đường Kẻ Ngang

```markdown
Nội dung phần trước

---

Nội dung phần sau
```

---

## 7. HÌNH ẢNH

### 7.1 Cú Pháp Hình Ảnh

```markdown
![Mô tả hình ảnh](đường_dẫn/tên_file.png)

![Biểu đồ thuật toán sắp xếp](images/sorting_chart.png)
```

### 7.2 Quy Tắc Hình Ảnh

- **Luôn có alt text** mô tả nội dung hình
- Đặt hình ảnh trong thư mục `images/` cùng cấp với file .md
- Tên file ảnh: viết thường, dùng `_` phân cách, ví dụ: `binary_tree_example.png`
- Dùng format PNG hoặc JPG
- Hình ảnh nên trên dòng riêng, có dòng trống trước và sau

---

## 8. LINKS

```markdown
Tham khảo thêm tại [Wikipedia](https://vi.wikipedia.org).

Xem chi tiết tại [Mục 2.3](#23-danh-sách-latex-commands-được-hỗ-trợ).
```

---

## 9. FOOTNOTES (CHÚ THÍCH)

```markdown
Thuật toán Dijkstra[^1] được sử dụng rộng rãi trong tìm đường đi ngắn nhất.

[^1]: Edsger W. Dijkstra, "A note on two problems in connexion with graphs", 1959.
```

---

## 10. TEMPLATE MẪU HOÀN CHỈNH

Dưới đây là template mẫu cho một chương giáo trình:

````markdown
# Chương 3: Giải Tích – Đạo Hàm và Tích Phân

> **Tóm tắt:** Chương này trình bày kiến thức cơ bản về đạo hàm và tích phân,
> bao gồm định nghĩa, công thức và ứng dụng trong thực tế.

## Mục tiêu học tập

- Hiểu khái niệm đạo hàm và ý nghĩa hình học
- Nắm vững các quy tắc tính đạo hàm
- Hiểu khái niệm tích phân và mối liên hệ với đạo hàm
- Áp dụng tích phân để tính diện tích và thể tích

---

## 3.1 Đạo Hàm

### 3.1.1 Định nghĩa

> **Định nghĩa:** Đạo hàm của hàm số $f(x)$ tại điểm $x_0$ được định nghĩa là:

$$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

Nếu giới hạn trên tồn tại và hữu hạn, ta nói hàm $f$ **khả vi** tại $x_0$.

### 3.1.2 Các quy tắc tính đạo hàm

| Quy tắc | Công thức |
|:--------|:----------|
| Hằng số | $(c)' = 0$ |
| Lũy thừa | $(x^n)' = nx^{n-1}$ |
| Tổng | $(f + g)' = f' + g'$ |
| Tích | $(fg)' = f'g + fg'$ |
| Thương | $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$ |
| Hàm hợp | $(f(g(x)))' = f'(g(x)) \cdot g'(x)$ |

### 3.1.3 Ví dụ minh họa bằng Python

```python
import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative(f, x, h=1e-7):
    """Tính đạo hàm số bằng phương pháp sai phân."""
    return (f(x + h) - f(x - h)) / (2 * h)

# Hàm f(x) = x^3 - 2x + 1
f = lambda x: x**3 - 2*x + 1
f_prime = lambda x: 3*x**2 - 2  # Đạo hàm giải tích

x = np.linspace(-3, 3, 100)
print(f"f'(1) = {numerical_derivative(f, 1):.6f}")  # ≈ 1.0
print(f"f'(1) exact = {f_prime(1)}")                  # = 1
```

---

## 3.2 Tích Phân

### 3.2.1 Định nghĩa

Tích phân xác định của $f(x)$ trên đoạn $[a, b]$:

$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$$

trong đó $\Delta x = \frac{b-a}{n}$.

> **Định lý cơ bản của giải tích:** Nếu $F$ là nguyên hàm của $f$ trên $[a, b]$, thì:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

---

## Tóm tắt chương

- Đạo hàm đo **tốc độ thay đổi** của hàm số
- Tích phân đo **tổng tích lũy** (diện tích dưới đồ thị)
- Đạo hàm và tích phân là phép toán **ngược nhau**

## Bài tập

1. Tính đạo hàm của $f(x) = 3x^4 - 2x^2 + 5x - 1$
2. Tính tích phân $\int_0^1 (x^2 + 2x) \, dx$
3. Viết chương trình Python tính tích phân số bằng phương pháp hình thang
````

---

## 12. SƠ ĐỒ MA TRẬN (MATRIX)

### 12.1 Cú Pháp Ma Trận

Dùng code block với ngôn ngữ `matrix` để vẽ sơ đồ ma trận trực quan.

**Định dạng đơn giản:**

````markdown
```matrix
name: A
1 2 3
4 5 6
7 8 9
caption: Ma trận A (3×3)
```
````

**Định dạng JSON:**

````markdown
```matrix
{"name": "B", "data": [[1, 0], [0, 1]], "caption": "Ma trận đơn vị"}
```
````

### 12.2 Quy Tắc Ma Trận

- Dùng **dấu cách** hoặc **dấu phẩy** để ngăn cách các giá trị trên mỗi hàng
- `name:` (tùy chọn) thêm nhãn như *A =* trước ma trận
- `caption:` (tùy chọn) thêm chú thích bên dưới
- Các hàng tự động được căn chỉnh cùng độ dài
- Hỗ trợ cả giá trị số và chữ

---

## 13. BIỂU ĐỒ (CHART)

### 13.1 Cú Pháp Biểu Đồ

Dùng code block với ngôn ngữ `chart` để vẽ biểu đồ.

**Định dạng đơn giản:**

````markdown
```chart
type: bar
title: Hiệu suất thuật toán
xlabel: Thuật toán
ylabel: Thời gian (ms)
labels: Bubble Sort, Merge Sort, Quick Sort, Heap Sort
Ngẫu nhiên: 450, 38, 35, 42
Đã sắp xếp: 120, 35, 30, 38
caption: Hình 1: So sánh thuật toán sắp xếp
```
````

**Định dạng JSON:**

````markdown
```chart
{
    "type": "pie",
    "title": "Thị phần",
    "data": {
        "labels": ["Chrome", "Firefox", "Safari", "Edge"],
        "datasets": [{"label": "Phần trăm", "values": [65, 10, 15, 10]}]
    },
    "caption": "Hình 2: Thị phần trình duyệt"
}
```
````

### 13.2 Các Loại Biểu Đồ Hỗ Trợ

| Loại | Từ khóa | Mô tả |
|------|---------|-------|
| Biểu đồ cột | `bar` | Cột dọc (mặc định) |
| Biểu đồ đường | `line` | Đường nối với điểm đánh dấu |
| Biểu đồ tròn | `pie` | Tỉ lệ phần trăm hình tròn |
| Biểu đồ phân tán | `scatter` | Phân bố điểm |

### 13.3 Quy Tắc Biểu Đồ

- Luôn chỉ định `type:` (mặc định là `bar` nếu bỏ qua)
- `labels:` định nghĩa danh mục trục x (ngăn cách bằng dấu phẩy)
- Mỗi dòng `Tên: giá trị` thêm một chuỗi dữ liệu
- Hỗ trợ nhiều chuỗi dữ liệu cho bar, line, scatter
- Biểu đồ tròn chỉ dùng chuỗi dữ liệu đầu tiên
- Dùng `title:`, `xlabel:`, `ylabel:`, `caption:` để đặt nhãn

---

## 14. ĐỒ THỊ (GRAPH)

### 14.1 Cú Pháp Đồ Thị

Dùng code block với ngôn ngữ `graph` để vẽ sơ đồ đồ thị/mạng.

**Định dạng danh sách cạnh:**

````markdown
```graph
title: Cây nhị phân
A -> B
A -> C
B -> D
B -> E
caption: Hình 3: Cây nhị phân đơn giản
```
````

**Đồ thị có trọng số:**

````markdown
```graph
directed: true
title: Đường đi ngắn nhất
A -> B: 5
A -> C: 3
B -> D: 2
C -> D: 7
C -> E: 1
D -> E: 4
caption: Hình 4: Đồ thị có hướng có trọng số
```
````

**Đồ thị vô hướng:**

````markdown
```graph
title: Mạng xã hội
Alice -- Bob
Bob -- Charlie
Alice -- Charlie
Charlie -- David
caption: Hình 5: Kết nối bạn bè
```
````

### 14.2 Quy Tắc Đồ Thị

- Dùng `->` hoặc `-->` cho cạnh có hướng (tự động bật `directed: true`)
- Dùng `--` cho cạnh vô hướng
- Thêm trọng số/nhãn cạnh sau `:` — ví dụ: `A -> B: 5`
- Các đỉnh tự động phát hiện từ cạnh; dùng `nodes:` để thêm đỉnh cô lập
- Dùng `title:` và `caption:` để đặt nhãn

---

## 15. QUY TRÌNH (WORKFLOW)

### 15.1 Cú Pháp Quy Trình

Dùng code block với ngôn ngữ `workflow` để vẽ lưu đồ quy trình.

**Định dạng đơn giản:**

````markdown
```workflow
title: Quy trình đăng nhập
[Bắt đầu]
<Nhập liệu>
(Xác thực thông tin)
{Hợp lệ?}
(Cấp quyền truy cập)
[Kết thúc]
caption: Hình 7: Quy trình xác thực
```
````

**Bố cục ngang:**

````markdown
```workflow
title: Đường ống dữ liệu
direction: horizontal
[Bắt đầu]
<Đọc dữ liệu>
(Chuyển đổi)
(Xác thực)
(Lưu trữ)
[Kết thúc]
caption: Hình 8: Quy trình ETL
```
````

### 15.2 Ký Hiệu Bước

| Ký hiệu | Hình dạng | Công dụng |
|----------|-----------|----------|
| `[text]` | Hộp bo tròn (xanh lá) | Bắt đầu / Kết thúc |
| `(text)` | Hình chữ nhật (xanh dương) | Bước xử lý |
| `{text}` | Hình thoi (vàng) | Quyết định |
| `<text>` | Hình bình hành (tím) | Đầu vào / Đầu ra |

### 15.3 Quy Tắc Quy Trình

- Các bước được nối tuần tự bằng mũi tên (trên xuống dưới hoặc trái sang phải)
- Dùng `direction: horizontal` hoặc `direction: vertical` (mặc định)
- Khuyến nghị dùng `[Bắt đầu]` và `[Kết thúc]` cho bước đầu và cuối
- Giữ quy trình tối đa **8 bước** để dễ đọc
- Dùng `title:` và `caption:` để đặt nhãn
- **Mỗi bước viết ngắn gọn, tối đa 10-12 ký tự** (ví dụ: `Thu nhận ảnh`, `Xử lý ảnh`)
- Nếu tên bước dài hơn 10 ký tự, hệ thống sẽ tự động xuống dòng
- **Bố cục ngang (`horizontal`):** viết tên bước **thật ngắn** (2-3 từ), không dùng câu dài
  - ✅ Đúng: `(Thu nhận ảnh)`, `(Trích xuất)`, `(Phân loại)`
  - ❌ Sai: `(Thu nhận và tiền xử lý ảnh đầu vào)`, `(Trích xuất đặc trưng từ dữ liệu)`
- **Bố cục dọc (`vertical`):** có thể viết dài hơn (tối đa 25-30 ký tự)

---

## 16. CHECKLIST TRƯỚC KHI XUẤT

Trước khi xuất file Markdown, kiểm tra:

- [ ] Mỗi file có đúng 1 heading H1
- [ ] Heading hierarchy đúng thứ tự (H1 → H2 → H3)
- [ ] Tất cả công thức inline dùng `$...$` (không có space thừa)
- [ ] Tất cả công thức display dùng `$$...$$` trên dòng riêng
- [ ] Tất cả code block có chỉ định ngôn ngữ
- [ ] Bảng có header row và separator row
- [ ] Hình ảnh có alt text
- [ ] Có dòng trống trước/sau: heading, code block, bảng, list, blockquote
- [ ] Không dùng HTML raw (trừ `<br>`)
- [ ] Không dùng LaTeX commands không được hỗ trợ (xem mục 2.5)
- [ ] Khối matrix dùng ngôn ngữ `matrix` với định dạng dữ liệu đúng
- [ ] Khối chart dùng ngôn ngữ `chart` với `type:` được chỉ định
- [ ] Khối graph dùng ngôn ngữ `graph` với ký hiệu cạnh hợp lệ
- [ ] Khối workflow dùng ngôn ngữ `workflow` với ký hiệu bước đúng
