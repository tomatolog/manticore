.. raw:: html

   <div class="navheader">

9.1.5. SetConnectTimeout
`Prev <api-func-setretries.html>`__ 
9.1. General API functions
 `Next <api-func-setarrayresult.html>`__

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

.. rubric:: 9.1.5. SetConnectTimeout
   :name: setconnecttimeout
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetConnectTimeout ( $timeout )

Sets the time allowed to spend connecting to the server before giving
up.

Under some circumstances, the server can be delayed in responding,
either due to network delays, or a query backlog. In either instance,
this allows the client application programmer some degree of control
over how their program interacts with ``searchd`` when not available,
and can ensure that the client application does not fail due to
exceeding the script execution limits (especially in PHP).

In the event of a failure to connect, an appropriate error code should
be returned back to the application in order for application-level error
handling to advise the user.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+---------------------------------------+--------------------------------------------+
| `Prev <api-func-setretries.html>`__    | `Up <api-funcgroup-general.html>`__   |  `Next <api-func-setarrayresult.html>`__   |
+----------------------------------------+---------------------------------------+--------------------------------------------+
| 9.1.4. SetRetries                      | `Home <index.html>`__                 |  9.1.6. SetArrayResult                     |
+----------------------------------------+---------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
