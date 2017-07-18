.. raw:: html

   <div class="navheader">

5.4.8. Formula expressions for all the built-in rankers
`Prev <factor-aggr-functions.html>`__ 
5.4. Search results ranking
 `Next <expressions.html>`__

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

.. rubric:: 5.4.8. Formula expressions for all the built-in rankers
   :name: formula-expressions-for-all-the-built-in-rankers
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Most of the other rankers can actually be emulated with the expression
based ranker. You just need to pass a proper expression. Such emulation
is, of course, going to be slower than using the built-in, compiled
ranker but still might be of interest if you want to fine-tune your
ranking formula starting with one of the existing ones. Also, the
formulas define the nitty gritty ranker details in a nicely readable
fashion.

.. raw:: html

   <div class="itemizedlist">

-  SPH\_RANK\_PROXIMITY\_BM25 = sum(lcs\*user\_weight)\*1000+bm25

-  SPH\_RANK\_BM25 = bm25

-  SPH\_RANK\_NONE = 1

-  SPH\_RANK\_WORDCOUNT = sum(hit\_count\*user\_weight)

-  SPH\_RANK\_PROXIMITY = sum(lcs\*user\_weight)

-  SPH\_RANK\_MATCHANY =
   sum((word\_count+(lcs-1)\*max\_lcs)\*user\_weight)

-  SPH\_RANK\_FIELDMASK = field\_mask

-  SPH\_RANK\_SPH04 =
   sum((4\*lcs+2\*(min\_hit\_pos==1)+exact\_hit)\*user\_weight)\*1000+bm25

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------+---------------------------+-----------------------------------------------+
| `Prev <factor-aggr-functions.html>`__          | `Up <weighting.html>`__   |  `Next <expressions.html>`__                  |
+------------------------------------------------+---------------------------+-----------------------------------------------+
| 5.4.7. Ranking factor aggregation functions    | `Home <index.html>`__     |  5.5. Expressions, functions, and operators   |
+------------------------------------------------+---------------------------+-----------------------------------------------+

.. raw:: html

   </div>
