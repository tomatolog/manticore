.. raw:: html

   <div class="navheader">

12.2.63. index\_field\_lengths
`Prev <conf-bigram-index.html>`__ 
12.2. Index configuration options
 `Next <conf-regexp-filter.html>`__

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

.. rubric:: 12.2.63. index\_field\_lengths
   :name: index_field_lengths
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Enables computing and storing of field lengths (both per-document and
average per-index values) into the index. Optional, default is 0 (do not
compute and store). Added in 2.1.1-beta.

When ``index_field_lengths`` is set to 1, ``indexer`` will 1) create a
respective length attribute for every full-text field, sharing the same
name but with *\_len* suffix; 2) compute a field length (counted in
keywords) for every document and store in to a respective attribute; 3)
compute the per-index averages. The lengths attributes will have a
special TOKENCOUNT type, but their values are in fact regular 32-bit
integers, and their values are generally accessible.

BM25A() and BM25F() functions in the expression ranker are based on
these lengths and require ``index_field_lengths`` to be enabled.
Historically, Sphinx used a simplified, stripped-down variant of BM25
that, unlike the complete function, did **not** account for document
length. (We later realized that it should have been called BM15 from the
start.) Starting with 2.1.1-beta, we added support for both a complete
variant of BM25, and its extension towards multiple fields, called
BM25F. They require per-document length and per-field lengths,
respectively. Hence the additional directive.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    index_field_lengths = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+---------------------------------+---------------------------------------+
| `Prev <conf-bigram-index.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-regexp-filter.html>`__   |
+--------------------------------------+---------------------------------+---------------------------------------+
| 12.2.62. bigram\_index               | `Home <index.html>`__           |  12.2.64. regexp\_filter              |
+--------------------------------------+---------------------------------+---------------------------------------+

.. raw:: html

   </div>
