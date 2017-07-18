.. raw:: html

   <div class="navheader">

8.6. INSERT and REPLACE syntax
`Prev <sphinxql-show-status.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-replace.html>`__

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

.. rubric:: 8.6. INSERT and REPLACE syntax
   :name: insert-and-replace-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    {INSERT | REPLACE} INTO index [(column, ...)]
        VALUES (value, ...)
        [, (...)]

INSERT statement, introduced in version 1.10-beta, is only supported for
RT indexes. It inserts new rows (documents) into an existing index, with
the provided column values.

ID column must be present in all cases. Rows with duplicate IDs will
**not** be overwritten by INSERT; use REPLACE to do that. REPLACE works
exactly like INSERT, except that if an old row has the same ID as a new
row, the old row is deleted before the new row is inserted.

``index`` is the name of RT index into which the new row(s) should be
inserted. The optional column names list lets you only explicitly
specify values for some of the columns present in the index. All the
other columns will be filled with their default values (0 for scalar
types, empty string for text types).

Expressions are not currently supported in INSERT and values should be
explicitly specified.

Multiple rows can be inserted using a single INSERT statement by
providing several comma-separated, parentheses-enclosed lists of rows
values.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+------------------------------------+-------------------------------------+
| `Prev <sphinxql-show-status.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-replace.html>`__   |
+-----------------------------------------+------------------------------------+-------------------------------------+
| 8.5. SHOW STATUS syntax                 | `Home <index.html>`__              |  8.7. REPLACE syntax                |
+-----------------------------------------+------------------------------------+-------------------------------------+

.. raw:: html

   </div>
