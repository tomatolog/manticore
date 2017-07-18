.. raw:: html

   <div class="navheader">

12.4.16. max\_packet\_size
`Prev <conf-attr-flush-period.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-mva-updates-pool.html>`__

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

.. rubric:: 12.4.16. max\_packet\_size
   :name: max_packet_size
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum allowed network packet size. Limits both query packets from
clients, and response packets from remote agents in distributed
environment. Only used for internal sanity checks, does not directly
affect RAM use or performance. Optional, default is 8M. Introduced in
version 0.9.9-rc1.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_packet_size = 32M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-attr-flush-period.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-mva-updates-pool.html>`__   |
+-------------------------------------------+-----------------------------------+------------------------------------------+
| 12.4.15. attr\_flush\_period              | `Home <index.html>`__             |  12.4.17. mva\_updates\_pool             |
+-------------------------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
