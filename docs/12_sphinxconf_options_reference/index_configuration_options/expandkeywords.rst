expand\_keywords
~~~~~~~~~~~~~~~~

Expand keywords with exact forms and/or stars when possible. Optional,
default is 0 (do not expand keywords). Introduced in version 1.10-beta.

Queries against indexes with ``expand_keywords`` feature enabled are
internally expanded as follows. If the index was built with prefix or
infix indexing enabled, every keyword gets internally replaced with a
disjunction of keyword itself and a respective prefix or infix (keyword
with stars). If the index was built with both stemming and
`index\_exact\_words <../../index_configuration_options/indexexact_words.md>`__
enabled, exact form is also added. Here's an example that shows how
internal expansion works when all of the above (infixes, stemming, and
exact words) are combined:

::


    running -> ( running | *running* | =running )

Expanded queries take naturally longer to complete, but can possibly
improve the search quality, as the documents with exact form matches
should be ranked generally higher than documents with stemmed or infix
matches.

Note that the existing query syntax does not allow to emulate this kind
of expansion, because internal expansion works on keyword level and
expands keywords within phrase or quorum operators too (which is not
possible through the query syntax).

This directive does not affect ``indexer`` in any way, it only affects
``searchd``.

Example:
^^^^^^^^

::


    expand_keywords = 1

