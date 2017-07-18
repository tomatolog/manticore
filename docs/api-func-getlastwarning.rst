.. raw:: html

   <div class="navheader">

9.1.2. GetLastWarning
`Prev <api-func-getlasterror.html>`__ 
9.1. General API functions
 `Next <api-func-setserver.html>`__

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

.. rubric:: 9.1.2. GetLastWarning
   :name: getlastwarning
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function GetLastWarning ()

Returns last warning message, as a string, in human readable format. If
there were no warnings during the previous API call, empty string is
returned.

You should call it to verify whether your request (such as
`Query() <api-func-query.html>`__) was completed but with warnings. For
instance, search query against a distributed index might complete
successfully even if several remote agents timed out. In that case, a
warning message would be produced.

The warning message is *not* reset by this call; so you can safely call
it several times if needed.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------------------+---------------------------------------+
| `Prev <api-func-getlasterror.html>`__    | `Up <api-funcgroup-general.html>`__   |  `Next <api-func-setserver.html>`__   |
+------------------------------------------+---------------------------------------+---------------------------------------+
| 9.1.1. GetLastError                      | `Home <index.html>`__                 |  9.1.3. SetServer                     |
+------------------------------------------+---------------------------------------+---------------------------------------+

.. raw:: html

   </div>
