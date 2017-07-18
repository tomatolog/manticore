.. raw:: html

   <div class="navheader">

12.2.34. agent\_connect\_timeout
`Prev <conf-agent-blackhole.html>`__ 
12.2. Index configuration options
 `Next <conf-agent-query-timeout.html>`__

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

.. rubric:: 12.2.34. agent\_connect\_timeout
   :name: agent_connect_timeout
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Remote agent connection timeout, in milliseconds. Optional, default is
1000 (ie. 1 second).

When connecting to remote agents, ``searchd`` will wait at most this
much time for connect() call to complete successfully. If the timeout is
reached but connect() does not complete, and
`retries <api-func-setretries.html>`__ are enabled, retry will be
initiated.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    agent_connect_timeout = 300

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+---------------------------------+---------------------------------------------+
| `Prev <conf-agent-blackhole.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-agent-query-timeout.html>`__   |
+-----------------------------------------+---------------------------------+---------------------------------------------+
| 12.2.33. agent\_blackhole               | `Home <index.html>`__           |  12.2.35. agent\_query\_timeout             |
+-----------------------------------------+---------------------------------+---------------------------------------------+

.. raw:: html

   </div>
