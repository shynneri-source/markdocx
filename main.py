#!/usr/bin/env python3
"""
Convenience entry point — delegates to markdocx.cli.main().

After installing the package (pip install -e .), you can also run:
    markdocx input.md -o output.docx
"""

from markdocx.cli import main

if __name__ == "__main__":
    main()
