sphinx-collapse
===============

``sphinx-collapse`` is a Sphinx extension that lets you add collapsible content to your documentation.

Collapsibles are useful to hide large amounts of content:

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-collapse/main/docs/source/_static/example.png

Features
--------

**Hide content**

Toggle the visibility of content with a Sphinx directive tailored for this purpose.

**Minimal code**

The library does not use JavaScript nor relies on third-party frameworks such as Bootstrap, Tailwind CSS, or Foundation.

**Configurable**

You can then customize the style of the collapsible directive using options or overriding the CSS.

Installation
------------

#. Install ``sphinx-collapse`` using PIP.

   .. code-block:: bash

      pip install sphinx-collapse


#. Add the extension to your Sphinx project ``conf.py`` file.

   .. code-block:: python

      extensions = ['sphinx_collapse']

Usage
-----

Using the directive:

.. code-block:: rst

   ..  collapse:: Click here

      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Renders:

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-collapse/main/docs/source/_static/example.png

Check out the full documentation for more customizable options at https://sphinx-collapse.readthedocs.io/

Contributing
------------

We encourage public contributions!
Please review `CONTRIBUTING <https://sphinx-collapse.readthedocs.io/en/latest/contribute.html>`_ for details on our code of conduct and development process.

Sponsors
--------

This project is sponsored by `Scylla <https://www.scylladb.com/>`_, The Real-Time Big Data Database.

License
-------

Copyright (c) 2022 - present David Garcia (`@dgarcia360 <https://twitter.com/dgarcia360>`_).

Licensed under the `MIT License <https://github.com/dgarcia360/sphinx-collapse/blob/main/LICENSE.md>`_.
