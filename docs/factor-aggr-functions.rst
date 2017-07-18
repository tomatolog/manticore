.. raw:: html

   <div class="navheader">

5.4.7. Ranking factor aggregation functions
`Prev <field-factors.html>`__ 
5.4. Search results ranking
 `Next <formulas-for-builtin-rankers.html>`__

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

.. rubric:: 5.4.7. Ranking factor aggregation functions
   :name: ranking-factor-aggregation-functions
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A **field aggregation function** is a single argument function that
takes an expression with field-level factors, iterates it over all the
matched fields, and computes the final results. Currently implemented
field aggregation functions are:

.. raw:: html

   <div class="itemizedlist">

-  ``sum``, sums the argument expression over all matched fields. For
   instance, ``sum(1)`` should return a number of matched fields.

-  ``top``, returns the greatest value of the argument over all matched
   fields.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------+------------------------------------------------------------+
| `Prev <field-factors.html>`__         | `Up <weighting.html>`__   |  `Next <formulas-for-builtin-rankers.html>`__              |
+---------------------------------------+---------------------------+------------------------------------------------------------+
| 5.4.6. Field-level ranking factors    | `Home <index.html>`__     |  5.4.8. Formula expressions for all the built-in rankers   |
+---------------------------------------+---------------------------+------------------------------------------------------------+

.. raw:: html

   </div>
