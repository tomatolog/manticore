.. raw:: html

   <div class="navheader">

9.2.2. SetMaxQueryTime
`Prev <api-func-setlimits.html>`__ 
9.2. General query settings
 `Next <api-func-setoverride.html>`__

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

.. rubric:: 9.2.2. SetMaxQueryTime
   :name: setmaxquerytime
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetMaxQueryTime ( $max\_query\_time )

Sets maximum search query time, in milliseconds. Parameter must be a
non-negative integer. Default value is 0 which means “do not limit”.

Similar to ``$cutoff`` setting from
`SetLimits() <api-func-setlimits.html>`__, but limits elapsed query time
instead of processed matches count. Local search queries will be stopped
once that much time has elapsed. Note that if you’re performing a search
which queries several local indexes, this limit applies to each index
separately.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+------------------------------------------------------+-----------------------------------------+
| `Prev <api-func-setlimits.html>`__    | `Up <api-funcgroup-general-query-settings.html>`__   |  `Next <api-func-setoverride.html>`__   |
+---------------------------------------+------------------------------------------------------+-----------------------------------------+
| 9.2.1. SetLimits                      | `Home <index.html>`__                                |  9.2.3. SetOverride                     |
+---------------------------------------+------------------------------------------------------+-----------------------------------------+

.. raw:: html

   </div>
