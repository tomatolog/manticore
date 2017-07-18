.. raw:: html

   <div class="navheader">

8.32. TRUNCATE RTINDEX syntax
`Prev <sphinxql-flush-hostnames.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-agent-status.html>`__

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

.. rubric:: 8.32. TRUNCATE RTINDEX syntax
   :name: truncate-rtindex-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    TRUNCATE RTINDEX rtindex

TRUNCATE RTINDEX statement, added in version 2.1.1-beta, clears the RT
index completely. It disposes the in-memory data, unlinks all the index
data files, and releases the associated binary logs.

.. code:: programlisting

    mysql> TRUNCATE RTINDEX rt;
    Query OK, 0 rows affected (0.05 sec)

You may want to use this if you are using RT indices as “delta index”
files; when you build the main index, you need to wipe the delta index,
and thus TRUNCATE RTINDEX. You also need to use this command before
attaching an index; see `Section 8.27, “ATTACH INDEX
syntax” <sphinxql-attach-index.html>`__.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+------------------------------------+-----------------------------------------------+
| `Prev <sphinxql-flush-hostnames.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-agent-status.html>`__   |
+---------------------------------------------+------------------------------------+-----------------------------------------------+
| 8.31. FLUSH HOSTNAMES syntax                | `Home <index.html>`__              |  8.33. SHOW AGENT STATUS                      |
+---------------------------------------------+------------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
