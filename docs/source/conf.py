# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ilha Proibida'
copyright = '2023, Grupo Vento'
author = 'Grupo Vento'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'
# Define a codificação dos arquivos fonte (UTF-8)
source_encoding = 'utf-8'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['theme_overrides.css']
