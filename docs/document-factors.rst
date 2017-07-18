.. raw:: html

   <div class="navheader">

5.4.5. Document-level ranking factors
`Prev <ranking-factors.html>`__ 
5.4. Search results ranking
 `Next <field-factors.html>`__

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

.. rubric:: 5.4.5. Document-level ranking factors
   :name: document-level-ranking-factors
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A **document-level factor** is a numeric value computed by the ranking
engine for every matched document with regards to the current query. (So
it differs from a plain document attribute in that the attribute do not
depend on the full text query, while factors might.) Those factors can
be used anywhere in the ranking expression. Currently implemented
document-level factors are:

.. raw:: html

   <div class="itemizedlist">

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

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------+---------------------------+---------------------------------------+
| `Prev <ranking-factors.html>`__                | `Up <weighting.html>`__   |  `Next <field-factors.html>`__        |
+------------------------------------------------+---------------------------+---------------------------------------+
| 5.4.4. Quick summary of the ranking factors    | `Home <index.html>`__     |  5.4.6. Field-level ranking factors   |
+------------------------------------------------+---------------------------+---------------------------------------+

.. raw:: html

   </div>
