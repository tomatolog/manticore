.. raw:: html

   <div class="navheader">

9.3.6. SetIndexWeights
`Prev <api-func-setfieldweights.html>`__ 
9.3. Full-text search query settings
 `Next <api-funcgroup-filtering.html>`__

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

.. rubric:: 9.3.6. SetIndexWeights
   :name: setindexweights
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetIndexWeights ( $weights )

Sets per-index weights, and enables weighted summing of match weights
across different indexes. Parameter must be a hash (associative array)
mapping string index names to integer weights. Default is empty array
that means to disable weighting summing.

When a match with the same document ID is found in several different
local indexes, by default Sphinx simply chooses the match from the index
specified last in the query. This is to support searching through
partially overlapping index partitions.

However in some cases the indexes are not just partitions, and you might
want to sum the weights across the indexes instead of picking one.
``SetIndexWeights()`` lets you do that. With summing enabled, final
match weight in result set will be computed as a sum of match weight
coming from the given index multiplied by respective per-index weight
specified in this call. Ie. if the document 123 is found in index A with
the weight of 2, and also in index B with the weight of 3, and you
called ``SetIndexWeights ( array ( "A"=>100, "B"=>10 ) )``, the final
weight return to the client will be 2\*100+3\*10 = 230.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+-------------------------------------------------------+--------------------------------------------+
| `Prev <api-func-setfieldweights.html>`__    | `Up <api-funcgroup-fulltext-query-settings.html>`__   |  `Next <api-funcgroup-filtering.html>`__   |
+---------------------------------------------+-------------------------------------------------------+--------------------------------------------+
| 9.3.5. SetFieldWeights                      | `Home <index.html>`__                                 |  9.4. Result set filtering settings        |
+---------------------------------------------+-------------------------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
