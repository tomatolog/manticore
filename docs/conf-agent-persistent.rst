.. raw:: html

   <div class="navheader">

12.2.32. agent\_persistent
`Prev <conf-agent.html>`__ 
12.2. Index configuration options
 `Next <conf-agent-blackhole.html>`__

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

.. rubric:: 12.2.32. agent\_persistent
   :name: agent_persistent
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Persistently connected remote agent declaration. Multi-value, optional,
default is empty. Introduced in version 2.1.1-beta.

``agent_persistent`` directive syntax matches that of the
`agent <conf-agent.html>`__ directive. The only difference is that the
master will **not** open a new connection to the agent for every query
and then close it. Rather, it will keep a connection open and attempt to
reuse for the subsequent queries. The maximal number of such persistent
connections per one agent host is limited by
`persistent\_connections\_limit <conf-persistent-connections-limit.html>`__
option of searchd section.

Note, that you **have** to set the last one in something greater than 0
if you want to use persistent agent connections. Otherwise - when
`persistent\_connections\_limit <conf-persistent-connections-limit.html>`__
is not defined, it assumes the zero num of persistent connections, and
‘agent\_persistent’ acts exactly as simple ‘agent’.

Persistent master-agent connections reduce TCP port pressure, and save
on connection handshakes. As of time of this writing, they are supported
**only** in workers=threads mode. In other modes, simple non-persistent
connections (i.e., one connection per operation) will be used, and a
warning will show up in the console.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    agent_persistent = remotebox:9312:index2

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------+---------------------------------+-----------------------------------------+
| `Prev <conf-agent.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-agent-blackhole.html>`__   |
+-------------------------------+---------------------------------+-----------------------------------------+
| 12.2.31. agent                | `Home <index.html>`__           |  12.2.33. agent\_blackhole              |
+-------------------------------+---------------------------------+-----------------------------------------+

.. raw:: html

   </div>
