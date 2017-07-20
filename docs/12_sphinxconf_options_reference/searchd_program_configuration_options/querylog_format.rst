query\_log\_format
~~~~~~~~~~~~~~~~~~

Query log format. Optional, allowed values are ‘plain’ and ‘sphinxql’,
default is ‘plain’.

The default one logs queries in a custom text format. The ‘sphinxql’
logs valid SphinxQL statements. This directive allows to switch between
the two formats on search daemon startup. The log format can also be
altered on the fly, using ``SET GLOBAL query_log_format=sphinxql``
syntax. Refer to `the section called “``searchd`` query log
formats” <../../searchd_query_log_formats/README.md>`__ for more
discussion and format details.

Example:
^^^^^^^^

::


    query_log_format = sphinxql

