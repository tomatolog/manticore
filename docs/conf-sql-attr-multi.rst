.. raw:: html

   <div class="navheader">

12.1.22. sql\_attr\_multi
`Prev <conf-sql-attr-float.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-string.html>`__

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

.. rubric:: 12.1.22. sql\_attr\_multi
   :name: sql_attr_multi
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

`Multi-valued attribute <mva.html>`__ (MVA) declaration. Multi-value
(ie. there may be more than one such attribute declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

Plain attributes only allow to attach 1 value per each document.
However, there are cases (such as tags or categories) when it is desired
to attach multiple values of the same attribute and be able to apply
filtering or grouping to value lists.

The declaration format is as follows (backslashes are for clarity only;
everything can be declared in a single line as well):

.. code:: programlisting

    sql_attr_multi = ATTR-TYPE ATTR-NAME 'from' SOURCE-TYPE \
        [;QUERY] \
        [;RANGE-QUERY]

where

.. raw:: html

   <div class="itemizedlist">

-  ATTR-TYPE is ‘uint’, ‘bigint’ or ‘timestamp’

-  SOURCE-TYPE is ‘field’, ‘query’, or ‘ranged-query’

-  QUERY is SQL query used to fetch all ( docid, attrvalue ) pairs

-  RANGE-QUERY is SQL query used to fetch min and max ID values, similar
   to ‘sql\_query\_range’

.. raw:: html

   </div>

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_multi = uint tag from query; SELECT id, tag FROM tags
    sql_attr_multi = bigint tag from ranged-query; \
        SELECT id, tag FROM tags WHERE id>=$start AND id<=$end; \
        SELECT MIN(id), MAX(id) FROM tags

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+----------------------------------+-----------------------------------------+
| `Prev <conf-sql-attr-float.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-string.html>`__   |
+----------------------------------------+----------------------------------+-----------------------------------------+
| 12.1.21. sql\_attr\_float              | `Home <index.html>`__            |  12.1.23. sql\_attr\_string             |
+----------------------------------------+----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
