.. raw:: html

   <div class="navheader">

8.47. Comment syntax
`Prev <sphinxql-multi-queries.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-reserved-keywords.html>`__

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

.. rubric:: 8.47. Comment syntax
   :name: comment-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Since version 2.0.1-beta, SphinxQL supports C-style comment syntax.
Everything from an opening ``/*`` sequence to a closing ``*/`` sequence
is ignored. Comments can span multiple lines, can not nest, and should
not get logged. MySQL specific ``/*! ... */`` comments are also
currently ignored. (As the comments support was rather added for better
compatibility with ``mysqldump`` produced dumps, rather than improving
general query interoperability between Sphinx and MySQL.)

.. code:: programlisting

    SELECT /*! SQL_CALC_FOUND_ROWS */ col1 FROM table1 WHERE ...

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+-----------------------------------------------+
| `Prev <sphinxql-multi-queries.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-reserved-keywords.html>`__   |
+-------------------------------------------+------------------------------------+-----------------------------------------------+
| 8.46. Multi-statement queries             | `Home <index.html>`__              |  8.48. List of SphinxQL reserved keywords     |
+-------------------------------------------+------------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
