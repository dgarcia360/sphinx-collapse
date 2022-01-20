"""
Collapse extension for Sphinx.

(c) 2022 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

from pathlib import Path
from uuid import uuid4

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective

__version__ = "0.1.1"


class _HTMLElement(nodes.Element, nodes.General):
    """
    Generic HTML element
    Adapted from https://github.com/pradyunsg/sphinx-inline-tabs
    """

    @staticmethod
    def visit(translator, node):
        attributes = node.attributes.copy()

        # Not necessary
        attributes.pop("ids")
        attributes.pop("classes")
        attributes.pop("names")
        attributes.pop("dupnames")
        attributes.pop("backrefs")

        text = translator.starttag(node, node.tagname, **attributes)
        translator.body.append(text.strip())

    @staticmethod
    def depart(translator, node):
        if node.endtag:
            translator.body.append(f"</{node.tagname}>")


class _HTMLLabel(_HTMLElement):
    """
    Label HTML element
    """

    tagname = "label"
    endtag = True


class _HTMLIcon(_HTMLElement):
    """
    Icon HTML element
    """

    tagname = "i"
    endtag = True


class _HTMLInput(_HTMLElement):
    """
    Input HTML element
    """

    tagname = "input"
    endtag = False


class CollapseDirective(SphinxDirective):
    """
    Collapse directive
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {"class_name": directives.unchanged, "icon": directives.unchanged}

    def run(self):

        self.assert_has_content()

        class_name = self.options.get("class_name", "sphinx_collapse")
        collapse_id = str(uuid4())

        # container
        container_class_name = class_name
        container = nodes.container(
            "",
            id=collapse_id,
            is_div=True,
            classes=[container_class_name],
        )

        # input
        input_class_name = class_name + "__input"
        custom_input = _HTMLInput(
            type="checkbox",
            ids=[collapse_id],
            name=collapse_id,
            classes=[input_class_name],
        )

        # icon
        icon_class_name = self.options.get("icon", class_name + "__icon")
        icon = _HTMLIcon(classes=[icon_class_name])

        # label
        label_class_name = class_name + "__label"
        label = _HTMLLabel(
            **{"for": collapse_id},
            classes=[label_class_name],
        )
        text = self.arguments[0].strip()

        label += icon
        label += nodes.Text(text, text)

        # content
        content_class_name = class_name + "__content"
        content = nodes.container(
            "",
            is_div=True,
            classes=[content_class_name],
        )
        self.state.nested_parse(self.content, self.content_offset, content)

        container += custom_input
        container += label
        container += content

        return [container]


def setup(app: Sphinx) -> dict:
    """
    Loads collapse directive
    """

    # Add CSS
    static_dir = str(Path(__file__).parent.joinpath("_static").absolute())
    app.connect(
        "builder-inited", (lambda app: app.config.html_static_path.append(static_dir))
    )
    app.add_css_file("sphinx_collapse.css")
    # Add custom nodes
    app.add_node(
        _HTMLIcon,
        html=(_HTMLIcon.visit, _HTMLIcon.depart),
    )
    app.add_node(
        _HTMLLabel,
        html=(_HTMLLabel.visit, _HTMLLabel.depart),
    )
    app.add_node(
        _HTMLInput,
        html=(_HTMLInput.visit, _HTMLInput.depart),
    )
    # Add directive
    app.add_directive("collapse", CollapseDirective)
