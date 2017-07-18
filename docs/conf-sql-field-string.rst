.. raw:: html

   <div class="navheader">

12.1.26. sql\_field\_string
`Prev <conf-sql-column-buffers.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-file-field.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.1.26. sql\_field\_string
   :name: sql_field_string
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Combined string attribute and full-text field declaration. Multi-value
(ie. there may be more than one such attribute declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.
Introduced in version 1.10-beta.

`sql\_attr\_string <conf-sql-attr-string.html>`__ only stores the column
value but does not full-text index it. In some cases it might be desired
to both full-text index the column and store it as attribute.
``sql_field_string`` lets you do exactly that. Both the field and the
attribute will be named the same.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_field_string = title # will be both indexed and stored

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+----------------------------------------+
| `Prev <conf-sql-column-buffers.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-file-field.html>`__   |
+--------------------------------------------+----------------------------------+----------------------------------------+
| 12.1.25. sql\_column\_buffers              | `Home <index.html>`__            |  12.1.27. sql\_file\_field             |
+--------------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
