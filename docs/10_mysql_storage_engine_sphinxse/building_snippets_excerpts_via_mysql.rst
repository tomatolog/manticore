Building snippets (excerpts) via MySQL
--------------------------------------

Starting with version 0.9.9-rc2, SphinxSE also includes a UDF function
that lets you create snippets through MySQL. The functionality is fully
similar to
`BuildExcerprts <../additional_functionality/buildexcerpts.md>`__ API
call but accessible through MySQL+SphinxSE.

The binary that provides the UDF is named ``sphinx.so`` and should be
automatically built and installed to proper location along with SphinxSE
itself. If it does not get installed automatically for some reason, look
for ``sphinx.so`` in the build directory and copy it to the plugins
directory of your MySQL instance. After that, register the UDF using the
following statement:

::


    CREATE FUNCTION sphinx_snippets RETURNS STRING SONAME 'sphinx.so';

Function name *must* be sphinx\_snippets, you can not use an arbitrary
name. Function arguments are as follows:

<b>Prototype:</b> function sphinx\_snippets ( document, index, words,
[options] );

Document and words arguments can be either strings or table columns.
Options must be specified like this:
``&#039;value&#039; AS option_name``. For a list of supported options,
refer to
`BuildExcerprts() <../additional_functionality/buildexcerpts.md>`__ API
call. The only UDF-specific additional option is named
``&#039;sphinx&#039;`` and lets you specify searchd location (host and
port).

Usage examples:

::


    SELECT sphinx_snippets('hello world doc', 'main', 'world',
        'sphinx://192.168.1.1/' AS sphinx, true AS exact_phrase,
        '[b]' AS before_match, '[/b]' AS after_match)
    FROM documents;

    SELECT title, sphinx_snippets(text, 'index', 'mysql php') AS text
        FROM sphinx, documents
        WHERE query='mysql php' AND sphinx.id=documents.id;

