.. raw:: html

   <div class="navheader">

12.1.2. sql\_host
`Prev <conf-source-type.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-port.html>`__

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

.. rubric:: 12.1.2. sql\_host
   :name: sql_host
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

SQL server host to connect to. Mandatory, no default value. Applies to
SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

In the simplest case when Sphinx resides on the same host with your
MySQL or PostgreSQL installation, you would simply specify “localhost”.
Note that MySQL client library chooses whether to connect over TCP/IP or
over UNIX socket based on the host name. Specifically “localhost” will
force it to use UNIX socket (this is the default and generally
recommended mode) and “127.0.0.1” will force TCP/IP usage. Refer to
`MySQL
manual <http://dev.mysql.com/doc/refman/5.0/en/mysql-real-connect.html>`__
for more details.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_host = localhost

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+----------------------------------+----------------------------------+
| `Prev <conf-source-type.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-port.html>`__   |
+-------------------------------------+----------------------------------+----------------------------------+
| 12.1.1. type                        | `Home <index.html>`__            |  12.1.3. sql\_port               |
+-------------------------------------+----------------------------------+----------------------------------+

.. raw:: html

   </div>
