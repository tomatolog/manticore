.. raw:: html

   <div class="navheader">

9.1.1. GetLastError
`Prev <api-funcgroup-general.html>`__ 
9.1. General API functions
 `Next <api-func-getlastwarning.html>`__

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

.. rubric:: 9.1.1. GetLastError
   :name: getlasterror
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function GetLastError()

Returns last error message, as a string, in human readable format. If
there were no errors during the previous API call, empty string is
returned.

You should call it when any other function (such as
`Query() <api-func-query.html>`__) fails (typically, the failing
function returns false). The returned string will contain the error
description.

The error message is *not* reset by this call; so you can safely call it
several times if needed.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------------------+--------------------------------------------+
| `Prev <api-funcgroup-general.html>`__    | `Up <api-funcgroup-general.html>`__   |  `Next <api-func-getlastwarning.html>`__   |
+------------------------------------------+---------------------------------------+--------------------------------------------+
| 9.1. General API functions               | `Home <index.html>`__                 |  9.1.2. GetLastWarning                     |
+------------------------------------------+---------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
