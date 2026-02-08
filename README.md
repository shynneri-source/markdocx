<div align="center">

# markdocx

**A Markdown-to-Word converter built for AI-generated textbooks**

Convert Markdown files — complete with LaTeX math, syntax-highlighted code, tables, and images — into polished `.docx` documents in one command.

[![PyPI](https://img.shields.io/pypi/v/markdocx.svg)](https://pypi.org/project/markdocx/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## Why This Exists

Large language models (ChatGPT, Claude, Gemini, …) produce great Markdown, but the journey from `.md` to a well-formatted **Word document** is painful:

- LaTeX formulas become plain text or broken images
- Code blocks lose their highlighting
- Tables, lists, and blockquotes need manual reformatting

**markdocx** bridges that gap. Feed it a Markdown file that follows a few simple rules and get a publication-ready `.docx` — math rendered as native Word OMML equations, code with VS Code–style colors, and everything else properly formatted.

## Features

| Category | What you get |
|:---------|:-------------|
| **Math** | Inline (`$...$`) and display (`$$...$$`) LaTeX → native OMML equations in Word |
| **Code** | 30+ languages with Pygments syntax highlighting, VS Code light theme, language labels |
| **Tables** | Auto-formatted Table Grid — bold header row, left/center/right alignment, inline math in cells |
| **Lists** | Bullet (•◦▪) and numbered lists, up to 6 nesting levels |
| **Other** | Blockquotes, horizontal rules, clickable hyperlinks, local images, footnotes |

## Quick Start

### Installation

```bash
# Using uv (recommended)
uv add markdocx

# Or using pip
pip install markdocx
```

<details>
<summary>Install from source (for development)</summary>

```bash
git clone https://github.com/shynerri-source/markdocx.git
cd markdocx
uv sync        # or: pip install -e .
```

</details>

### Usage

#### CLI

```bash
# Convert a single file
markdocx input.md
markdocx input.md -o output.docx

# Convert an entire directory
markdocx ./chapters/ -o ./output/

# Recursively search subdirectories
markdocx ./chapters/ -o ./output/ -r

# Verbose logging
markdocx input.md -v
```

#### Python API

```python
from markdocx import convert_file, convert_directory

# Single file
convert_file("input.md", "output.docx")

# Entire directory
results = convert_directory("./chapters/", output_dir="./output/", recursive=True)
```

### CLI Options

| Flag | Description |
|:-----|:------------|
| `input` | Markdown file or directory to convert |
| `-o, --output` | Output file or directory path |
| `-r, --recursive` | Recursively find `.md` files in subdirectories |
| `-v, --verbose` | Show detailed processing logs |

## How It Works

```
Markdown file
     │
     ▼
 md_parser.py        ─── markdown-it-py tokenizer
     │
     ▼
 docx_builder.py     ─── walks the token stream, builds Word elements
     ├── math_renderer.py   ─── LaTeX → MathML → OMML (native Word equations)
     ├── code_renderer.py   ─── Pygments lexer → colored Word runs
     └── styles.py          ─── fonts, colors, spacing presets
     │
     ▼
  .docx file          ─── python-docx output
```

### Math Pipeline

LaTeX is converted to **native OMML** (Office Math Markup Language), not images. This means formulas are editable, scale perfectly, and look like they were typed in Word's equation editor.

```
LaTeX string → latex2mathml → MathML → XSLT → OMML → Word paragraph
```

### Code Pipeline

```
Source code → Pygments lexer + VS Code theme → colored Word runs inside a shaded table cell
```

## Project Structure

```
markdocx/
├── main.py                  # Convenience entry point
├── pyproject.toml           # Project metadata & dependencies
├── src/
│   └── markdocx/            # Installable package
│       ├── __init__.py      # Public API (convert_file, convert_directory)
│       ├── cli.py           # CLI entry point (markdocx command)
│       ├── core.py          # Top-level orchestrator
│       ├── md_parser.py     # Markdown → token stream
│       ├── math_renderer.py # LaTeX → OMML (native Word math)
│       ├── code_renderer.py # Code → syntax-highlighted Word runs
│       ├── docx_builder.py  # Token stream → DOCX elements
│       └── styles.py        # Fonts, colors, and layout presets
└── rule/
    ├── ai_gen_doc_rule.md      # AI writing rules (Vietnamese)
    └── ai_gen_doc_rule_en.md   # AI writing rules (English)
```

## Dependencies

| Package | Version | Role |
|:--------|:--------|:-----|
| [python-docx](https://python-docx.readthedocs.io/) | 1.2.0 | DOCX generation |
| [markdown-it-py](https://github.com/executablebooks/markdown-it-py) | 4.0.0 | Markdown parsing |
| [mdit-py-plugins](https://github.com/executablebooks/mdit-py-plugins) | 0.5.0 | Math & footnote plugins |
| [latex2mathml](https://github.com/roniemartinez/latex2mathml) | 3.78.1 | LaTeX → MathML conversion |
| [lxml](https://lxml.de/) | 6.0.2 | XML/XSLT processing |
| [Pygments](https://pygments.org/) | 2.19.2 | Syntax highlighting |
| [matplotlib](https://matplotlib.org/) | 3.10.8 | LaTeX rendering (fallback) |
| [Pillow](https://python-pillow.org/) | 12.1.0 | Image processing |

## AI Writing Rules

The `rule/` directory contains detailed guidelines for prompting AI models to produce Markdown that converts cleanly:

| File | Language | Description |
|:-----|:---------|:------------|
| `rule/ai_gen_doc_rule.md` | Vietnamese | Full rule set — heading structure, LaTeX constraints, code block format, tables, etc. |
| `rule/ai_gen_doc_rule_en.md` | English | Same rules, English version |

**How to use:** Paste the contents of the appropriate rule file into your AI system prompt (or at the start of the conversation) before asking it to write textbook content.

## Contributing

Contributions are welcome. Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
