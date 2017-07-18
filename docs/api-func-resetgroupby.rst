.. raw:: html

   <div class="navheader">

9.6.5. ResetGroupBy
`Prev <api-func-resetfilters.html>`__ 
9.6. Querying
 `Next <api-funcgroup-additional-functionality.html>`__

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

.. rubric:: 9.6.5. ResetGroupBy
   :name: resetgroupby
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function ResetGroupBy ()

Clears all currently group-by settings, and disables group-by.

This call is only normally required when using multi-queries. You can
change individual group-by settings using ``SetGroupBy()`` and
``SetGroupDistinct()`` calls, but you can not disable group-by using
those calls. ``ResetGroupBy()`` fully resets previous group-by settings
and disables group-by mode in the current state, so that subsequent
``AddQuery()`` calls can perform non-grouping searches.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+----------------------------------------+-----------------------------------------------------------+
| `Prev <api-func-resetfilters.html>`__    | `Up <api-funcgroup-querying.html>`__   |  `Next <api-funcgroup-additional-functionality.html>`__   |
+------------------------------------------+----------------------------------------+-----------------------------------------------------------+
| 9.6.4. ResetFilters                      | `Home <index.html>`__                  |  9.7. Additional functionality                            |
+------------------------------------------+----------------------------------------+-----------------------------------------------------------+

.. raw:: html

   </div>
