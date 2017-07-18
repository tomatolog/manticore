.. raw:: html

   <div class="navheader">

12.2.33. agent\_blackhole
`Prev <conf-agent-persistent.html>`__ 
12.2. Index configuration options
 `Next <conf-agent-connect-timeout.html>`__

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

.. rubric:: 12.2.33. agent\_blackhole
   :name: agent_blackhole
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Remote blackhole agent declaration in the `distributed
index <distributed.html>`__. Multi-value, optional, default is empty.
Introduced in version 0.9.9-rc1.

``agent_blackhole`` lets you fire-and-forget queries to remote agents.
That is useful for debugging (or just testing) production clusters: you
can setup a separate debugging/testing searchd instance, and forward the
requests to this instance from your production master (aggregator)
instance without interfering with production work. Master searchd will
attempt to connect and query blackhole agent normally, but it will
neither wait nor process any responses. Also, all network errors on
blackhole agents will be ignored. The value format is completely
identical to regular `agent <conf-agent.html>`__ directive.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    agent_blackhole = testbox:9312:testindex1,testindex2

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------------+-----------------------------------------------+
| `Prev <conf-agent-persistent.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-agent-connect-timeout.html>`__   |
+------------------------------------------+---------------------------------+-----------------------------------------------+
| 12.2.32. agent\_persistent               | `Home <index.html>`__           |  12.2.34. agent\_connect\_timeout             |
+------------------------------------------+---------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
