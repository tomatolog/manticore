.. raw:: html

   <div class="navheader">

10.4. Building snippets (excerpts) via MySQL
`Prev <sphinxse-using.html>`__ 
Chapter 10. MySQL storage engine (SphinxSE)
 `Next <reporting-bugs.html>`__

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

.. rubric:: 10.4. Building snippets (excerpts) via MySQL
   :name: building-snippets-excerpts-via-mysql
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Starting with version 0.9.9-rc2, SphinxSE also includes a UDF function
that lets you create snippets through MySQL. The functionality is fully
similar to `BuildExcerprts <api-func-buildexcerpts.html>`__ API call but
accessible through MySQL+SphinxSE.

The binary that provides the UDF is named ``sphinx.so`` and should be
automatically built and installed to proper location along with SphinxSE
itself. If it does not get installed automatically for some reason, look
for ``sphinx.so`` in the build directory and copy it to the plugins
directory of your MySQL instance. After that, register the UDF using the
following statement:

.. code:: programlisting

    CREATE FUNCTION sphinx_snippets RETURNS STRING SONAME 'sphinx.so';

Function name *must* be sphinx\_snippets, you can not use an arbitrary
name. Function arguments are as follows:

**Prototype:** function sphinx\_snippets ( document, index, words,
[options] );

Document and words arguments can be either strings or table columns.
Options must be specified like this: ``'value' AS option_name``. For a
list of supported options, refer to
`BuildExcerprts() <api-func-buildexcerpts.html>`__ API call. The only
UDF-specific additional option is named ``'sphinx'`` and lets you
specify searchd location (host and port).

Usage examples:

.. code:: programlisting

    SELECT sphinx_snippets('hello world doc', 'main', 'world',
        'sphinx://192.168.1.1/' AS sphinx, true AS exact_phrase,
        '[b]' AS before_match, '[/b]' AS after_match)
    FROM documents;

    SELECT title, sphinx_snippets(text, 'index', 'mysql php') AS text
        FROM sphinx, documents
        WHERE query='mysql php' AND sphinx.id=documents.id;

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+--------------------------+-----------------------------------+
| `Prev <sphinxse-using.html>`__    | `Up <sphinxse.html>`__   |  `Next <reporting-bugs.html>`__   |
+-----------------------------------+--------------------------+-----------------------------------+
| 10.3. Using SphinxSE              | `Home <index.html>`__    |  Chapter 11. Reporting bugs       |
+-----------------------------------+--------------------------+-----------------------------------+

.. raw:: html

   </div>
