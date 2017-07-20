sql\_field\_string
~~~~~~~~~~~~~~~~~~

Combined string attribute and full-text field declaration. Multi-value
(ie. there may be more than one such attribute declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

`sql\_attr\_string <../../data_source_configuration_options/sqlattr_string.md>`__
only stores the column value but does not full-text index it. In some
cases it might be desired to both full-text index the column and store
it as attribute. ``sql_field_string`` lets you do exactly that. Both the
field and the attribute will be named the same.

Example:
^^^^^^^^

::


    sql_field_string = title # will be both indexed and stored

