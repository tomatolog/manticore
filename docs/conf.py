#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.abspath('..'))
extensions = [
    'sphinx.ext.autodoc',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Manticore'
copyright = '2017, Manticore Search'
version = '2.3.3'
release = '2.3.3'
pygments_style = 'sphinx'
todo_include_todos = False
