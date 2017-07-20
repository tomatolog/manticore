index\_field\_lengths
~~~~~~~~~~~~~~~~~~~~~

Enables computing and storing of field lengths (both per-document and
average per-index values) into the index. Optional, default is 0 (do not
compute and store).

When ``index_field_lengths`` is set to 1, ``indexer`` will 1) create a
respective length attribute for every full-text field, sharing the same
name but with \_\_len\_ suffix; 2) compute a field length (counted in
keywords) for every document and store in to a respective attribute; 3)
compute the per-index averages. The lengths attributes will have a
special TOKENCOUNT type, but their values are in fact regular 32-bit
integers, and their values are generally accessible.

BM25A() and BM25F() functions in the expression ranker are based on
these lengths and require ``index_field_lengths`` to be enabled.
Historically, Manticore used a simplified, stripped-down variant of BM25
that, unlike the complete function, did <b>not</b> account for document
length. (We later realized that it should have been called BM15 from the
start.) Also we added support for both a complete variant of BM25, and
its extension towards multiple fields, called BM25F. They require
per-document length and per-field lengths, respectively. Hence the
additional directive.

Example:
^^^^^^^^

::


    index_field_lengths = 1

