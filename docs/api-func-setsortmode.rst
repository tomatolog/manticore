.. raw:: html

   <div class="navheader">

9.3.3. SetSortMode
`Prev <api-func-setrankingmode.html>`__ 
9.3. Full-text search query settings
 `Next <api-func-setweights.html>`__

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

.. rubric:: 9.3.3. SetSortMode
   :name: setsortmode
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetSortMode ( $mode, $sortby=“” )

Set matches sorting mode, as described in `Section 5.6, “Sorting
modes” <sorting-modes.html>`__. Parameter must be a constant specifying
one of the known modes.

**WARNING:** (PHP specific) you **must not** take the matching mode
constant name in quotes, that syntax specifies a string and is
incorrect:

.. code:: programlisting

    $cl->SetSortMode ( "SPH_SORT_ATTR_DESC" ); // INCORRECT! will not work as expected
    $cl->SetSortMode ( SPH_SORT_ATTR_ASC ); // correct, works OK

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+-------------------------------------------------------+----------------------------------------+
| `Prev <api-func-setrankingmode.html>`__    | `Up <api-funcgroup-fulltext-query-settings.html>`__   |  `Next <api-func-setweights.html>`__   |
+--------------------------------------------+-------------------------------------------------------+----------------------------------------+
| 9.3.2. SetRankingMode                      | `Home <index.html>`__                                 |  9.3.4. SetWeights                     |
+--------------------------------------------+-------------------------------------------------------+----------------------------------------+

.. raw:: html

   </div>
