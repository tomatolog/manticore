.. raw:: html

   <div class="navheader">

12.4.51. agent\_retry\_count
`Prev <conf-agent-query-timeout-default.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-agent-retry-delay.html>`__

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

.. rubric:: 12.4.51. agent\_retry\_count
   :name: agent_retry_count
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Integer, specifies how many times sphinx will try to connect and query
remote agents in distributed index before reporting fatal query error.
Default is 0 (i.e. no retries). This value may be also specified on
per-query basis using ‘OPTION retry\_count=XXX’ clause. If per-query
option exists, it will override the one specified in config.

Note, that if you use `agent mirrors <conf-agent.html>`__ in definition
of your distributed index, then before every attempt of connect sphinx
will select different mirror, according to specified
`ha\_strategy <conf-ha-strategy.html>`__\ specified.

For example, if you have 10 mirrors, and surely know, that at least one
of them alive, then you can definitely take the answer to a correct
query, specifying options ``ha_strategy = roundrobin`` and
``agent_retry_count = 9`` in your config.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------------+-----------------------------------+-------------------------------------------+
| `Prev <conf-agent-query-timeout-default.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-agent-retry-delay.html>`__   |
+-----------------------------------------------------+-----------------------------------+-------------------------------------------+
| 12.4.50. agent\_query\_timeout                      | `Home <index.html>`__             |  12.4.52. agent\_retry\_delay             |
+-----------------------------------------------------+-----------------------------------+-------------------------------------------+

.. raw:: html

   </div>
