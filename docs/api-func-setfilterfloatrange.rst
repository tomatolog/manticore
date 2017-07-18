.. raw:: html

   <div class="navheader">

9.4.4. SetFilterFloatRange
`Prev <api-func-setfilterrange.html>`__ 
9.4. Result set filtering settings
 `Next <api-func-setgeoanchor.html>`__

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

.. rubric:: 9.4.4. SetFilterFloatRange
   :name: setfilterfloatrange
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetFilterFloatRange ( $attribute, $min, $max,
$exclude=false )

Adds new float range filter.

On this call, additional new filter is added to the existing list of
filters. ``$attribute`` must be a string with attribute name. ``$min``
and ``$max`` must be floats that define the acceptable attribute values
range (including the boundaries). ``$exclude`` must be a boolean value;
it controls whether to accept the matching documents (default mode, when
``$exclude`` is false) or reject them.

Only those documents where ``$attribute`` column value stored in the
index is between ``$min`` and ``$max`` (including values that are
exactly equal to ``$min`` or ``$max``) will be matched (or rejected, if
``$exclude`` is true).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+-----------------------------------------+------------------------------------------+
| `Prev <api-func-setfilterrange.html>`__    | `Up <api-funcgroup-filtering.html>`__   |  `Next <api-func-setgeoanchor.html>`__   |
+--------------------------------------------+-----------------------------------------+------------------------------------------+
| 9.4.3. SetFilterRange                      | `Home <index.html>`__                   |  9.4.5. SetGeoAnchor                     |
+--------------------------------------------+-----------------------------------------+------------------------------------------+

.. raw:: html

   </div>
