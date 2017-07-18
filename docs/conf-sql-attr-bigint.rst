.. raw:: html

   <div class="navheader">

12.1.19. sql\_attr\_bigint
`Prev <conf-sql-attr-bool.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-timestamp.html>`__

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

.. rubric:: 12.1.19. sql\_attr\_bigint
   :name: sql_attr_bigint
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

64-bit signed integer `attribute <attributes.html>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only. Note
that unlike `sql\_attr\_uint <conf-sql-attr-uint.html>`__, these values
are **signed**. Introduced in version 0.9.9-rc1.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_bigint = my_bigint_id

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+----------------------------------+--------------------------------------------+
| `Prev <conf-sql-attr-bool.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-timestamp.html>`__   |
+---------------------------------------+----------------------------------+--------------------------------------------+
| 12.1.18. sql\_attr\_bool              | `Home <index.html>`__            |  12.1.20. sql\_attr\_timestamp             |
+---------------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
