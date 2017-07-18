.. raw:: html

   <div class="navheader">

9.3.1. SetMatchMode
`Prev <api-funcgroup-fulltext-query-settings.html>`__ 
9.3. Full-text search query settings
 `Next <api-func-setrankingmode.html>`__

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

.. rubric:: 9.3.1. SetMatchMode
   :name: setmatchmode
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**DEPRECATED**

**Prototype:** function SetMatchMode ( $mode )

Sets full-text query matching mode, as described in `Section 5.1,
“Matching modes” <matching-modes.html>`__. Parameter must be a constant
specifying one of the known modes.

**WARNING:** (PHP specific) you **must not** take the matching mode
constant name in quotes, that syntax specifies a string and is
incorrect:

.. code:: programlisting

    $cl->SetMatchMode ( "SPH_MATCH_ANY" ); // INCORRECT! will not work as expected
    $cl->SetMatchMode ( SPH_MATCH_ANY ); // correct, works OK

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------------------+-------------------------------------------------------+--------------------------------------------+
| `Prev <api-funcgroup-fulltext-query-settings.html>`__    | `Up <api-funcgroup-fulltext-query-settings.html>`__   |  `Next <api-func-setrankingmode.html>`__   |
+----------------------------------------------------------+-------------------------------------------------------+--------------------------------------------+
| 9.3. Full-text search query settings                     | `Home <index.html>`__                                 |  9.3.2. SetRankingMode                     |
+----------------------------------------------------------+-------------------------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
