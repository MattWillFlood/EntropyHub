# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys
sys.path.insert(0, os.path.abspath('../EntropyHubPy/'))
#sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

def setup(app):
    app.add_css_file('custom.css')
   # app.add_js_file("widget-popup.js")


# -- Project information -----------------------------------------------------
project = 'EntropyHub'
copyright = '2025, Matthew W. Flood'
author = 'Matthew W. Flood'
# The full version, including alpha/beta/rc tags
release = '2.0'

# -- General configuration ---------------------------------------------------
extensions = [ 'sphinx_rtd_theme', 'sphinx.ext.autodoc',
     'sphinxcontrib.matlab', 'sphinx.ext.githubpages', 'sphinx_togglebutton' ]
#extensions = [ 'sphinx_rtd_theme', 'sphinx.ext.autodoc', 'sphinx_toolbox.collapse', 'hidden_code_block']

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
html_theme_options = {'collapse_navigation': False,}
html_static_path = ['_static']
html_show_sphinx = False
html_context = {'display_github': True, 'github_user': 'MattWillFlood', 'github_repo': 'EntropyHub','github_version': 'main/docs/'}
html_favicon = './_images/favicon.ico'

#html_js_files = ["widget-popup.js"]

matlab_src_dir = r'../EntropyHubMat/'

add_module_names = False

