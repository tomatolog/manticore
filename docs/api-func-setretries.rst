.. raw:: html

   <div class="navheader">

9.1.4. SetRetries
`Prev <api-func-setserver.html>`__ 
9.1. General API functions
 `Next <api-func-setconnecttimeout.html>`__

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

.. rubric:: 9.1.4. SetRetries
   :name: setretries
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetRetries ( $count, $delay=0 )

Sets distributed retry count and delay.

On temporary failures ``searchd`` will attempt up to ``$count`` retries
per agent. ``$delay`` is the delay between the retries, in milliseconds.
Retries are disabled by default. Note that this call will **not** make
the API itself retry on temporary failure; it only tells ``searchd`` to
do so. Currently, the list of temporary failures includes all kinds of
connect() failures and maxed out (too busy) remote agents.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------------+-----------------------------------------------+
| `Prev <api-func-setserver.html>`__    | `Up <api-funcgroup-general.html>`__   |  `Next <api-func-setconnecttimeout.html>`__   |
+---------------------------------------+---------------------------------------+-----------------------------------------------+
| 9.1.3. SetServer                      | `Home <index.html>`__                 |  9.1.5. SetConnectTimeout                     |
+---------------------------------------+---------------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
