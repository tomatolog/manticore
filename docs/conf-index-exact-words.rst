.. raw:: html

   <div class="navheader">

12.2.42. index\_exact\_words
`Prev <conf-inplace-write-factor.html>`__ 
12.2. Index configuration options
 `Next <conf-overshort-step.html>`__

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

.. rubric:: 12.2.42. index\_exact\_words
   :name: index_exact_words
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Whether to index the original keywords along with the stemmed/remapped
versions. Optional, default is 0 (do not index). Introduced in version
0.9.9-rc1.

When enabled, ``index_exact_words`` forces ``indexer`` to put the raw
keywords in the index along with the stemmed versions. That, in turn,
enables `exact form operator <extended-syntax.html>`__ in the query
language to work. This impacts the index size and the indexing time.
However, searching performance is not impacted at all.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    index_exact_words = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+---------------------------------+----------------------------------------+
| `Prev <conf-inplace-write-factor.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-overshort-step.html>`__   |
+----------------------------------------------+---------------------------------+----------------------------------------+
| 12.2.41. inplace\_write\_factor              | `Home <index.html>`__           |  12.2.43. overshort\_step              |
+----------------------------------------------+---------------------------------+----------------------------------------+

.. raw:: html

   </div>
