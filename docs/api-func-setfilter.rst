.. raw:: html

   <div class="navheader">

9.4.2. SetFilter
`Prev <api-func-setidrange.html>`__ 
9.4. Result set filtering settings
 `Next <api-func-setfilterrange.html>`__

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

.. rubric:: 9.4.2. SetFilter
   :name: setfilter
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetFilter ( $attribute, $values, $exclude=false
)

Adds new integer values set filter.

On this call, additional new filter is added to the existing list of
filters. ``$attribute`` must be a string with attribute name.
``$values`` must be a plain array containing integer values.
``$exclude`` must be a boolean value; it controls whether to accept the
matching documents (default mode, when ``$exclude`` is false) or reject
them.

Only those documents where ``$attribute`` column value stored in the
index matches any of the values from ``$values`` array will be matched
(or rejected, if ``$exclude`` is true).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+-----------------------------------------+--------------------------------------------+
| `Prev <api-func-setidrange.html>`__    | `Up <api-funcgroup-filtering.html>`__   |  `Next <api-func-setfilterrange.html>`__   |
+----------------------------------------+-----------------------------------------+--------------------------------------------+
| 9.4.1. SetIDRange                      | `Home <index.html>`__                   |  9.4.3. SetFilterRange                     |
+----------------------------------------+-----------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
