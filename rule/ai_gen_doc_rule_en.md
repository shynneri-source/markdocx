# Markdown Textbook Writing Rules for AI

> **Purpose**: This file contains rules for AI models (ChatGPT, Claude, Gemini, etc.) to generate
> Markdown textbook files that convert cleanly to DOCX with properly rendered math formulas
> and syntax-highlighted code blocks.

---

## 1. DOCUMENT STRUCTURE

### 1.1 Heading Hierarchy

```markdown
# Chapter 1: Chapter Title (H1 — use only once per file)

## 1.1 Section Title (H2)

### 1.1.1 Subsection Title (H3)

#### Subheading (H4 — use sparingly for further subdivision)
```

**Rules:**
- Each file must have exactly **one H1 heading** (the chapter/part title)
- Number headings sequentially: `## 1.1`, `### 1.1.1`, `#### a)` …
- Never skip heading levels (e.g., H1 → H3 without H2)
- Always leave one blank line before and after every heading

### 1.2 Chapter Template

```markdown
# Chapter X: Title

> **Summary:** Brief overview of the chapter content.

## Learning Objectives
- Objective 1
- Objective 2

## X.1 Main Content

### X.1.1 Subsection

Content…

## Chapter Summary

## Exercises
```

---

## 2. MATH FORMULAS (LATEX)

### 2.1 Inline Math

Use **single dollar signs** `$...$` for short formulas within running text.

```markdown
The quadratic equation $ax^2 + bx + c = 0$ is solved using the quadratic formula.

The derivative of $f(x) = x^n$ is $f'(x) = nx^{n-1}$.

For $n \geq 1$ and $x \in \mathbb{R}$.
```

**Inline math rules:**
- No whitespace immediately after the opening `$` or before the closing `$`
- Use for short, simple expressions only
- ✅ Correct: `$x^2 + y^2 = r^2$`
- ❌ Wrong: `$ x^2 + y^2 = r^2 $` (extraneous spaces)

### 2.2 Display Math

Use **double dollar signs** `$$...$$` for standalone formulas on their own line.

```markdown
The quadratic formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Definite integral:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$
```

**Display math rules:**
- `$$` must appear on its own line
- Leave one blank line before and after each `$$` block
- Use for long, complex, or important formulas
- Each display block should contain **one expression only**

### 2.3 Supported LaTeX Commands

#### Basic symbols:
| Command | Renders | Example |
|---------|---------|---------|
| `\frac{a}{b}` | Fraction | $\frac{a}{b}$ |
| `x^{n}` | Superscript | $x^{n}$ |
| `x_{i}` | Subscript | $x_{i}$ |
| `\sqrt{x}` | Square root | $\sqrt{x}$ |
| `\sqrt[n]{x}` | n-th root | $\sqrt[n]{x}$ |
| `\sum_{i=1}^{n}` | Summation | $\sum_{i=1}^{n}$ |
| `\prod_{i=1}^{n}` | Product | $\prod_{i=1}^{n}$ |
| `\int_a^b` | Integral | $\int_a^b$ |
| `\lim_{x \to 0}` | Limit | $\lim_{x \to 0}$ |
| `\infty` | Infinity | $\infty$ |

#### Greek letters:
| Command | Renders | Command | Renders |
|---------|---------|---------|---------|
| `\alpha` | α | `\beta` | β |
| `\gamma` | γ | `\delta` | δ |
| `\epsilon` | ε | `\theta` | θ |
| `\lambda` | λ | `\mu` | μ |
| `\pi` | π | `\sigma` | σ |
| `\omega` | ω | `\phi` | φ |

#### Relation & logic symbols:
| Command | Renders | Command | Renders |
|---------|---------|---------|---------|
| `\leq` | ≤ | `\geq` | ≥ |
| `\neq` | ≠ | `\approx` | ≈ |
| `\in` | ∈ | `\notin` | ∉ |
| `\subset` | ⊂ | `\forall` | ∀ |
| `\exists` | ∃ | `\Rightarrow` | ⇒ |
| `\Leftrightarrow` | ⇔ | `\cup` | ∪ |
| `\cap` | ∩ | `\mathbb{R}` | ℝ |

### 2.4 Complex Formula Examples

```markdown
**Taylor's Theorem:**

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

**Matrix:**

$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$

**System of equations:**

$$\begin{cases} 2x + 3y = 5 \\ 4x - y = 1 \end{cases}$$
```

### 2.5 AVOID These Commands

The following LaTeX commands are **not supported** and should be avoided:

- ❌ `\newcommand` — Custom command definitions
- ❌ `\usepackage` — Package imports
- ❌ Complex environments: `align`, `gather`, `multline` — Use separate `$$...$$` blocks instead
- ❌ `\tag{}` — Equation numbering
- ❌ `\label{}` / `\ref{}` — Cross-references
- ❌ `\color{}` — Colored formulas

**Well-supported (use freely):**
- ✅ `\text{}`, `\mathrm{}`, `\mathbf{}`, `\mathit{}`
- ✅ `\operatorname{}`
- ✅ `\left` / `\right` (auto-scaling delimiters)
- ✅ `\quad`, `\qquad`, `\,`, `\;`
- ✅ `\begin{pmatrix}`, `\begin{bmatrix}`, `\begin{vmatrix}` (matrices)
- ✅ `\begin{cases}` (piecewise / systems of equations)
- ✅ `\overline{}`, `\underline{}`, `\hat{}`, `\vec{}`, `\dot{}`

---

## 3. CODE BLOCKS

### 3.1 Fenced Code Blocks

**Always** specify the language after the opening ` ``` ` for proper syntax highlighting.

````markdown
```python
def fibonacci(n):
    """Return the n-th Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Usage
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```
````

### 3.2 Supported Languages

| Language | Identifier |
|----------|-----------|
| Python | `python` |
| JavaScript | `javascript` or `js` |
| TypeScript | `typescript` or `ts` |
| Java | `java` |
| C | `c` |
| C++ | `cpp` |
| C# | `csharp` or `cs` |
| Go | `go` |
| Rust | `rust` or `rs` |
| Ruby | `ruby` or `rb` |
| PHP | `php` |
| Swift | `swift` |
| Kotlin | `kotlin` or `kt` |
| SQL | `sql` |
| HTML | `html` |
| CSS | `css` |
| Bash / Shell | `bash` or `sh` |
| YAML | `yaml` or `yml` |
| JSON | `json` |
| XML | `xml` |
| LaTeX | `latex` or `tex` |
| Markdown | `markdown` or `md` |
| Plain text | `text` or `plaintext` |

### 3.3 Code Rules

- **Always specify the language** after the opening triple backtick
- Keep code **concise** and focused on the concept being illustrated
- Add **explanatory comments** inside the code
- Each code block should be **30–40 lines max** (split if longer)
- Use **4 spaces** for indentation (never tabs)
- Leave one blank line before and after every code block

### 3.4 Inline Code

Use single backticks for code references within running text:

```markdown
The `print()` function in Python outputs to the console.

Variable `x` has type `int` while `name` has type `str`.

Run `pip install numpy` to install the NumPy library.
```

---

## 4. TABLES

### 4.1 Table Syntax

```markdown
| Algorithm | Time Complexity | Space Complexity |
|:----------|:---------------:|----------------:|
| Bubble Sort | $O(n^2)$ | $O(1)$ |
| Merge Sort | $O(n \log n)$ | $O(n)$ |
| Quick Sort | $O(n \log n)$ | $O(\log n)$ |
```

### 4.2 Table Rules

- **Always include a header row** (first row)
- **Always include a separator row** (`|---|`)
- Alignment: `:---` (left), `:---:` (center), `---:` (right)
- **Inline math** is allowed inside table cells
- **Bold/italic** is allowed inside table cells
- Do **not** place code blocks inside tables
- Keep tables simple — **5–6 columns max**

---

## 5. LISTS

### 5.1 Unordered Lists

```markdown
- First item
- Second item
  - Sub-item 2.1
  - Sub-item 2.2
    - Deeper sub-item
- Third item
```

### 5.2 Ordered Lists

```markdown
1. First step
2. Second step
   1. Sub-step 2.1
   2. Sub-step 2.2
3. Third step
```

### 5.3 List Rules

- Use `-` for unordered lists (not `*` or `+`)
- Use `1.`, `2.`, `3.` for ordered lists
- Indent **2 spaces** for nested items
- Do not nest more than **3 levels deep**
- Leave one blank line before and after every list

---

## 6. TEXT FORMATTING

### 6.1 Bold, Italic, Strikethrough

```markdown
**Bold text** for important terms.

*Italic text* for emphasis or foreign terms.

***Bold italic*** for special emphasis.

~~Strikethrough~~ for deprecated or incorrect information.
```

### 6.2 Blockquotes

```markdown
> **Definition:** An algorithm is a finite set of well-defined steps
> designed to solve a specific problem.

> **Note:** This is important information to remember.

> **Example:** An illustration of the concept discussed above.
```

### 6.3 Horizontal Rules

```markdown
Content before

---

Content after
```

---

## 7. IMAGES

### 7.1 Image Syntax

```markdown
![Image description](path/to/image.png)

![Sorting algorithm comparison chart](images/sorting_chart.png)
```

### 7.2 Image Rules

- **Always include alt text** describing the image content
- Place images in an `images/` directory at the same level as the `.md` file
- File names: lowercase, underscore-separated, e.g. `binary_tree_example.png`
- Use PNG or JPG format
- Each image should be on its own line with blank lines before and after

---

## 8. LINKS

```markdown
See the [Wikipedia article](https://en.wikipedia.org) for details.

Refer to [Section 2.3](#23-supported-latex-commands) for the full list.
```

---

## 9. FOOTNOTES

```markdown
Dijkstra's algorithm[^1] is widely used for shortest-path computation.

[^1]: Edsger W. Dijkstra, "A note on two problems in connexion with graphs", 1959.
```

---

## 10. COMPLETE TEMPLATE

Below is a full chapter template:

````markdown
# Chapter 3: Calculus — Derivatives and Integrals

> **Summary:** This chapter covers the fundamentals of derivatives and integrals,
> including definitions, formulas, and real-world applications.

## Learning Objectives

- Understand the concept of a derivative and its geometric interpretation
- Master the basic differentiation rules
- Understand the concept of an integral and its relationship to differentiation
- Apply integrals to compute areas and volumes

---

## 3.1 Derivatives

### 3.1.1 Definition

> **Definition:** The derivative of a function $f(x)$ at point $x_0$ is defined as:

$$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

If this limit exists and is finite, we say $f$ is **differentiable** at $x_0$.

### 3.1.2 Differentiation Rules

| Rule | Formula |
|:-----|:--------|
| Constant | $(c)' = 0$ |
| Power | $(x^n)' = nx^{n-1}$ |
| Sum | $(f + g)' = f' + g'$ |
| Product | $(fg)' = f'g + fg'$ |
| Quotient | $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$ |
| Chain | $(f(g(x)))' = f'(g(x)) \cdot g'(x)$ |

### 3.1.3 Python Example

```python
import numpy as np

def numerical_derivative(f, x, h=1e-7):
    """Compute the numerical derivative using central differences."""
    return (f(x + h) - f(x - h)) / (2 * h)

# f(x) = x^3 - 2x + 1
f = lambda x: x**3 - 2*x + 1
f_prime = lambda x: 3*x**2 - 2  # Analytical derivative

print(f"f'(1) ≈ {numerical_derivative(f, 1):.6f}")  # ≈ 1.0
print(f"f'(1) exact = {f_prime(1)}")                  # = 1
```

---

## 3.2 Integrals

### 3.2.1 Definition

The definite integral of $f(x)$ on the interval $[a, b]$:

$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$$

where $\Delta x = \frac{b-a}{n}$.

> **Fundamental Theorem of Calculus:** If $F$ is an antiderivative of $f$ on $[a, b]$, then:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

---

## Chapter Summary

- Derivatives measure the **rate of change** of a function
- Integrals measure **cumulative accumulation** (area under the curve)
- Differentiation and integration are **inverse operations**

## Exercises

1. Compute the derivative of $f(x) = 3x^4 - 2x^2 + 5x - 1$
2. Evaluate the integral $\int_0^1 (x^2 + 2x) \, dx$
3. Write a Python program to approximate an integral using the trapezoidal rule
````

---

## 11. PRE-EXPORT CHECKLIST

Before finalizing a Markdown file, verify:

- [ ] Exactly one H1 heading per file
- [ ] Heading hierarchy is correct (H1 → H2 → H3 — no skipped levels)
- [ ] All inline formulas use `$...$` with no extraneous spaces
- [ ] All display formulas use `$$...$$` on their own lines
- [ ] All code blocks specify a language
- [ ] Tables have a header row and a separator row
- [ ] Images have alt text
- [ ] Blank lines before/after: headings, code blocks, tables, lists, blockquotes
- [ ] No raw HTML (except `<br>`)
- [ ] No unsupported LaTeX commands (see Section 2.5)
