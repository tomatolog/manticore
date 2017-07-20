Ranking factor aggregation functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A <b>field aggregation function</b> is a single argument function that
takes an expression with field-level factors, iterates it over all the
matched fields, and computes the final results. Currently implemented
field aggregation functions are:

-  ``sum``, sums the argument expression over all matched fields. For
   instance, ``sum(1)`` should return a number of matched fields.

-  ``top``, returns the greatest value of the argument over all matched
   fields.
