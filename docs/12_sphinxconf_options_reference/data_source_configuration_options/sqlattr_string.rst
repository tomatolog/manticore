sql\_attr\_string
~~~~~~~~~~~~~~~~~

String attribute declaration. Multi-value (ie. there may be more than
one such attribute declared), optional. Applies to SQL source types
(``mysql``, ``pgsql``, ``mssql``) only.

String attributes can store arbitrary strings attached to every
document. There's a fixed size limit of 4 MB per value. Also,
``searchd`` will currently cache all the values in RAM, which is an
additional implicit limit.

String attributes can be used for sorting and grouping(ORDER BY, GROUP
BY, WITHIN GROUP ORDER BY). Note that attributes declared using
``sql_attr_string`` will <b>not</b> be full-text indexed; you can use
`sql\_field\_string <../../data_source_configuration_options/sqlfield_string.md>`__
directive for that.

Example:
^^^^^^^^

::


    sql_attr_string = title # will be stored but will not be indexed

