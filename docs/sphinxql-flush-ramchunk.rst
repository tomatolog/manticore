.. raw:: html

   <div class="navheader">

8.29. FLUSH RAMCHUNK syntax
`Prev <sphinxql-flush-rtindex.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-flush-attributes.html>`__

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

.. rubric:: 8.29. FLUSH RAMCHUNK syntax
   :name: flush-ramchunk-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    FLUSH RAMCHUNK rtindex

FLUSH RAMCHUNK statement, added in version 2.1.2-release, forcibly
creates a new disk chunk in a RT index.

Normally, RT index would flush and convert the contents of the RAM chunk
into a new disk chunk automatically, once the RAM chunk reaches the
maximum allowed `rt\_mem\_limit <conf-rt-mem-limit.html>`__ size.
However, for debugging and testing it might be useful to forcibly create
a new disk chunk, and FLUSH RAMCHUNK statement does exactly that.

Note that using FLUSH RAMCHUNK increases RT index fragmentation. Most
likely, you want to use FLUSH RTINDEX instead. We suggest that you
abstain from using just this statement unless you’re absolutely sure
what you’re doing. As the right way is to issue FLUSH RAMCHUNK with
following `OPTIMIZE <sphinxql-optimize-index.html>`__ command. Such
combo allows to keep RT index fragmentation on minimum.

.. code:: programlisting

    mysql> FLUSH RAMCHUNK rt;
    Query OK, 0 rows affected (0.05 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+----------------------------------------------+
| `Prev <sphinxql-flush-rtindex.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-flush-attributes.html>`__   |
+-------------------------------------------+------------------------------------+----------------------------------------------+
| 8.28. FLUSH RTINDEX syntax                | `Home <index.html>`__              |  8.30. FLUSH ATTRIBUTES syntax               |
+-------------------------------------------+------------------------------------+----------------------------------------------+

.. raw:: html

   </div>
