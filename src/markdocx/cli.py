#!/usr/bin/env python3
"""
markdocx — CLI Entry Point
===========================
Convert Markdown textbooks to polished DOCX with native
math equations and syntax-highlighted code.

Usage:
    markdocx input.md                     # Convert single file
    markdocx input.md -o output.docx      # Specify output path
    markdocx ./docs/                       # Convert all .md in directory
    markdocx ./docs/ -r -o ./output/       # Recursive + output dir
"""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="markdocx",
        description="Convert Markdown textbooks to DOCX "
                    "(math equations, code syntax highlighting, tables, images...)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  markdocx chapter1.md
  markdocx chapter1.md -o bai1.docx
  markdocx ./chapters/ -o ./output/ -r
  markdocx ./chapters/ -r -v
        """,
    )

    parser.add_argument(
        "input",
        help="Markdown file or directory containing .md files to convert",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output .docx file path (or directory if input is a directory)",
        default=None,
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Recursively find .md files in subdirectories",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed processing logs",
    )

    args = parser.parse_args()

    # Lazy import to speed up --help
    from markdocx.core import convert_file, convert_directory

    input_path = os.path.abspath(args.input)

    try:
        if os.path.isfile(input_path):
            # ── Convert single file ──
            if not input_path.lower().endswith(".md"):
                print(f"Error: Expected a .md file, got: {input_path}", file=sys.stderr)
                sys.exit(1)

            output = convert_file(input_path, args.output, verbose=args.verbose)
            print(f"\nDone: {output}")

        elif os.path.isdir(input_path):
            # ── Convert directory ──
            results = convert_directory(
                input_path,
                output_dir=args.output,
                recursive=args.recursive,
                verbose=args.verbose,
            )

            if not results:
                print("No .md files found.", file=sys.stderr)
                sys.exit(1)

            print("\n" + "=" * 60)
            print("CONVERSION RESULTS")
            print("=" * 60)
            for md_path, docx_path, success, error in results:
                status = "OK" if success else "FAIL"
                name = os.path.basename(md_path)
                if success:
                    print(f"  [{status}] {name} -> {os.path.basename(docx_path)}")
                else:
                    print(f"  [{status}] {name} — Error: {error}")

            success_count = sum(1 for *_, ok, _ in results if ok)
            fail_count = len(results) - success_count
            print(f"\nTotal: {success_count} succeeded, {fail_count} failed")

        else:
            print(f"Error: Invalid path: {input_path}", file=sys.stderr)
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nCancelled by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
