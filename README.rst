About
-----

This is a simple plugin that runs::

    python setup.py build_ext --inplace

In the current directory before running the tests, which means that you can
then run pytest seamlessly on packages with compiled extensions.

To use this, run pytest with::

    pytest --inplace-build <other arguments>

or add::

    [tool:pytest]
    addopts = --inplace-build

to your ``setup.cfg`` file for the option to always be added automatically.

Note that if you have entry points in your package that need to be installed
for the tests to run, you will still need to make sure ``pip install -e .``
has been run for your package.
