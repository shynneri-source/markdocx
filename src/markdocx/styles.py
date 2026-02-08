"""
Document styles configuration.
Định nghĩa font, kích thước, màu sắc cho tài liệu giáo trình.
"""

from docx.shared import Pt, Inches, RGBColor, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


# ── Font Configuration ──────────────────────────────────────────────
FONT_BODY = "Times New Roman"
FONT_HEADING = "Arial"
FONT_CODE = "Consolas"

FONT_SIZE_BODY = Pt(12)
FONT_SIZE_CODE = Pt(9.5)
FONT_SIZE_CODE_BLOCK = Pt(9)
FONT_SIZE_SMALL = Pt(10)

# ── Heading Sizes ───────────────────────────────────────────────────
HEADING_SIZES = {
    1: Pt(22),
    2: Pt(18),
    3: Pt(15),
    4: Pt(13),
    5: Pt(12),
    6: Pt(11),
}

HEADING_COLORS = {
    1: RGBColor(0x1A, 0x23, 0x7E),    # Deep Blue
    2: RGBColor(0x28, 0x3E, 0x9A),    # Medium Blue
    3: RGBColor(0x37, 0x47, 0x4F),    # Dark Gray Blue
    4: RGBColor(0x45, 0x55, 0x60),    # Gray
    5: RGBColor(0x54, 0x64, 0x6E),    # Medium Gray
    6: RGBColor(0x60, 0x70, 0x7A),    # Light Gray
}

# ── Colors ──────────────────────────────────────────────────────────
COLOR_BODY_TEXT = RGBColor(0x21, 0x21, 0x21)
COLOR_LINK = RGBColor(0x05, 0x63, 0xC1)
COLOR_INLINE_CODE_BG = "E8E8E8"
COLOR_CODE_BLOCK_BG = "F8F8F8"
COLOR_CODE_BLOCK_BORDER = "DDDDDD"
COLOR_BLOCKQUOTE_BORDER = "BBBBBB"
COLOR_BLOCKQUOTE_TEXT = RGBColor(0x55, 0x55, 0x55)
COLOR_TABLE_HEADER_BG = "E3F2FD"
COLOR_TABLE_BORDER = "BBBBBB"
COLOR_HR = "CCCCCC"

# ── Spacing ─────────────────────────────────────────────────────────
LINE_SPACING = 1.15
PARA_SPACE_BEFORE = Pt(3)
PARA_SPACE_AFTER = Pt(6)
HEADING_SPACE_BEFORE = Pt(18)
HEADING_SPACE_AFTER = Pt(8)
CODE_BLOCK_SPACE = Pt(6)
LIST_INDENT = Inches(0.35)

# ── Page Setup ──────────────────────────────────────────────────────
PAGE_MARGIN_TOP = Cm(2.54)
PAGE_MARGIN_BOTTOM = Cm(2.54)
PAGE_MARGIN_LEFT = Cm(2.54)
PAGE_MARGIN_RIGHT = Cm(2.54)

# ── Math ────────────────────────────────────────────────────────────
MATH_DPI = 300
MATH_FONTSIZE_INLINE = 14
MATH_FONTSIZE_DISPLAY = 16
MATH_MAX_WIDTH = Inches(5.5)
MATH_INLINE_HEIGHT = Inches(0.22)

# ── Code Syntax Colors (VS Code-like theme) ────────────────────────
from pygments.token import Token

SYNTAX_COLORS = {
    Token.Keyword:                  RGBColor(0x00, 0x00, 0xCC),     # Blue
    Token.Keyword.Constant:         RGBColor(0x00, 0x00, 0xCC),
    Token.Keyword.Declaration:      RGBColor(0x00, 0x00, 0xCC),
    Token.Keyword.Namespace:        RGBColor(0x7B, 0x30, 0x7B),     # Purple
    Token.Keyword.Type:             RGBColor(0x26, 0x7F, 0x99),     # Teal
    Token.Name.Function:            RGBColor(0x79, 0x5E, 0x26),     # Dark Yellow
    Token.Name.Function.Magic:      RGBColor(0x79, 0x5E, 0x26),
    Token.Name.Class:               RGBColor(0x26, 0x7F, 0x99),     # Teal
    Token.Name.Decorator:           RGBColor(0x79, 0x5E, 0x26),     # Dark Yellow
    Token.Name.Builtin:             RGBColor(0x26, 0x7F, 0x99),     # Teal
    Token.Name.Builtin.Pseudo:      RGBColor(0x00, 0x00, 0xCC),
    Token.Literal.String:           RGBColor(0xA3, 0x15, 0x15),     # Red
    Token.Literal.String.Doc:       RGBColor(0xA3, 0x15, 0x15),
    Token.Literal.String.Single:    RGBColor(0xA3, 0x15, 0x15),
    Token.Literal.String.Double:    RGBColor(0xA3, 0x15, 0x15),
    Token.Literal.String.Escape:    RGBColor(0xEE, 0x00, 0x00),
    Token.Literal.String.Interpol:  RGBColor(0xEE, 0x00, 0x00),
    Token.Literal.String.Affix:     RGBColor(0x00, 0x00, 0xCC),
    Token.Literal.Number:           RGBColor(0x09, 0x88, 0x58),     # Green
    Token.Literal.Number.Integer:   RGBColor(0x09, 0x88, 0x58),
    Token.Literal.Number.Float:     RGBColor(0x09, 0x88, 0x58),
    Token.Comment:                  RGBColor(0x6A, 0x99, 0x55),     # Olive Green
    Token.Comment.Single:           RGBColor(0x6A, 0x99, 0x55),
    Token.Comment.Multiline:        RGBColor(0x6A, 0x99, 0x55),
    Token.Comment.Hashbang:         RGBColor(0x6A, 0x99, 0x55),
    Token.Operator:                 RGBColor(0x33, 0x33, 0x33),
    Token.Operator.Word:            RGBColor(0x00, 0x00, 0xCC),
    Token.Punctuation:              RGBColor(0x33, 0x33, 0x33),
    Token.Name.Tag:                 RGBColor(0x80, 0x00, 0x00),     # HTML tags
    Token.Name.Attribute:           RGBColor(0xFF, 0x00, 0x00),     # HTML attrs
}


def get_syntax_color(token_type):
    """Get color for a Pygments token type, walking up the hierarchy."""
    t = token_type
    while t:
        if t in SYNTAX_COLORS:
            return SYNTAX_COLORS[t]
        t = t.parent
    return None


# ── XML Helpers ─────────────────────────────────────────────────────

def set_paragraph_shading(paragraph, fill_color):
    """Set background color for an entire paragraph."""
    pPr = paragraph._element.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_color)
    pPr.append(shd)


def set_paragraph_borders(paragraph, color="CCCCCC", size="4", space="4"):
    """Add borders around a paragraph."""
    pPr = paragraph._element.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        border = OxmlElement(f"w:{side}")
        border.set(qn("w:val"), "single")
        border.set(qn("w:sz"), size)
        border.set(qn("w:space"), space)
        border.set(qn("w:color"), color)
        pBdr.append(border)
    pPr.append(pBdr)


def set_run_shading(run, fill_color):
    """Set background highlight for a run (inline code)."""
    rPr = run._element.get_or_add_rPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_color)
    rPr.append(shd)


def set_blockquote_style(paragraph, depth=1):
    """Style a paragraph as a blockquote with left border."""
    paragraph.paragraph_format.left_indent = Inches(0.4 * depth)
    pPr = paragraph._element.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "18")
    left.set(qn("w:space"), "8")
    left.set(qn("w:color"), COLOR_BLOCKQUOTE_BORDER)
    pBdr.append(left)
    pPr.append(pBdr)


def add_horizontal_rule(doc):
    """Add a horizontal rule to the document."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(8)
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), COLOR_HR)
    pBdr.append(bottom)
    pPr.append(pBdr)


def set_table_header_shading(cell, fill_color=COLOR_TABLE_HEADER_BG):
    """Set background color for a table header cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill_color)
    tcPr.append(shd)


def setup_document_styles(doc):
    """Configure the document with standard page setup and styles."""
    # Page margins
    for section in doc.sections:
        section.top_margin = PAGE_MARGIN_TOP
        section.bottom_margin = PAGE_MARGIN_BOTTOM
        section.left_margin = PAGE_MARGIN_LEFT
        section.right_margin = PAGE_MARGIN_RIGHT

    # Default paragraph style
    style = doc.styles["Normal"]
    font = style.font
    font.name = FONT_BODY
    font.size = FONT_SIZE_BODY
    font.color.rgb = COLOR_BODY_TEXT
    pf = style.paragraph_format
    pf.space_before = PARA_SPACE_BEFORE
    pf.space_after = PARA_SPACE_AFTER
    pf.line_spacing = LINE_SPACING

    # Set East Asian font for Normal style
    rPr = style._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    rFonts.set(qn("w:eastAsia"), FONT_BODY)

    # Heading styles
    for level in range(1, 7):
        style_name = f"Heading {level}"
        if style_name in doc.styles:
            h_style = doc.styles[style_name]
            h_font = h_style.font
            h_font.name = FONT_HEADING
            h_font.size = HEADING_SIZES.get(level, Pt(11))
            h_font.color.rgb = HEADING_COLORS.get(level, COLOR_BODY_TEXT)
            h_font.bold = True
            h_pf = h_style.paragraph_format
            h_pf.space_before = HEADING_SPACE_BEFORE
            h_pf.space_after = HEADING_SPACE_AFTER
            h_pf.keep_with_next = True

            # East Asian font
            h_rPr = h_style._element.get_or_add_rPr()
            h_rFonts = h_rPr.find(qn("w:rFonts"))
            if h_rFonts is None:
                h_rFonts = OxmlElement("w:rFonts")
                h_rPr.insert(0, h_rFonts)
            h_rFonts.set(qn("w:eastAsia"), FONT_HEADING)
