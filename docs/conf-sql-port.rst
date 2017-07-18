.. raw:: html

   <div class="navheader">

12.1.3. sql\_port
`Prev <conf-sql-host.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-user.html>`__

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

.. rubric:: 12.1.3. sql\_port
   :name: sql_port
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

SQL server IP port to connect to. Optional, default is 3306 for
``mysql`` source type and 5432 for ``pgsql`` type. Applies to SQL source
types (``mysql``, ``pgsql``, ``mssql``) only. Note that it depends on
`sql\_host <conf-sql-host.html>`__ setting whether this value will
actually be used.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_port = 3306

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------+----------------------------------+----------------------------------+
| `Prev <conf-sql-host.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-user.html>`__   |
+----------------------------------+----------------------------------+----------------------------------+
| 12.1.2. sql\_host                | `Home <index.html>`__            |  12.1.4. sql\_user               |
+----------------------------------+----------------------------------+----------------------------------+

.. raw:: html

   </div>
