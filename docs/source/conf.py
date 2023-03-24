# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Vju 3'
copyright = '2023, iCsys AS'
author = 'iCsys AS'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    # "sphinx_multiversion",
]


# Make sure the target is unique
autosectionlabel_prefix_document = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_sidebars = {
    '**': ['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html',  "_templates\\versioning.html"],
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
