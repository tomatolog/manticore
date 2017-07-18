.. raw:: html

   <div class="navheader">

9.4.3. SetFilterRange
`Prev <api-func-setfilter.html>`__ 
9.4. Result set filtering settings
 `Next <api-func-setfilterfloatrange.html>`__

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

.. rubric:: 9.4.3. SetFilterRange
   :name: setfilterrange
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetFilterRange ( $attribute, $min, $max,
$exclude=false )

Adds new integer range filter.

On this call, additional new filter is added to the existing list of
filters. ``$attribute`` must be a string with attribute name. ``$min``
and ``$max`` must be integers that define the acceptable attribute
values range (including the boundaries). ``$exclude`` must be a boolean
value; it controls whether to accept the matching documents (default
mode, when ``$exclude`` is false) or reject them.

Only those documents where ``$attribute`` column value stored in the
index is between ``$min`` and ``$max`` (including values that are
exactly equal to ``$min`` or ``$max``) will be matched (or rejected, if
``$exclude`` is true).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+-----------------------------------------+-------------------------------------------------+
| `Prev <api-func-setfilter.html>`__    | `Up <api-funcgroup-filtering.html>`__   |  `Next <api-func-setfilterfloatrange.html>`__   |
+---------------------------------------+-----------------------------------------+-------------------------------------------------+
| 9.4.2. SetFilter                      | `Home <index.html>`__                   |  9.4.4. SetFilterFloatRange                     |
+---------------------------------------+-----------------------------------------+-------------------------------------------------+

.. raw:: html

   </div>
