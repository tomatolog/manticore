.. raw:: html

   <div class="navheader">

12.1.17. sql\_attr\_uint
`Prev <conf-sql-query-killlist.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-bool.html>`__

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

.. rubric:: 12.1.17. sql\_attr\_uint
   :name: sql_attr_uint
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Unsigned integer `attribute <attributes.html>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

The column value should fit into 32-bit unsigned integer range. Values
outside this range will be accepted but wrapped around. For instance, -1
will be wrapped around to 2^32-1 or 4,294,967,295.

You can specify bit count for integer attributes by appending
‘:BITCOUNT’ to attribute name (see example below). Attributes with less
than default 32-bit size, or bitfields, perform slower. But they require
less RAM when using `extern storage <conf-docinfo.html>`__: such
bitfields are packed together in 32-bit chunks in ``.spa`` attribute
data file. Bit size settings are ignored if using `inline
storage <conf-docinfo.html>`__.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_uint = group_id
    sql_attr_uint = forum_id:9 # 9 bits for forum_id

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+---------------------------------------+
| `Prev <conf-sql-query-killlist.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-bool.html>`__   |
+--------------------------------------------+----------------------------------+---------------------------------------+
| 12.1.16. sql\_query\_killlist              | `Home <index.html>`__            |  12.1.18. sql\_attr\_bool             |
+--------------------------------------------+----------------------------------+---------------------------------------+

.. raw:: html

   </div>
