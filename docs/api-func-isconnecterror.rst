.. raw:: html

   <div class="navheader">

9.1.7. IsConnectError
`Prev <api-func-setarrayresult.html>`__ 
9.1. General API functions
 `Next <api-funcgroup-general-query-settings.html>`__

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

.. rubric:: 9.1.7. IsConnectError
   :name: isconnecterror
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function IsConnectError ()

Checks whether the last error was a network error on API side, or a
remote error reported by searchd. Returns true if the last connection
attempt to searchd failed on API side, false otherwise (if the error was
remote, or there were no connection attempts at all). Introduced in
version 0.9.9-rc1.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+---------------------------------------+---------------------------------------------------------+
| `Prev <api-func-setarrayresult.html>`__    | `Up <api-funcgroup-general.html>`__   |  `Next <api-funcgroup-general-query-settings.html>`__   |
+--------------------------------------------+---------------------------------------+---------------------------------------------------------+
| 9.1.6. SetArrayResult                      | `Home <index.html>`__                 |  9.2. General query settings                            |
+--------------------------------------------+---------------------------------------+---------------------------------------------------------+

.. raw:: html

   </div>
