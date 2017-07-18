.. raw:: html

   <div class="navheader">

12.1.9. mysql\_ssl\_cert, mysql\_ssl\_key, mysql\_ssl\_ca
`Prev <conf-mysql-connect-flags.html>`__ 
12.1. Data source configuration options
 `Next <conf-odbc-dsn.html>`__

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

.. rubric:: 12.1.9. mysql\_ssl\_cert, mysql\_ssl\_key, mysql\_ssl\_ca
   :name: mysql_ssl_cert-mysql_ssl_key-mysql_ssl_ca
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

SSL certificate settings to use for connecting to MySQL server.
Optional, default values are empty strings (do not use SSL). Applies to
``mysql`` source type only.

These directives let you set up secure SSL connection between
``indexer`` and MySQL. The details on creating the certificates and
setting up MySQL server can be found in MySQL documentation.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mysql_ssl_cert = /etc/ssl/client-cert.pem
    mysql_ssl_key = /etc/ssl/client-key.pem
    mysql_ssl_ca = /etc/ssl/cacert.pem

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+----------------------------------+----------------------------------+
| `Prev <conf-mysql-connect-flags.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-odbc-dsn.html>`__   |
+---------------------------------------------+----------------------------------+----------------------------------+
| 12.1.8. mysql\_connect\_flags               | `Home <index.html>`__            |  12.1.10. odbc\_dsn              |
+---------------------------------------------+----------------------------------+----------------------------------+

.. raw:: html

   </div>
