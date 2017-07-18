Expression based ranker (SPH\_RANK\_EXPR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Expression ranker, added in version 2.0.2-beta, lets you change the
ranking formula on the fly, on a per-query basis. For a quick kickoff,
this is how you emulate PROXIMITY\_BM25 ranker using the expression
based one:

::


    SELECT *, WEIGHT() FROM myindex WHERE MATCH('hello world')
    OPTION ranker=expr('sum(lcs*user_weight)*1000+bm25')

The output of this query must not change if you omit the ``OPTION``
clause, because the default ranker (PROXIMITY\_BM25) behaves exactly
like specified in the ranker formula above. But the expression ranker is
somewhat more flexible than just that and provides access to many more
factors.

The ranking formula is an arbitrary arithmetic expression that can use
constants, document attributes, built-in functions and operators
(described in `the section called “Expressions, functions, and
operators” <../../expressions,_functions,_and_operators/README.html>`__),
and also a few ranking-specific things that are only accessible in a
ranking formula. Namely, those are field aggregation functions,
field-level, and document-level ranking factors.
