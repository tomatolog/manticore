import os
import sys

import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage'
]

master_doc = 'index'
source_suffix = '.rst'
project = u'Manticore Search'
copyright = u'2017, Manticore Search'

pygments_style = 'sphinx'
language = 'en'
man_pages = [
    ('index', 'manticoresearch.com', u'Manticore Documentation',
     [u'Manticore Search'], 1)
]
