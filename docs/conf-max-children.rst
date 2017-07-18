.. raw:: html

   <div class="navheader">

12.4.8. max\_children
`Prev <conf-sphinxql-timeout.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-net-workers.html>`__

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

.. rubric:: 12.4.8. max\_children
   :name: max_children
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum amount of worker threads (or in other words, concurrent queries
to run in parallel). Optional, default is 0 (unlimited) in
workers=threads, or 1.5 times the CPU cores count in
workers=thread\_pool mode.

max\_children imposes a hard limit on the number of threads working on
user queries. There might still be additional internal threads doing
maintenance tasks, but when it comes to user queries, it is no more than
max\_children concurrent threads (and queries) at all times.

Note that in workers=threads mode a thread is allocated for every
connection rather than an active query. So when there are 100 idle
connections but only 2 active connections with currently running
queries, that still accounts for 102 threads, all of them subject to
max\_children limit. So with a max\_children set way too low, and pooled
connections not reused well enough on the application side, you can
effectively DOS your own server. When the limit is reached, any
additional incoming connections will be dismissed with a temporary
“maxed out” error immediately as they attempt to connect. Thus, in
threads mode you should choose the max\_children limit rather carefully,
with not just the concurrent queries but also with potentially idle
*network connections* in mind.

Now, in workers=thread\_pool mode the network connections are separated
from query processing, so in the example above, 100 idle connections
will all be handled by an internal network thread, and only the 2
actually active queries will be subject to max\_children limit. When the
limit is reached, any additional incoming *connections* will still be
accepted, and any additional *queries* will `get
enqueued <conf-queue-max-length.html>`__ until there are free worker
threads. The queries will only start failing with a temporary Thus, in
thread\_pool mode it makes little sense to raise max\_children much
higher than the amount of CPU cores. Usually that will only hurt CPU
contention and *decrease* the general throughput.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_children = 10

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------+-------------------------------------+
| `Prev <conf-sphinxql-timeout.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-net-workers.html>`__   |
+------------------------------------------+-----------------------------------+-------------------------------------+
| 12.4.7. sphinxql\_timeout                | `Home <index.html>`__             |  12.4.9. net\_workers               |
+------------------------------------------+-----------------------------------+-------------------------------------+

.. raw:: html

   </div>
