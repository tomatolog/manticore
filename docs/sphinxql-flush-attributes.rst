.. raw:: html

   <div class="navheader">

8.30. FLUSH ATTRIBUTES syntax
`Prev <sphinxql-flush-ramchunk.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-flush-hostnames.html>`__

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

.. rubric:: 8.30. FLUSH ATTRIBUTES syntax
   :name: flush-attributes-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    FLUSH ATTRIBUTES

Added in 2.3.1-beta. Flushes all in-memory attribute updates in all the
active disk indexes to disk. Returns a tag that identifies the result
on-disk state (basically, a number of actual disk attribute saves
performed since the daemon startup).

.. code:: programlisting

    mysql> UPDATE testindex SET channel_id=1107025 WHERE id=1;
    Query OK, 1 row affected (0.04 sec)

    mysql> FLUSH ATTRIBUTES;
    +------+
    | tag  |
    +------+
    |    1 |
    +------+
    1 row in set (0.19 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+------------------------------------+---------------------------------------------+
| `Prev <sphinxql-flush-ramchunk.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-flush-hostnames.html>`__   |
+--------------------------------------------+------------------------------------+---------------------------------------------+
| 8.29. FLUSH RAMCHUNK syntax                | `Home <index.html>`__              |  8.31. FLUSH HOSTNAMES syntax               |
+--------------------------------------------+------------------------------------+---------------------------------------------+

.. raw:: html

   </div>
