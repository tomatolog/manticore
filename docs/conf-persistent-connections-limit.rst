.. raw:: html

   <div class="navheader">

12.4.42. persistent\_connections\_limit
`Prev <conf-ha-period-karma.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-rt-merge-iops.html>`__

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

.. rubric:: 12.4.42. persistent\_connections\_limit
   :name: persistent_connections_limit
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The maximum # of simultaneous persistent connections to remote
`persistent agents <conf-agent-persistent.html>`__. Each time connecting
agent defined under ‘agent\_persistent’ we try to reuse existing
connection (if any), or connect and save the connection for the future.
However we can’t hold unlimited # of such persistent connections, since
each one holds a worker on agent size (and finally we’ll receive the
‘maxed out’ error, when all of them are busy). This very directive
limits the number. It affects the num of connections to each agent’s
host, across all distributed indexes.

It is reasonable to set the value equal or less than
`max\_children <conf-max-children.html>`__ option of the agents.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    persistent_connections_limit = 29 # assume that each host of agents has max_children = 30 (or 29).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+-----------------------------------+---------------------------------------+
| `Prev <conf-ha-period-karma.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-rt-merge-iops.html>`__   |
+-----------------------------------------+-----------------------------------+---------------------------------------+
| 12.4.41. ha\_period\_karma              | `Home <index.html>`__             |  12.4.43. rt\_merge\_iops             |
+-----------------------------------------+-----------------------------------+---------------------------------------+

.. raw:: html

   </div>
