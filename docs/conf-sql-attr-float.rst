.. raw:: html

   <div class="navheader">

12.1.21. sql\_attr\_float
`Prev <conf-sql-attr-timestamp.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-multi.html>`__

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

.. rubric:: 12.1.21. sql\_attr\_float
   :name: sql_attr_float
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Floating point `attribute <attributes.html>`__ declaration. Multi-value
(there might be multiple attributes declared), optional. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

The values will be stored in single precision, 32-bit IEEE 754 format.
Represented range is approximately from 1e-38 to 1e+38. The amount of
decimal digits that can be stored precisely is approximately 7. One
important usage of the float attributes is storing latitude and
longitude values (in radians), for further usage in query-time geosphere
distance calculations.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_float = lat_radians
    sql_attr_float = long_radians

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+----------------------------------------+
| `Prev <conf-sql-attr-timestamp.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-multi.html>`__   |
+--------------------------------------------+----------------------------------+----------------------------------------+
| 12.1.20. sql\_attr\_timestamp              | `Home <index.html>`__            |  12.1.22. sql\_attr\_multi             |
+--------------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
