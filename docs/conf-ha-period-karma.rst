.. raw:: html

   <div class="navheader">

12.4.41. ha\_period\_karma
`Prev <conf-ha-ping-interval.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-persistent-connections-limit.html>`__

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

.. rubric:: 12.4.41. ha\_period\_karma
   :name: ha_period_karma
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Agent mirror statistics window size, in seconds. Optional, default is
60. Added in 2.1.1-beta.

For a distributed index with agent mirrors in it (see more in ???),
master tracks several different per-mirror counters. These counters are
then used for failover and balancing. (Master picks the best mirror to
use based on the counters.) Counters are accumulated in blocks of
``ha_period_karma`` seconds.

After beginning a new block, master may still use the accumulated values
from the previous one, until the new one is half full. Thus, any
previous history stops affecting the mirror choice after 1.5 times
ha\_period\_karma seconds at most.

Despite that at most 2 blocks are used for mirror selection, upto 15
last blocks are actually stored, for instrumentation purposes. They can
be inspected using `SHOW AGENT
STATUS <sphinxql-show-agent-status.html>`__ statement.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    ha_period_karma = 120

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------+------------------------------------------------------+
| `Prev <conf-ha-ping-interval.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-persistent-connections-limit.html>`__   |
+------------------------------------------+-----------------------------------+------------------------------------------------------+
| 12.4.40. ha\_ping\_interval              | `Home <index.html>`__             |  12.4.42. persistent\_connections\_limit             |
+------------------------------------------+-----------------------------------+------------------------------------------------------+

.. raw:: html

   </div>
