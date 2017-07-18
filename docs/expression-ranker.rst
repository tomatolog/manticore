.. raw:: html

   <div class="navheader">

5.4.3. Expression based ranker (SPH\_RANK\_EXPR)
`Prev <builtin-rankers.html>`__ 
5.4. Search results ranking
 `Next <ranking-factors.html>`__

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

.. rubric:: 5.4.3. Expression based ranker (SPH\_RANK\_EXPR)
   :name: expression-based-ranker-sph_rank_expr
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Expression ranker, added in version 2.0.2-beta, lets you change the
ranking formula on the fly, on a per-query basis. For a quick kickoff,
this is how you emulate PROXIMITY\_BM25 ranker using the expression
based one:

.. code:: programlisting

    SELECT *, WEIGHT() FROM myindex WHERE MATCH('hello world')
    OPTION ranker=expr('sum(lcs*user_weight)*1000+bm25')

The output of this query must not change if you omit the ``OPTION``
clause, because the default ranker (PROXIMITY\_BM25) behaves exactly
like specified in the ranker formula above. But the expression ranker is
somewhat more flexible than just that and provides access to many more
factors.

The ranking formula is an arbitrary arithmetic expression that can use
constants, document attributes, built-in functions and operators
(described in `Section 5.5, “Expressions, functions, and
operators” <expressions.html>`__), and also a few ranking-specific
things that are only accessible in a ranking formula. Namely, those are
field aggregation functions, field-level, and document-level ranking
factors.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+---------------------------+------------------------------------------------+
| `Prev <builtin-rankers.html>`__      | `Up <weighting.html>`__   |  `Next <ranking-factors.html>`__               |
+--------------------------------------+---------------------------+------------------------------------------------+
| 5.4.2. Available built-in rankers    | `Home <index.html>`__     |  5.4.4. Quick summary of the ranking factors   |
+--------------------------------------+---------------------------+------------------------------------------------+

.. raw:: html

   </div>
