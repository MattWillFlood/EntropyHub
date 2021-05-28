# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys
sys.path.insert(0, os.path.abspath('../EntropyHubPy/'))
import sphinx_rtd_theme

def setup(app):
    app.add_css_file('custom.css')

# -- Project information -----------------------------------------------------
project = 'EntropyHub'
copyright = '2021, Matthew W. Flood'
author = 'Matthew W. Flood'
# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [ 'sphinx_rtd_theme', 'sphinx.ext.autodoc',
     'sphinxcontrib.matlab', 'sphinx.ext.githubpages']
#extensions = [ 'sphinx_rtd_theme', 'sphinx.ext.autodoc']

autodoc_mock_imports = ["numpy", 'scipy','matplotlib','PyEMD','requests']
pygments_style = 'sphinx'


# source_suffix = {'.rst': 'restructuredtext',
#    '.md': 'markdown',}
# root_doc = "README"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme =  "sphinx_rtd_theme" #'alabaster'
html_logo = "./_images/Logo.png"
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

#html_js_files = ['documenter.js', 'search.js', 'themeswap.js', ]
html_theme_options = {'collapse_navigation': False,}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['js']
html_static_path = ['_static']
html_show_sphinx = True

matlab_src_dir = r'../EntropyHubMat/'

add_module_names = False

