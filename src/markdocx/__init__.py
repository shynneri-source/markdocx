"""
markdocx
========
Convert AI-generated Markdown textbooks to polished DOCX
with native math equations and syntax-highlighted code.
"""

from markdocx.core import convert_file, convert_directory

__version__ = "10.0.2"
__all__ = ["convert_file", "convert_directory"]
