"""
Tests for collapse extension.

(c) 2022 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

import subprocess
import sys
from pathlib import Path
from textwrap import dedent


def test_substitution_prompt(tmp_path: Path) -> None:
    """
    The ``collapse`` directive runs with no errors.
    """
    source_directory = tmp_path / "source"
    source_directory.mkdir()
    source_file = source_directory / "index.rst"
    conf_py = source_directory / "conf.py"
    conf_py.touch()
    source_file.touch()
    conf_py_content = dedent(
        """\
        extensions = ['sphinx_collapse']
        """,
    )
    conf_py.write_text(conf_py_content)
    source_file_content = dedent(
        """\
        .. collapse:: Heading

           Lorem ipsum
        """,
    )
    source_file.write_text(source_file_content)
    destination_directory = tmp_path / "destination"
    args = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        "-W",
        # Directory containing source and configuration files.
        str(source_directory),
        # Directory containing build files.
        str(destination_directory),
        # Source file to process.
        str(source_file),
    ]
    subprocess.check_output(args=args)
    expected = "Lorem ipsum"
    content_html = Path(str(destination_directory)) / "index.html"
    assert expected in content_html.read_text()
