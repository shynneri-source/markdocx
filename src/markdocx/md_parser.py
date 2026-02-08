"""
Markdown parser using markdown-it-py.
Phân tích cú pháp Markdown thành token stream.
"""

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.front_matter import front_matter_plugin


def create_parser():
    """
    Create a configured markdown-it-py parser with all necessary plugins.
    Supports: tables, strikethrough, math ($...$, $$...$$), footnotes.
    """
    md = MarkdownIt("commonmark", {"breaks": True, "html": True})

    # Enable built-in extensions
    md.enable("table")
    md.enable("strikethrough")

    # Enable math support: $inline$ and $$display$$
    md.use(dollarmath_plugin, double_inline=True)

    # Enable footnotes
    md.use(footnote_plugin)

    # Enable front matter (YAML)
    md.use(front_matter_plugin)

    return md


def parse_markdown(text):
    """
    Parse markdown text into a list of tokens.

    Args:
        text: Raw markdown string

    Returns:
        List of markdown-it Token objects
    """
    md = create_parser()
    tokens = md.parse(text)
    return tokens


def render_html(text):
    """
    Render markdown text to HTML (for debugging/preview).

    Args:
        text: Raw markdown string

    Returns:
        HTML string
    """
    md = create_parser()
    return md.render(text)
