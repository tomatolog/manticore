.. raw:: html

   <div class="navheader">

12.1.18. sql\_attr\_bool
`Prev <conf-sql-attr-uint.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-bigint.html>`__

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

.. rubric:: 12.1.18. sql\_attr\_bool
   :name: sql_attr_bool
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Boolean `attribute <attributes.html>`__ declaration. Multi-value (there
might be multiple attributes declared), optional. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only. Equivalent to
`sql\_attr\_uint <conf-sql-attr-uint.html>`__ declaration with a bit
count of 1.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_bool = is_deleted # will be packed to 1 bit

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+----------------------------------+-----------------------------------------+
| `Prev <conf-sql-attr-uint.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-bigint.html>`__   |
+---------------------------------------+----------------------------------+-----------------------------------------+
| 12.1.17. sql\_attr\_uint              | `Home <index.html>`__            |  12.1.19. sql\_attr\_bigint             |
+---------------------------------------+----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
