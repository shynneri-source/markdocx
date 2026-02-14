"""
Math formula renderer.
Chuyển đổi công thức LaTeX thành OMML (Office Math Markup Language)
để hiển thị native trong Word. Sử dụng latex2mathml + XSLT.
"""

import logging
import re
from lxml import etree

import latex2mathml.converter

logger = logging.getLogger(__name__)

# ── XSLT stylesheet to convert MathML → OMML ───────────────────────
# Microsoft's MML2OMML transformation (minimal embedded version)
# We load it once at module level for performance.
_OMML_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
_MATHML_NS = "http://www.w3.org/1998/Math/MathML"


def _clean_latex(latex_str):
    """
    Clean/normalize LaTeX string for latex2mathml compatibility.
    """
    s = latex_str.strip()

    # Normalize common shortcuts
    s = s.replace(r"\R", r"\mathbb{R}")
    s = s.replace(r"\N", r"\mathbb{N}")
    s = s.replace(r"\Z", r"\mathbb{Z}")
    s = s.replace(r"\Q", r"\mathbb{Q}")
    s = s.replace(r"\C", r"\mathbb{C}")

    return s


def latex_to_mathml(latex_str):
    """
    Convert LaTeX math string to MathML XML string.

    Args:
        latex_str: LaTeX math expression (without $ delimiters)

    Returns:
        MathML XML string, or None on failure
    """
    if not latex_str or not latex_str.strip():
        return None

    cleaned = _clean_latex(latex_str)

    try:
        mathml = latex2mathml.converter.convert(cleaned)
        return mathml
    except Exception as e:
        logger.warning(f"latex2mathml failed for: {latex_str!r} → {e}")
        return None


def _mathml_to_omml(mathml_str):
    """
    Convert MathML XML string to OMML (Office Math Markup Language) element.
    Uses a direct conversion approach since lxml XSLT with Microsoft's
    MML2OMML.xsl requires the full file.

    We use a simplified but robust recursive converter.
    """
    try:
        # Parse the MathML
        # latex2mathml output may have namespace declaration
        if 'xmlns' not in mathml_str:
            mathml_str = mathml_str.replace('<math>', f'<math xmlns="{_MATHML_NS}">')

        root = etree.fromstring(mathml_str.encode('utf-8'))
        # Build OMML
        omml = _convert_mathml_element(root)
        return omml
    except Exception as e:
        logger.warning(f"MathML→OMML conversion failed: {e}")
        return None


def _make_omml(tag, text=None):
    """Create an OMML element with optional text."""
    el = etree.SubElement(etree.Element("dummy"), f"{{{_OMML_NS}}}{tag}")
    el = etree.Element(f"{{{_OMML_NS}}}{tag}")
    if text is not None:
        el.text = text
    return el


def _omml_run(text):
    """Create an OMML run <m:r> containing <m:t>text</m:t>."""
    r = etree.Element(f"{{{_OMML_NS}}}r")
    t = etree.SubElement(r, f"{{{_OMML_NS}}}t")
    t.text = text
    return r


def _append_flattened(parent, child):
    """Append child to parent, flattening nested oMath groups.
    
    Word doesn't support nested m:oMath inside m:oMath.
    When a child is itself an oMath group (used as container for mrow etc.),
    we flatten it by appending its children directly to the parent.
    """
    if _local(child.tag) == "oMath" and _local(parent.tag) == "oMath":
        for sub in list(child):
            parent.append(sub)
    else:
        parent.append(child)


def _local(tag):
    """Strip namespace from tag."""
    if '}' in tag:
        return tag.split('}', 1)[1]
    return tag


def _convert_mathml_element(elem):
    """
    Recursively convert a MathML element tree to OMML element tree.
    Supports: mrow, mi, mn, mo, mfrac, msqrt, mroot, msup, msub,
    msubsup, mover, munder, munderover, mtable, mtr, mtd, mtext,
    mfenced (pmatrix, bmatrix, cases, vmatrix...), mspace.
    """
    tag = _local(elem.tag)

    if tag == "math":
        omath = etree.Element(f"{{{_OMML_NS}}}oMath")
        for child in elem:
            result = _convert_mathml_element(child)
            if result is not None:
                _append_flattened(omath, result)
        return omath

    elif tag == "mrow":
        # Detect matrix pattern: mo(delimiter) + mtable + mo(delimiter)
        # latex2mathml produces this for pmatrix, bmatrix, vmatrix, etc.
        children = list(elem)
        child_tags = [_local(c.tag) for c in children]

        # Pattern 1: mo + mtable + mo  (pmatrix, bmatrix, vmatrix, Bmatrix, Vmatrix)
        if child_tags == ["mo", "mtable", "mo"]:
            open_delim = _get_text(children[0]) or "("
            close_delim = _get_text(children[2]) or ")"
            d = etree.Element(f"{{{_OMML_NS}}}d")
            dPr = etree.SubElement(d, f"{{{_OMML_NS}}}dPr")
            begChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}begChr")
            begChr.set(f"{{{_OMML_NS}}}val", open_delim)
            endChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}endChr")
            endChr.set(f"{{{_OMML_NS}}}val", close_delim)
            e_elem = etree.SubElement(d, f"{{{_OMML_NS}}}e")
            mtable_omml = _convert_mathml_element(children[1])
            if mtable_omml is not None:
                e_elem.append(mtable_omml)
            return d

        # Pattern 2: mo + mtable  (cases — only opening delimiter)
        if child_tags == ["mo", "mtable"]:
            open_delim = _get_text(children[0]) or "{"
            d = etree.Element(f"{{{_OMML_NS}}}d")
            dPr = etree.SubElement(d, f"{{{_OMML_NS}}}dPr")
            begChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}begChr")
            begChr.set(f"{{{_OMML_NS}}}val", open_delim)
            endChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}endChr")
            endChr.set(f"{{{_OMML_NS}}}val", "")
            e_elem = etree.SubElement(d, f"{{{_OMML_NS}}}e")
            mtable_omml = _convert_mathml_element(children[1])
            if mtable_omml is not None:
                e_elem.append(mtable_omml)
            return d

        # Pattern 3: mixed content containing mo + mtable (e.g. I = (matrix))
        # Detect mtable surrounded by mo delimiters within a larger mrow
        mtable_idx = None
        for i, t in enumerate(child_tags):
            if t == "mtable":
                mtable_idx = i
                break

        if mtable_idx is not None:
            # Check for delimiter mo before and/or after the mtable
            has_open = (mtable_idx > 0 and child_tags[mtable_idx - 1] == "mo")
            has_close = (mtable_idx < len(child_tags) - 1 and child_tags[mtable_idx + 1] == "mo")

            if has_open or has_close:
                group = etree.Element(f"{{{_OMML_NS}}}oMath")
                # Convert children before the opening delimiter
                start = (mtable_idx - 1) if has_open else mtable_idx
                for child in children[:start]:
                    result = _convert_mathml_element(child)
                    if result is not None:
                        _append_flattened(group, result)

                # Build the delimiter-wrapped matrix
                open_delim = _get_text(children[mtable_idx - 1]) if has_open else ""
                close_delim = _get_text(children[mtable_idx + 1]) if has_close else ""

                d = etree.Element(f"{{{_OMML_NS}}}d")
                dPr = etree.SubElement(d, f"{{{_OMML_NS}}}dPr")
                begChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}begChr")
                begChr.set(f"{{{_OMML_NS}}}val", open_delim or "")
                endChr_el = etree.SubElement(dPr, f"{{{_OMML_NS}}}endChr")
                endChr_el.set(f"{{{_OMML_NS}}}val", close_delim or "")
                e_elem = etree.SubElement(d, f"{{{_OMML_NS}}}e")
                mtable_omml = _convert_mathml_element(children[mtable_idx])
                if mtable_omml is not None:
                    e_elem.append(mtable_omml)
                group.append(d)

                # Convert children after the closing delimiter
                end = (mtable_idx + 2) if has_close else (mtable_idx + 1)
                for child in children[end:]:
                    result = _convert_mathml_element(child)
                    if result is not None:
                        _append_flattened(group, result)
                return group

        # Default: group — just convert children sequentially
        group = etree.Element(f"{{{_OMML_NS}}}oMath")
        for child in children:
            result = _convert_mathml_element(child)
            if result is not None:
                _append_flattened(group, result)
        return group

    elif tag in ("mi", "mn", "mo", "mtext"):
        text = (elem.text or "").strip()
        if not text:
            return None
        r = etree.Element(f"{{{_OMML_NS}}}r")
        # Mark identifier styling
        if tag == "mi" and len(text) == 1:
            rPr = etree.SubElement(r, f"{{{_OMML_NS}}}rPr")
            sty = etree.SubElement(rPr, f"{{{_OMML_NS}}}sty")
            sty.set(f"{{{_OMML_NS}}}val", "p" if text.isdigit() else "i")
        t = etree.SubElement(r, f"{{{_OMML_NS}}}t")
        t.text = text
        return r

    elif tag == "mfrac":
        children = list(elem)
        if len(children) < 2:
            return None
        f = etree.Element(f"{{{_OMML_NS}}}f")
        fPr = etree.SubElement(f, f"{{{_OMML_NS}}}fPr")
        # Check for line (displaystyle fraction vs inline)
        if elem.get("linethickness") == "0":
            type_el = etree.SubElement(fPr, f"{{{_OMML_NS}}}type")
            type_el.set(f"{{{_OMML_NS}}}val", "noBar")

        num = etree.SubElement(f, f"{{{_OMML_NS}}}num")
        num_content = _convert_mathml_element(children[0])
        if num_content is not None:
            num.append(num_content)

        den = etree.SubElement(f, f"{{{_OMML_NS}}}den")
        den_content = _convert_mathml_element(children[1])
        if den_content is not None:
            den.append(den_content)
        return f

    elif tag == "msqrt":
        rad = etree.Element(f"{{{_OMML_NS}}}rad")
        radPr = etree.SubElement(rad, f"{{{_OMML_NS}}}radPr")
        degHide = etree.SubElement(radPr, f"{{{_OMML_NS}}}degHide")
        degHide.set(f"{{{_OMML_NS}}}val", "1")
        deg = etree.SubElement(rad, f"{{{_OMML_NS}}}deg")
        e_elem = etree.SubElement(rad, f"{{{_OMML_NS}}}e")
        for child in elem:
            result = _convert_mathml_element(child)
            if result is not None:
                e_elem.append(result)
        return rad

    elif tag == "mroot":
        children = list(elem)
        rad = etree.Element(f"{{{_OMML_NS}}}rad")
        radPr = etree.SubElement(rad, f"{{{_OMML_NS}}}radPr")
        deg = etree.SubElement(rad, f"{{{_OMML_NS}}}deg")
        if len(children) > 1:
            deg_content = _convert_mathml_element(children[1])
            if deg_content is not None:
                deg.append(deg_content)
        e_elem = etree.SubElement(rad, f"{{{_OMML_NS}}}e")
        if children:
            base_content = _convert_mathml_element(children[0])
            if base_content is not None:
                e_elem.append(base_content)
        return rad

    elif tag == "msup":
        children = list(elem)
        if len(children) < 2:
            return None
        sSup = etree.Element(f"{{{_OMML_NS}}}sSup")
        e_elem = etree.SubElement(sSup, f"{{{_OMML_NS}}}e")
        base = _convert_mathml_element(children[0])
        if base is not None:
            e_elem.append(base)
        sup = etree.SubElement(sSup, f"{{{_OMML_NS}}}sup")
        sup_content = _convert_mathml_element(children[1])
        if sup_content is not None:
            sup.append(sup_content)
        return sSup

    elif tag == "msub":
        children = list(elem)
        if len(children) < 2:
            return None
        sSub = etree.Element(f"{{{_OMML_NS}}}sSub")
        e_elem = etree.SubElement(sSub, f"{{{_OMML_NS}}}e")
        base = _convert_mathml_element(children[0])
        if base is not None:
            e_elem.append(base)
        sub = etree.SubElement(sSub, f"{{{_OMML_NS}}}sub")
        sub_content = _convert_mathml_element(children[1])
        if sub_content is not None:
            sub.append(sub_content)
        return sSub

    elif tag == "msubsup":
        children = list(elem)
        if len(children) < 3:
            return None
        sSubSup = etree.Element(f"{{{_OMML_NS}}}sSubSup")
        e_elem = etree.SubElement(sSubSup, f"{{{_OMML_NS}}}e")
        base = _convert_mathml_element(children[0])
        if base is not None:
            e_elem.append(base)
        sub = etree.SubElement(sSubSup, f"{{{_OMML_NS}}}sub")
        sub_c = _convert_mathml_element(children[1])
        if sub_c is not None:
            sub.append(sub_c)
        sup = etree.SubElement(sSubSup, f"{{{_OMML_NS}}}sup")
        sup_c = _convert_mathml_element(children[2])
        if sup_c is not None:
            sup.append(sup_c)
        return sSubSup

    elif tag == "mover":
        children = list(elem)
        if len(children) < 2:
            return None
        # Check if the "over" is an accent (hat, bar, vec, etc.)
        acc = etree.Element(f"{{{_OMML_NS}}}acc")
        accPr = etree.SubElement(acc, f"{{{_OMML_NS}}}accPr")
        # Get the accent character
        over_text = _get_text(children[1])
        if over_text:
            chr_el = etree.SubElement(accPr, f"{{{_OMML_NS}}}chr")
            chr_el.set(f"{{{_OMML_NS}}}val", over_text)
        e_elem = etree.SubElement(acc, f"{{{_OMML_NS}}}e")
        base = _convert_mathml_element(children[0])
        if base is not None:
            e_elem.append(base)
        return acc

    elif tag == "munder":
        children = list(elem)
        if len(children) < 2:
            return None
        # Use limLow for underscript
        limLow = etree.Element(f"{{{_OMML_NS}}}limLow")
        e_elem = etree.SubElement(limLow, f"{{{_OMML_NS}}}e")
        base = _convert_mathml_element(children[0])
        if base is not None:
            e_elem.append(base)
        lim = etree.SubElement(limLow, f"{{{_OMML_NS}}}lim")
        lim_c = _convert_mathml_element(children[1])
        if lim_c is not None:
            lim.append(lim_c)
        return limLow

    elif tag == "munderover":
        children = list(elem)
        if len(children) < 3:
            return None
        # nary (summation, product, integral, etc.) or limLow+sup
        base_text = _get_text(children[0])
        nary_chars = {"∑", "∏", "∫", "∬", "∭", "⋃", "⋂", "⋁", "⋀"}
        if base_text in nary_chars:
            nary = etree.Element(f"{{{_OMML_NS}}}nary")
            naryPr = etree.SubElement(nary, f"{{{_OMML_NS}}}naryPr")
            chr_el = etree.SubElement(naryPr, f"{{{_OMML_NS}}}chr")
            chr_el.set(f"{{{_OMML_NS}}}val", base_text)
            sub = etree.SubElement(nary, f"{{{_OMML_NS}}}sub")
            sub_c = _convert_mathml_element(children[1])
            if sub_c is not None:
                sub.append(sub_c)
            sup = etree.SubElement(nary, f"{{{_OMML_NS}}}sup")
            sup_c = _convert_mathml_element(children[2])
            if sup_c is not None:
                sup.append(sup_c)
            e_elem = etree.SubElement(nary, f"{{{_OMML_NS}}}e")
            return nary
        else:
            # Generic: use limLow then wrap in sSup
            limLow = etree.Element(f"{{{_OMML_NS}}}limLow")
            e_elem = etree.SubElement(limLow, f"{{{_OMML_NS}}}e")
            base = _convert_mathml_element(children[0])
            if base is not None:
                e_elem.append(base)
            lim = etree.SubElement(limLow, f"{{{_OMML_NS}}}lim")
            lim_c = _convert_mathml_element(children[1])
            if lim_c is not None:
                lim.append(lim_c)
            # Wrap in sSup for the overscript
            sSup = etree.Element(f"{{{_OMML_NS}}}sSup")
            e2 = etree.SubElement(sSup, f"{{{_OMML_NS}}}e")
            e2.append(limLow)
            sup = etree.SubElement(sSup, f"{{{_OMML_NS}}}sup")
            sup_c = _convert_mathml_element(children[2])
            if sup_c is not None:
                sup.append(sup_c)
            return sSup

    elif tag == "mfenced":
        # Delimiters: parentheses, brackets, braces, cases, etc.
        open_delim = elem.get("open", "(")
        close_delim = elem.get("close", ")")
        separators = elem.get("separators", ",")

        d = etree.Element(f"{{{_OMML_NS}}}d")
        dPr = etree.SubElement(d, f"{{{_OMML_NS}}}dPr")
        if open_delim:
            begChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}begChr")
            begChr.set(f"{{{_OMML_NS}}}val", open_delim)
        if close_delim:
            endChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}endChr")
            endChr.set(f"{{{_OMML_NS}}}val", close_delim)
        if separators:
            sepChr = etree.SubElement(dPr, f"{{{_OMML_NS}}}sepChr")
            sepChr.set(f"{{{_OMML_NS}}}val", separators.strip()[0] if separators.strip() else "")

        for child in elem:
            e_elem = etree.SubElement(d, f"{{{_OMML_NS}}}e")
            result = _convert_mathml_element(child)
            if result is not None:
                e_elem.append(result)
        return d

    elif tag == "mtable":
        # Matrix/table
        m = etree.Element(f"{{{_OMML_NS}}}m")
        mPr = etree.SubElement(m, f"{{{_OMML_NS}}}mPr")
        # Count columns from first row
        first_row = elem.find(f"{{{_MATHML_NS}}}mtr")
        if first_row is None:
            first_row = elem.find("mtr")
        if first_row is not None:
            num_cols = len(list(first_row))
            mcs = etree.SubElement(mPr, f"{{{_OMML_NS}}}mcs")
            mc = etree.SubElement(mcs, f"{{{_OMML_NS}}}mc")
            mcPr = etree.SubElement(mc, f"{{{_OMML_NS}}}mcPr")
            count = etree.SubElement(mcPr, f"{{{_OMML_NS}}}count")
            count.set(f"{{{_OMML_NS}}}val", str(num_cols))
            mcJc = etree.SubElement(mcPr, f"{{{_OMML_NS}}}mcJc")
            mcJc.set(f"{{{_OMML_NS}}}val", "center")

        for row_elem in elem:
            if _local(row_elem.tag) == "mtr":
                mr = etree.SubElement(m, f"{{{_OMML_NS}}}mr")
                for cell_elem in row_elem:
                    if _local(cell_elem.tag) == "mtd":
                        e_elem = etree.SubElement(mr, f"{{{_OMML_NS}}}e")
                        for cell_child in cell_elem:
                            result = _convert_mathml_element(cell_child)
                            if result is not None:
                                _append_flattened(e_elem, result)
                        # If mtd has direct text
                        if cell_elem.text and cell_elem.text.strip():
                            e_elem.append(_omml_run(cell_elem.text.strip()))
        return m

    elif tag == "mspace":
        return _omml_run("\u2003")  # em space

    elif tag == "mpadded":
        # Just process children
        group = etree.Element(f"{{{_OMML_NS}}}oMath")
        for child in elem:
            result = _convert_mathml_element(child)
            if result is not None:
                _append_flattened(group, result)
        return group

    elif tag == "mstyle":
        # Just process children (ignore style attrs for now)
        group = etree.Element(f"{{{_OMML_NS}}}oMath")
        for child in elem:
            result = _convert_mathml_element(child)
            if result is not None:
                _append_flattened(group, result)
        return group

    elif tag == "menclose":
        # Treat as grouping
        group = etree.Element(f"{{{_OMML_NS}}}oMath")
        for child in elem:
            result = _convert_mathml_element(child)
            if result is not None:
                _append_flattened(group, result)
        return group

    else:
        # Unknown tag — try to process children or text
        if elem.text and elem.text.strip():
            return _omml_run(elem.text.strip())
        group = etree.Element(f"{{{_OMML_NS}}}oMath")
        for child in elem:
            result = _convert_mathml_element(child)
            if result is not None:
                _append_flattened(group, result)
        if len(group):
            return group
        return None


def _get_text(elem):
    """Get all text content from a MathML element recursively."""
    texts = []
    if elem.text:
        texts.append(elem.text)
    for child in elem:
        texts.append(_get_text(child))
        if child.tail:
            texts.append(child.tail)
    return "".join(texts).strip()


def latex_to_omml(latex_str):
    """
    Convert LaTeX math to an OMML element that can be inserted into a DOCX paragraph.

    Args:
        latex_str: LaTeX math expression (without $ delimiters)

    Returns:
        lxml Element (OMML oMath), or None on failure
    """
    mathml = latex_to_mathml(latex_str)
    if mathml is None:
        return None

    omml = _mathml_to_omml(mathml)
    return omml


def latex_to_omml_para(latex_str):
    """
    Convert LaTeX math to an OMML oMathPara element (for display/block math).

    Args:
        latex_str: LaTeX math expression

    Returns:
        lxml Element (OMML oMathPara), or None on failure
    """
    omath = latex_to_omml(latex_str)
    if omath is None:
        return None

    # Wrap in oMathPara for block display
    oMathPara = etree.Element(f"{{{_OMML_NS}}}oMathPara")
    oMathPara.append(omath)
    return oMathPara
