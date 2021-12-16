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
release = '0.2'

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
html_theme_options = {'collapse_navigation': False,}
html_static_path = ['_static']
html_show_sphinx = True
html_context = {'display_github': True, 'github_user': 'MattWillFlood', 'github_repo': 'EntropyHub','github_version': 'main/docs/'}
html_favicon = './_images/favicon.ico'

matlab_src_dir = r'../EntropyHubMat/'

add_module_names = False

