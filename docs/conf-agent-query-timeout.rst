.. raw:: html

   <div class="navheader">

12.2.35. agent\_query\_timeout
`Prev <conf-agent-connect-timeout.html>`__ 
12.2. Index configuration options
 `Next <conf-preopen.html>`__

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

.. rubric:: 12.2.35. agent\_query\_timeout
   :name: agent_query_timeout
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Remote agent query timeout, in milliseconds. Optional, default is 3000
(ie. 3 seconds). Added in version 2.1.1-beta.

After connection, ``searchd`` will wait at most this much time for
remote queries to complete. This timeout is fully separate from
connection timeout; so the maximum possible delay caused by a remote
agent equals to the sum of ``agent_connection_timeout`` and
``agent_query_timeout``. Queries will **not** be retried if this timeout
is reached; a warning will be produced instead.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    agent_query_timeout = 10000 # our query can be long, allow up to 10 sec

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+---------------------------------+---------------------------------+
| `Prev <conf-agent-connect-timeout.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-preopen.html>`__   |
+-----------------------------------------------+---------------------------------+---------------------------------+
| 12.2.34. agent\_connect\_timeout              | `Home <index.html>`__           |  12.2.36. preopen               |
+-----------------------------------------------+---------------------------------+---------------------------------+

.. raw:: html

   </div>
