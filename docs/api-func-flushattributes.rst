.. raw:: html

   <div class="navheader">

9.7.6. FlushAttributes
`Prev <api-func-status.html>`__ 
9.7. Additional functionality
 `Next <api-funcgroup-pconn.html>`__

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

.. rubric:: 9.7.6. FlushAttributes
   :name: flushattributes
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function FlushAttributes ()

Forces ``searchd`` to flush pending attribute updates to disk, and
blocks until completion. Returns a non-negative internal “flush tag” on
success. Returns -1 and sets an error message on error. Introduced in
version 1.10-beta.

Attribute values updated using
`UpdateAttributes() <api-func-updateatttributes.html>`__ API call are
only kept in RAM until a so-called flush (which writes the current,
possibly updated attribute values back to disk). FlushAttributes() call
lets you enforce a flush. The call will block until ``searchd`` finishes
writing the data to disk, which might take seconds or even minutes
depending on the total data size (.spa file size). All the currently
updated indexes will be flushed.

Flush tag should be treated as an ever growing magic number that does
not mean anything. It’s guaranteed to be non-negative. It is guaranteed
to grow over time, though not necessarily in a sequential fashion; for
instance, two calls that return 10 and then 1000 respectively are a
valid situation. If two calls to FlushAttrs() return the same tag, it
means that there were no actual attribute updates in between them, and
therefore current flushed state remained the same (for all indexes).

Usage example:

.. code:: programlisting

    $status = $cl->FlushAttributes ();
    if ( $status<0 )
        print "ERROR: " . $cl->GetLastError();

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------+--------------------------------------------------------+----------------------------------------+
| `Prev <api-func-status.html>`__    | `Up <api-funcgroup-additional-functionality.html>`__   |  `Next <api-funcgroup-pconn.html>`__   |
+------------------------------------+--------------------------------------------------------+----------------------------------------+
| 9.7.5. Status                      | `Home <index.html>`__                                  |  9.8. Persistent connections           |
+------------------------------------+--------------------------------------------------------+----------------------------------------+

.. raw:: html

   </div>
