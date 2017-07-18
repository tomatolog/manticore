.. raw:: html

   <div class="navheader">

12.1.8. mysql\_connect\_flags
`Prev <conf-sql-sock.html>`__ 
12.1. Data source configuration options
 `Next <conf-mysql-ssl.html>`__

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

.. rubric:: 12.1.8. mysql\_connect\_flags
   :name: mysql_connect_flags
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

MySQL client connection flags. Optional, default value is 0 (do not set
any flags). Applies to ``mysql`` source type only.

This option must contain an integer value with the sum of the flags. The
value will be passed to
`mysql\_real\_connect() <http://dev.mysql.com/doc/refman/5.0/en/mysql-real-connect.html>`__
verbatim. The flags are enumerated in mysql\_com.h include file. Flags
that are especially interesting in regard to indexing, with their
respective values, are as follows:

.. raw:: html

   <div class="itemizedlist">

-  CLIENT\_COMPRESS = 32; can use compression protocol

-  CLIENT\_SSL = 2048; switch to SSL after handshake

-  CLIENT\_SECURE\_CONNECTION = 32768; new 4.1 authentication

.. raw:: html

   </div>

For instance, you can specify 2080 (2048+32) to use both compression and
SSL, or 32768 to use new authentication only. Initially, this option was
introduced to be able to use compression when the ``indexer`` and
``mysqld`` are on different hosts. Compression on 1 Gbps links is most
likely to hurt indexing time though it reduces network traffic, both in
theory and in practice. However, enabling compression on 100 Mbps links
may improve indexing time significantly (upto 20-30% of the total
indexing time improvement was reported). Your mileage may vary.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mysql_connect_flags = 32 # enable compression

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------+----------------------------------+--------------------------------------------------------------+
| `Prev <conf-sql-sock.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-mysql-ssl.html>`__                              |
+----------------------------------+----------------------------------+--------------------------------------------------------------+
| 12.1.7. sql\_sock                | `Home <index.html>`__            |  12.1.9. mysql\_ssl\_cert, mysql\_ssl\_key, mysql\_ssl\_ca   |
+----------------------------------+----------------------------------+--------------------------------------------------------------+

.. raw:: html

   </div>
