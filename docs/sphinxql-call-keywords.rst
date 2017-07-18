.. raw:: html

   <div class="navheader">

8.15. CALL KEYWORDS syntax
`Prev <sphinxql-call-snippets.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-call-qsuggest.html>`__

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

.. rubric:: 8.15. CALL KEYWORDS syntax
   :name: call-keywords-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    CALL KEYWORDS(text, index [, options])

CALL KEYWORDS statement, introduced in version 1.10-beta, splits text
into particular keywords. It returns tokenized and normalized forms of
the keywords, and, optionally, keyword statistics. Since version
2.2.2-beta it also returns the position of each keyword in the query and
all forms of tokenized keywords in the case that lemmatizers were used.

``text`` is the text to break down to keywords. ``index`` is the name of
the index from which to take the text processing settings. ``options``
prior 2.3.2-beta, is an optional boolean parameter that specifies
whether to return document and hit occurrence statistics. ``options``
starting with 2.3.2-beta, can also accept parameters for configuring
folding depending on tokenization settings:

.. raw:: html

   <div class="itemizedlist">

-  ``stats`` - show statistics of keywords, default is 0

-  ``fold_wildcards`` - fold wildcards, default is 1

-  ``fold_lemmas`` - fold morphological lemmas, default is 0

-  ``fold_blended`` - fold blended words, default is 0

-  ``expansion_limit`` - override expansion\_limit defined in
   configuration, default is 0 (use value from configuration)

.. raw:: html

   </div>

.. code:: programlisting

    call keywords(
        'que*',
        'myindex',
        1 as fold_wildcards,
        1 as fold_lemmas,
        1 as fold_blended,
        1 as expansion_limit,
        1 as stats);

Default values to match previous CALL KEYWORDS output are:

.. code:: programlisting

    call keywords(
        'que*',
        'myindex',
        1 as fold_wildcards,
        0 as fold_lemmas,
        0 as fold_blended,
        0 as expansion_limit,
        0 as stats);

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+-------------------------------------------+
| `Prev <sphinxql-call-snippets.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-call-qsuggest.html>`__   |
+-------------------------------------------+------------------------------------+-------------------------------------------+
| 8.14. CALL SNIPPETS syntax                | `Home <index.html>`__              |  8.16. CALL QSUGGEST syntax               |
+-------------------------------------------+------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
