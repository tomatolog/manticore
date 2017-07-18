.. raw:: html

   <div class="navheader">

9.4.6. SetFilterString
`Prev <api-func-setgeoanchor.html>`__ 
9.4. Result set filtering settings
 `Next <api-funcgroup-groupby.html>`__

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

.. rubric:: 9.4.6. SetFilterString
   :name: setfilterstring
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetFilterString ( $attribute, $value,
$exclude=false )

Adds new string value filter.

On this call, additional new filter is added to the existing list of
filters. ``$attribute`` must be a string with attribute name. ``$value``
must be a string. ``$exclude`` must be a boolean value; it controls
whether to accept the matching documents (default mode, when
``$exclude`` is false) or reject them.

Only those documents where ``$attribute`` column value stored in the
index matches string value from ``$value`` will be matched (or rejected,
if ``$exclude`` is true).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------------+------------------------------------------+
| `Prev <api-func-setgeoanchor.html>`__    | `Up <api-funcgroup-filtering.html>`__   |  `Next <api-funcgroup-groupby.html>`__   |
+------------------------------------------+-----------------------------------------+------------------------------------------+
| 9.4.5. SetGeoAnchor                      | `Home <index.html>`__                   |  9.5. GROUP BY settings                  |
+------------------------------------------+-----------------------------------------+------------------------------------------+

.. raw:: html

   </div>
