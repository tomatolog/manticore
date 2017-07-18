.. raw:: html

   <div class="navheader">

12.2.31. agent
`Prev <conf-local.html>`__ 
12.2. Index configuration options
 `Next <conf-agent-persistent.html>`__

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

.. rubric:: 12.2.31. agent
   :name: agent
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Remote agent declaration in the `distributed
index <distributed.html>`__. Multi-value, optional, default is empty.

``agent`` directive declares remote agents that are searched every time
when the enclosing distributed index is searched. The agents are,
essentially, pointers to networked indexes. Prior to version 2.1.1-beta,
the value format was:

.. code:: programlisting

    agent = address:index-list

Starting with 2.1.1-beta, the value can additionally specify multiple
alternatives (agent mirrors) for either the address only, or the address
and index list:

.. code:: programlisting

    agent = address1 [ | address2 [...] ]:index-list
    agent = address1:index-list [ | address2:index-list [...] ]

In both cases the address specification must be one of the following:

.. code:: programlisting

    address = hostname:port # eg. server2:9312
    address = /absolute/unix/socket/path # eg. /var/run/sphinx2.sock

Where ``hostname`` is the remote host name, ``port`` is the remote TCP
port number, ``index-list`` is a comma-separated list of index names,
and square braces [] designate an optional clause.

In other words, you can point every single agent to one or more remote
indexes, residing on one or more networked servers. There are absolutely
no restrictions on the pointers. To point out a couple important things,
the host can be localhost, and the remote index can be a distributed
index in turn, all that is legal. That enables a bunch of very different
usage modes:

.. raw:: html

   <div class="itemizedlist">

-  sharding over multiple agent servers, and creating an arbitrary
   cluster topology;

-  sharding over multiple agent servers, mirrored for HA/LB (High
   Availability and Load Balancing) purposes (starting with 2.1.1-beta);

-  sharding within localhost, to utilize multiple cores (historical and
   not recommended in versions 1.x and above, use multiple local indexes
   and dist\_threads directive instead);

.. raw:: html

   </div>

All agents are searched in parallel. An index list is passed verbatim to
the remote agent. How exactly that list is searched within the agent
(ie. sequentially or in parallel too) depends solely on the agent
configuration (ie. dist\_threads directive). Master has no remote
control over that.

Starting with 2.2.9-release, the value can additionally enumerate per
agent options such as:

.. raw:: html

   <div class="itemizedlist">

-  `ha\_strategy <conf-ha-strategy.html>`__ - random, roundrobin,
   nodeads, noerrors (replaces index
   `ha\_strategy <conf-ha-strategy.html>`__ for particular agent)

-  `conn <conf-agent-persistent.html>`__ - pconn, persistent (same as
   `agent\_persistent <conf-agent-persistent.html>`__ agent declaration)

-  `blackhole <conf-agent-blackhole.html>`__ - 0,1 (same as
   `agent\_blackhole <conf-agent-blackhole.html>`__ agent declaration)

.. raw:: html

   </div>

.. code:: programlisting

    agent = address1:index-list[[ha_strategy=value] | [conn=value] | [blackhole=value]]

.. rubric:: Example:
   :name: example

.. code:: programlisting

    # config on box2
    # sharding an index over 3 servers
    agent = box2:9312:chunk2
    agent = box3:9312:chunk3

    # config on box2
    # sharding an index over 3 servers
    agent = box1:9312:chunk2
    agent = box3:9312:chunk3

    # config on box3
    # sharding an index over 3 servers
    agent = box1:9312:chunk2
    agent = box2:9312:chunk3

    # per agent options
    agent = box1:9312:chunk1[ha_strategy=nodeads]
    agent = box2:9312:chunk2[conn=pconn]
    agent = test:9312:any[blackhole=1]

.. rubric:: Agent mirrors
   :name: agent-mirrors

New syntax added in 2.1.1-beta lets you define so-called **agent
mirrors** that can be used interchangeably when processing a search
query. Master server keeps track of mirror status (alive or dead) and
response times, and does automatic failover and load balancing based on
that. For example, this line:

.. code:: programlisting

    agent = box1:9312|box2:9312|box3:9312:chunk2

Declares that box1:9312, box2:9312, and box3:9312 all have an index
called chunk2, and can be used as interchangeable mirrors. If any single
of those servers go down, the queries will be distributed between the
other two. When it gets back up, master will detect that and begin
routing queries to all three boxes again.

Another way to define the mirrors is to explicitly specify the index
list for every mirror:

.. code:: programlisting

    agent = box1:9312:box1chunk2|box2:9312:box2chunk2

This works essentially the same as the previous example, but different
index names will be used when querying different severs: box1chunk2 when
querying box1:9312, and box2chunk when querying box2:9312.

By default, all queries are routed to the best of the mirrors. The best
one is picked based on the recent statistics, as controlled by the
`ha\_period\_karma <conf-ha-period-karma.html>`__ config directive.
Master stores a number of metrics (total query count, error count,
response time, etc) recently observed for every agent. It groups those
by time spans, and karma is that time span length. The best agent mirror
is then determined dynamically based on the last 2 such time spans.
Specific algorithm that will be used to pick a mirror can be configured
`ha\_strategy <conf-ha-strategy.html>`__ directive.

The karma period is in seconds and defaults to 60 seconds. Master stores
upto 15 karma spans with per-agent statistics for instrumentation
purposes (see `SHOW AGENT STATUS <sphinxql-show-agent-status.html>`__
statement). However, only the last 2 spans out of those are ever used
for HA/LB logic.

When there are no queries, master sends a regular ping command every
`ha\_ping\_interval <conf-ha-ping-interval.html>`__ milliseconds in
order to have some statistics and at least check, whether the remote
host is still alive. ha\_ping\_interval defaults to 1000 msec. Setting
it to 0 disables pings and statistics will only be accumulated based on
actual queries.

.. rubric:: Example:
   :name: example-1

.. code:: programlisting

    # sharding index over 4 servers total
    # in just 2 chunks but with 2 failover mirrors for each chunk
    # box1, box2 carry chunk1 as local
    # box3, box4 carry chunk2 as local

    # config on box1, box2
    agent = box3:9312|box4:9312:chunk2

    # config on box3, box4
    agent = box1:9312|box2:9312:chunk1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------+---------------------------------+------------------------------------------+
| `Prev <conf-local.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-agent-persistent.html>`__   |
+-------------------------------+---------------------------------+------------------------------------------+
| 12.2.30. local                | `Home <index.html>`__           |  12.2.32. agent\_persistent              |
+-------------------------------+---------------------------------+------------------------------------------+

.. raw:: html

   </div>
