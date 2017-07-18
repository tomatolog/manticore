.. raw:: html

   <div class="navheader">

8.31. FLUSH HOSTNAMES syntax
`Prev <sphinxql-flush-attributes.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-truncate-rtindex.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 8.31. FLUSH HOSTNAMES syntax
   :name: flush-hostnames-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    FLUSH HOSTNAMES

Added in 2.3.2-beta. Renew IPs associates to agent host names. To always
query the DNS for getting the host name IP, see
`hostname\_lookup <conf-hostname-lookup.html>`__ directive.

.. code:: programlisting

    mysql> FLUSH HOSTNAMES;
    Query OK, 5 rows affected (0.01 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+------------------------------------+----------------------------------------------+
| `Prev <sphinxql-flush-attributes.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-truncate-rtindex.html>`__   |
+----------------------------------------------+------------------------------------+----------------------------------------------+
| 8.30. FLUSH ATTRIBUTES syntax                | `Home <index.html>`__              |  8.32. TRUNCATE RTINDEX syntax               |
+----------------------------------------------+------------------------------------+----------------------------------------------+

.. raw:: html

   </div>
