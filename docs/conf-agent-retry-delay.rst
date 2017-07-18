.. raw:: html

   <div class="navheader">

12.4.52. agent\_retry\_delay
`Prev <conf-agent-retry-count.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-hostname-lookup.html>`__

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

.. rubric:: 12.4.52. agent\_retry\_delay
   :name: agent_retry_delay
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Integer, in milliseconds. Specifies the delay sphinx rest before
retrying to query a remote agent in case it fails. The value has sense
only if non-zero `agent\_retry\_count <conf-agent-retry-count.html>`__
or non-zero per-query OPTION retry\_count specified. Default is 500.
This value may be also specified on per-query basis using ‘OPTION
retry\_delay=XXX’ clause. If per-query option exists, it will override
the one specified in config.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+-----------------------------------+-----------------------------------------+
| `Prev <conf-agent-retry-count.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-hostname-lookup.html>`__   |
+-------------------------------------------+-----------------------------------+-----------------------------------------+
| 12.4.51. agent\_retry\_count              | `Home <index.html>`__             |  12.4.53. hostname\_lookup              |
+-------------------------------------------+-----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
