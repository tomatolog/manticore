index\_exact\_words
~~~~~~~~~~~~~~~~~~~

Whether to index the original keywords along with the stemmed/remapped
versions. Optional, default is 0 (do not index).

When enabled, ``index_exact_words`` forces ``indexer`` to put the raw
keywords in the index along with the stemmed versions. That, in turn,
enables `exact form operator <../../extended_query_syntax.md>`__ in the
query language to work. This impacts the index size and the indexing
time. However, searching performance is not impacted at all.

Example:
^^^^^^^^

::


    index_exact_words = 1

