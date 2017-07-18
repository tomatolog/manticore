.. raw:: html

   <div class="navheader">

12.1.7. sql\_sock
`Prev <conf-sql-db.html>`__ 
12.1. Data source configuration options
 `Next <conf-mysql-connect-flags.html>`__

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

.. rubric:: 12.1.7. sql\_sock
   :name: sql_sock
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

UNIX socket name to connect to for local SQL servers. Optional, default
value is empty (use client library default settings). Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

On Linux, it would typically be ``/var/lib/mysql/mysql.sock``. On
FreeBSD, it would typically be ``/tmp/mysql.sock``. Note that it depends
on `sql\_host <conf-sql-host.html>`__ setting whether this value will
actually be used.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_sock = /tmp/mysql.sock

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------+----------------------------------+---------------------------------------------+
| `Prev <conf-sql-db.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-mysql-connect-flags.html>`__   |
+--------------------------------+----------------------------------+---------------------------------------------+
| 12.1.6. sql\_db                | `Home <index.html>`__            |  12.1.8. mysql\_connect\_flags              |
+--------------------------------+----------------------------------+---------------------------------------------+

.. raw:: html

   </div>
