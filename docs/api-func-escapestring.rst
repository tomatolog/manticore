.. raw:: html

   <div class="navheader">

9.7.4. EscapeString
`Prev <api-func-buildkeywords.html>`__ 
9.7. Additional functionality
 `Next <api-func-status.html>`__

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

.. rubric:: 9.7.4. EscapeString
   :name: escapestring
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function EscapeString ( $string )

Escapes characters that are treated as special operators by the query
language parser. Returns an escaped string.

``$string`` is a string to escape.

This function might seem redundant because it’s trivial to implement in
any calling application. However, as the set of special characters might
change over time, it makes sense to have an API call that is guaranteed
to escape all such characters at all times.

Usage example:

.. code:: programlisting

    $escaped = $cl->EscapeString ( "escaping-sample@query/string" );

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+--------------------------------------------------------+------------------------------------+
| `Prev <api-func-buildkeywords.html>`__    | `Up <api-funcgroup-additional-functionality.html>`__   |  `Next <api-func-status.html>`__   |
+-------------------------------------------+--------------------------------------------------------+------------------------------------+
| 9.7.3. BuildKeywords                      | `Home <index.html>`__                                  |  9.7.5. Status                     |
+-------------------------------------------+--------------------------------------------------------+------------------------------------+

.. raw:: html

   </div>
