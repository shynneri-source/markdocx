"""
Core conversion orchestrator.
Điều phối quá trình chuyển đổi từ Markdown sang DOCX.
"""

import os
import glob
import logging
import time

from markdocx.md_parser import parse_markdown
from markdocx.docx_builder import DocxBuilder

logger = logging.getLogger(__name__)


def convert_file(input_path, output_path=None, verbose=False):
    """
    Convert a single Markdown file to DOCX.

    Args:
        input_path: Path to the .md file
        output_path: Path for the output .docx file (auto-generated if None)
        verbose: Enable verbose logging

    Returns:
        Path to the output .docx file

    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If input is not a .md file
    """
    _setup_logging(verbose)

    input_path = os.path.abspath(input_path)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    if not input_path.lower().endswith(".md"):
        raise ValueError(f"Expected a .md file, got: {input_path}")

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".docx"
    output_path = os.path.abspath(output_path)

    logger.info(f"Converting: {input_path}")
    start = time.time()

    # Read markdown
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Parse
    tokens = parse_markdown(md_text)
    logger.info(f"  Parsed {len(tokens)} tokens")

    # Build DOCX
    base_dir = os.path.dirname(input_path)
    builder = DocxBuilder(base_dir=base_dir)
    builder.build(tokens, output_path)

    elapsed = time.time() - start
    logger.info(f"  Done in {elapsed:.2f}s → {output_path}")

    return output_path


def convert_directory(input_dir, output_dir=None, recursive=False, verbose=False):
    """
    Convert all Markdown files in a directory to DOCX.

    Args:
        input_dir: Path to the directory containing .md files
        output_dir: Path for output .docx files (uses input_dir if None)
        recursive: Search for .md files recursively
        verbose: Enable verbose logging

    Returns:
        List of (input_path, output_path, success, error) tuples
    """
    _setup_logging(verbose)

    input_dir = os.path.abspath(input_dir)
    if not os.path.isdir(input_dir):
        raise NotADirectoryError(f"Not a directory: {input_dir}")

    if output_dir is None:
        output_dir = input_dir
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # Find markdown files
    pattern = os.path.join(input_dir, "**", "*.md") if recursive else os.path.join(input_dir, "*.md")
    md_files = sorted(glob.glob(pattern, recursive=recursive))

    if not md_files:
        logger.warning(f"No .md files found in: {input_dir}")
        return []

    logger.info(f"Found {len(md_files)} markdown file(s)")

    results = []
    for md_file in md_files:
        # Compute output path preserving relative structure
        rel_path = os.path.relpath(md_file, input_dir)
        out_path = os.path.join(output_dir, os.path.splitext(rel_path)[0] + ".docx")

        try:
            convert_file(md_file, out_path, verbose=verbose)
            results.append((md_file, out_path, True, None))
        except Exception as e:
            logger.error(f"Failed to convert {md_file}: {e}")
            results.append((md_file, out_path, False, str(e)))

    # Summary
    success = sum(1 for *_, ok, _ in results if ok)
    failed = len(results) - success
    logger.info(f"\nConversion complete: {success} succeeded, {failed} failed")

    return results


def _setup_logging(verbose=False):
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )
