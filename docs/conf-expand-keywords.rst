.. raw:: html

   <div class="navheader">

12.2.46. expand\_keywords
`Prev <conf-hitless-words.html>`__ 
12.2. Index configuration options
 `Next <conf-blend-chars.html>`__

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

.. rubric:: 12.2.46. expand\_keywords
   :name: expand_keywords
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Expand keywords with exact forms and/or stars when possible. Optional,
default is 0 (do not expand keywords). Introduced in version 1.10-beta.

Queries against indexes with ``expand_keywords`` feature enabled are
internally expanded as follows. If the index was built with prefix or
infix indexing enabled, every keyword gets internally replaced with a
disjunction of keyword itself and a respective prefix or infix (keyword
with stars). If the index was built with both stemming and
`index\_exact\_words <conf-index-exact-words.html>`__ enabled, exact
form is also added. Here’s an example that shows how internal expansion
works when all of the above (infixes, stemming, and exact words) are
combined:

.. code:: programlisting

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

.. rubric:: Example:
   :name: example

.. code:: programlisting

    expand_keywords = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------+-------------------------------------+
| `Prev <conf-hitless-words.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-blend-chars.html>`__   |
+---------------------------------------+---------------------------------+-------------------------------------+
| 12.2.45. hitless\_words               | `Home <index.html>`__           |  12.2.47. blend\_chars              |
+---------------------------------------+---------------------------------+-------------------------------------+

.. raw:: html

   </div>
