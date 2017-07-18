.. raw:: html

   <div class="navheader">

12.1.10. odbc\_dsn
`Prev <conf-mysql-ssl.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-query-pre.html>`__

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

.. rubric:: 12.1.10. odbc\_dsn
   :name: odbc_dsn
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

ODBC DSN to connect to. Mandatory, no default value. Applies to ``odbc``
source type only.

ODBC DSN (Data Source Name) specifies the credentials (host, user,
password, etc) to use when connecting to ODBC data source. The format
depends on specific ODBC driver used.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    odbc_dsn = Driver={Oracle ODBC Driver};Dbq=myDBName;Uid=myUsername;Pwd=myPassword

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------------------------+----------------------------------+---------------------------------------+
| `Prev <conf-mysql-ssl.html>`__                               | `Up <confgroup-source.html>`__   |  `Next <conf-sql-query-pre.html>`__   |
+--------------------------------------------------------------+----------------------------------+---------------------------------------+
| 12.1.9. mysql\_ssl\_cert, mysql\_ssl\_key, mysql\_ssl\_ca    | `Home <index.html>`__            |  12.1.11. sql\_query\_pre             |
+--------------------------------------------------------------+----------------------------------+---------------------------------------+

.. raw:: html

   </div>
