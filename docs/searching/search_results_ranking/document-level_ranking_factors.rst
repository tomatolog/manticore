Document-level ranking factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A <b>document-level factor</b> is a numeric value computed by the
ranking engine for every matched document with regards to the current
query. So it differs from a plain document attribute in that the
attribute do not depend on the full text query, while factors might.
Those factors can be used anywhere in the ranking expression. Currently
implemented document-level factors are:

-  ``bm25`` (integer), a document-level BM25 estimate (computed without
   keyword occurrence filtering).

-  ``max_lcs`` (integer), a query-level maximum possible value that the
   sum(lcs\*user\_weight) expression can ever take. This can be useful
   for weight boost scaling. For instance, MATCHANY ranker formula uses
   this to guarantee that a full phrase match in any field ranks higher
   than any combination of partial matches in all fields.

-  ``field_mask`` (integer), a document-level 32-bit mask of matched
   fields.

-  ``query_word_count`` (integer), the number of unique keywords in a
   query, adjusted for a number of excluded keywords. For instance, both
   ``(one one one one)`` and ``(one !two)`` queries should assign a
   value of 1 to this factor, because there is just one unique
   non-excluded keyword.

-  ``doc_word_count`` (integer), the number of unique keywords matched
   in the entire document.
