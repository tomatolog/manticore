.. raw:: html

   <div class="navheader">

9.7.5. Status
`Prev <api-func-escapestring.html>`__ 
9.7. Additional functionality
 `Next <api-func-flushattributes.html>`__

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

.. rubric:: 9.7.5. Status
   :name: status
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function Status ()

Queries searchd status, and returns an array of status variable name and
value pairs.

Usage example:

.. code:: programlisting

    $status = $cl->Status ();
    foreach ( $status as $row )
        print join ( ": ", $row ) . "\n";

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+--------------------------------------------------------+---------------------------------------------+
| `Prev <api-func-escapestring.html>`__    | `Up <api-funcgroup-additional-functionality.html>`__   |  `Next <api-func-flushattributes.html>`__   |
+------------------------------------------+--------------------------------------------------------+---------------------------------------------+
| 9.7.4. EscapeString                      | `Home <index.html>`__                                  |  9.7.6. FlushAttributes                     |
+------------------------------------------+--------------------------------------------------------+---------------------------------------------+

.. raw:: html

   </div>
