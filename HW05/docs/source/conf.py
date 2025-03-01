# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HomeWork 05'
copyright = '2025, Thomas M.'
author = 'Thomas M.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Ensure Sphinx can find your code
# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath('../src'))


extensions = [
    'sphinx.ext.autodoc',     # Automatically extracts docstrings
    'sphinx.ext.napoleon',    # Support for Google and NumPy-style docstrings
    'sphinx.ext.viewcode',    # Adds links to source code
    'sphinx.ext.duration',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = [
#     'sphinx.ext.duration',
# ]
