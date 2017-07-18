.. raw:: html

   <div class="navheader">

12.4.40. ha\_ping\_interval
`Prev <conf-sphinxql-state.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-ha-period-karma.html>`__

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

.. rubric:: 12.4.40. ha\_ping\_interval
   :name: ha_ping_interval
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Interval between agent mirror pings, in milliseconds. Optional, default
is 1000. Added in 2.1.1-beta.

For a distributed index with agent mirrors in it (see more in ???),
master sends all mirrors a ping command during the idle periods. This is
to track the current agent status (alive or dead, network roundtrip,
etc). The interval between such pings is defined by this directive.

To disable pings, set ha\_ping\_interval to 0.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    ha_ping_interval = 0

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+-----------------------------------+-----------------------------------------+
| `Prev <conf-sphinxql-state.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-ha-period-karma.html>`__   |
+----------------------------------------+-----------------------------------+-----------------------------------------+
| 12.4.39. sphinxql\_state               | `Home <index.html>`__             |  12.4.41. ha\_period\_karma             |
+----------------------------------------+-----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
