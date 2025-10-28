# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sudoku generator'
copyright = '2025, bilbopingouin'
author = 'bilbopingouin'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Adding path
import os   # noqa: E402
import sys  # noqa: E402
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../libs')

print(sys.path)


extensions = [
        'sphinx.ext.duration',  # Shows how long it lasted to generate
                                # the files
        'sphinx.ext.doctest',   # Allows to run `make doctest` which
                                # can be used to test some functions
        'sphinx.ext.autodoc',   # Allows to browse the code to get the
                                # function description directly from there
        'sphinx.ext.autosummary',  # Allows to automatise the autodoc
        ]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
