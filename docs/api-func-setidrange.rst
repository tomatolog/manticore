.. raw:: html

   <div class="navheader">

9.4.1. SetIDRange
`Prev <api-funcgroup-filtering.html>`__ 
9.4. Result set filtering settings
 `Next <api-func-setfilter.html>`__

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

.. rubric:: 9.4.1. SetIDRange
   :name: setidrange
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetIDRange ( $min, $max )

Sets an accepted range of document IDs. Parameters must be integers.
Defaults are 0 and 0; that combination means to not limit by range.

After this call, only those records that have document ID between
``$min`` and ``$max`` (including IDs exactly equal to ``$min`` or
``$max``) will be matched.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+-----------------------------------------+---------------------------------------+
| `Prev <api-funcgroup-filtering.html>`__    | `Up <api-funcgroup-filtering.html>`__   |  `Next <api-func-setfilter.html>`__   |
+--------------------------------------------+-----------------------------------------+---------------------------------------+
| 9.4. Result set filtering settings         | `Home <index.html>`__                   |  9.4.2. SetFilter                     |
+--------------------------------------------+-----------------------------------------+---------------------------------------+

.. raw:: html

   </div>
