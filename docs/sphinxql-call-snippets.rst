.. raw:: html

   <div class="navheader">

8.14. CALL SNIPPETS syntax
`Prev <sphinxql-rollback.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-call-keywords.html>`__

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

.. rubric:: 8.14. CALL SNIPPETS syntax
   :name: call-snippets-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    CALL SNIPPETS(data, index, query[, opt_value AS opt_name[, ...]])

CALL SNIPPETS statement, introduced in version 1.10-beta, builds a
snippet from provided data and query, using specified index settings.

``data`` is the source data to extract a snippet from. It could be a
single string, or the list of the strings enclosed in curly brackets.
``index`` is the name of the index from which to take the text
processing settings. ``query`` is the full-text query to build snippets
for. Additional options are documented in `Section 9.7.1,
“BuildExcerpts” <api-func-buildexcerpts.html>`__. Usage example:

.. code:: programlisting

    CALL SNIPPETS('this is my document text', 'test1', 'hello world',
        5 AS around, 200 AS limit);
    CALL SNIPPETS(('this is my document text','this is my another text'), 'test1', 'hello world',
        5 AS around, 200 AS limit);
    CALL SNIPPETS(('data/doc1.txt','data/doc2.txt','/home/sphinx/doc3.txt'), 'test1', 'hello world',
        5 AS around, 200 AS limit, 1 AS load_files);

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+------------------------------------+-------------------------------------------+
| `Prev <sphinxql-rollback.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-call-keywords.html>`__   |
+--------------------------------------+------------------------------------+-------------------------------------------+
| 8.13. ROLLBACK syntax                | `Home <index.html>`__              |  8.15. CALL KEYWORDS syntax               |
+--------------------------------------+------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
