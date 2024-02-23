=========
Reference
=========

The `collapse` directive allows you to create collapsible content blocks in your documentation with an optional heading.

Syntax
------

.. code-block:: rst

  .. collapse:: <string>
    :class_name: <string>
    :open: <string>
    :icon: <string>

Options
-------

.. rst:directive:: .. collapse:: <heading>

  .. rst:directive:option:: class_name
    :type: string

    The HTML class name that wraps the ``collapse`` element.
    By default, this is ``sphinx_collapse``.

  .. rst:directive:option:: open
    :type: string

    If set, the collapsible block is expanded by default.

  .. rst:directive:option:: icon
    :type: string

    The HTML class name that defines the ``collapse`` icon.
    By default, this is set to ``sphinx_collapse_icon``.
    To specify multiple classes, separate the class names with a space, e.g. ``:icon: fa fa-caret-down``.
