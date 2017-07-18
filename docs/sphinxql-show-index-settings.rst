.. raw:: html

   <div class="navheader">

8.36. SHOW INDEX SETTINGS syntax
`Prev <sphinxql-show-index-status.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-optimize-index.html>`__

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

.. rubric:: 8.36. SHOW INDEX SETTINGS syntax
   :name: show-index-settings-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW INDEX index_name[.N | CHUNK N] SETTINGS

Displays per-index settings in a ``sphinx.conf`` compliant file format,
similar to the `–dumpconfig <ref-indextool.html>`__ option of the
indextool. The report provides a breakdown of all the index settings,
including tokenizer and dictionary options. You may also specify a
particular `chunk number <conf-rt-mem-limit.html>`__ for the RT indexes.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+------------------------------------+--------------------------------------------+
| `Prev <sphinxql-show-index-status.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-optimize-index.html>`__   |
+-----------------------------------------------+------------------------------------+--------------------------------------------+
| 8.35. SHOW INDEX STATUS syntax                | `Home <index.html>`__              |  8.37. OPTIMIZE INDEX syntax               |
+-----------------------------------------------+------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
