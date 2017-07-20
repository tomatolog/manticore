agent
~~~~~

Remote agent declaration in the `distributed
index <../../distributed_searching.md>`__. Multi-value, optional,
default is empty.

``agent`` directive declares remote agents that are searched every time
when the enclosing distributed index is searched. The agents are,
essentially, pointers to networked indexes. The value specifies address,
and also can additionally specify multiple alternatives (agent mirrors)
for either the address only, or the address and index list:

::


    agent = address1 [ | address2 [...] ][:index-list]
    agent = address1[:index-list [ | address2[:index-list [...] ] ] ]

In both cases the address specification must be one of the following:

::


    address = hostname[:port] # eg. server2:9312
    address = /absolute/unix/socket/path # eg. /var/run/sphinx2.sock

Where ``hostname`` is the remote host name, ``port`` is the remote TCP
port number, ``index-list`` is a comma-separated list of index names,
and square braces [] designate an optional clause.

When index name is omited, it is assumed the same index as the one where
this line is defined. I.e. when defining agents for distributed index
‘mycoolindex’ you can just point the address, and it is assumed to calll
‘mycoolindex’ index on agent's endpoints.

When port number is omited, it is assumed to be default sphinxql IANA
port (9312). However when portnumber is pointed, but invalid (say, port
70000), it will fail (skip) such agent.

In other words, you can point every single agent to one or more remote
indexes, residing on one or more networked servers. There are absolutely
no restrictions on the pointers. To point out a couple important things,
the host can be localhost, and the remote index can be a distributed
index in turn, all that is legal. That enables a bunch of very different
usage modes:

-  sharding over multiple agent servers, and creating an arbitrary
   cluster topology;

-  sharding over multiple agent servers, mirrored for HA/LB (High
   Availability and Load Balancing) purposes;

-  sharding within localhost, to utilize multiple cores (however, it is
   simpler just to use multiple local indexes and dist\_threads
   directive instead);

All agents are searched in parallel. An index list is passed verbatim to
the remote agent. How exactly that list is searched within the agent
(ie. sequentially or in parallel too) depends solely on the agent
configuration (ie. dist\_threads directive). Master has no remote
control over that.

The value can additionally enumerate per agent options such as:

-  `ha\_strategy <../../index_configuration_options/hastrategy.md>`__ -
   random, roundrobin, nodeads, noerrors (replaces index
   `ha\_strategy <../../index_configuration_options/hastrategy.md>`__
   for particular agent)

-  `conn <../../index_configuration_options/agentpersistent.md>`__ -
   pconn, persistent (same as
   `agent\_persistent <../../index_configuration_options/agentpersistent.md>`__
   agent declaration)

-  `blackhole <../../index_configuration_options/agentblackhole.md>`__ -
   0,1 (same as
   `agent\_blackhole <../../index_configuration_options/agentblackhole.md>`__
   agent declaration)

::


    agent = address1:index-list[[ha_strategy=value] | [conn=value] | [blackhole=value]]

Example:
^^^^^^^^

::


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

Agent mirrors
^^^^^^^^^^^^^

The syntax lets you define so-called <b>agent mirrors</b> that can be
used interchangeably when processing a search query. Master server keeps
track of mirror status (alive or dead) and response times, and does
automatic failover and load balancing based on that. For example, this
line:

::


    agent = box1:9312|box2:9312|box3:9312:chunk2

declares that box1:9312, box2:9312, and box3:9312 all have an index
called chunk2, and can be used as interchangeable mirrors. If any single
of those servers go down, the queries will be distributed between the
other two. When it gets back up, master will detect that and begin
routing queries to all three boxes again.

Another way to define the mirrors is to explicitly specify the index
list for every mirror:

::


    agent = box1:9312:box1chunk2|box2:9312:box2chunk2

This works essentially the same as the previous example, but different
index names will be used when querying different severs: box1chunk2 when
querying box1:9312, and box2chunk when querying box2:9312.

By default, all queries are routed to the best of the mirrors. The best
one is picked based on the recent statistics, as controlled by the
`ha\_period\_karma <../../searchd_program_configuration_options/haperiod_karma.md>`__
config directive. Master stores a number of metrics (total query count,
error count, response time, etc) recently observed for every agent. It
groups those by time spans, and karma is that time span length. The best
agent mirror is then determined dynamically based on the last 2 such
time spans. Specific algorithm that will be used to pick a mirror can be
configured
`ha\_strategy <../../index_configuration_options/hastrategy.md>`__
directive.

The karma period is in seconds and defaults to 60 seconds. Master stores
up to 15 karma spans with per-agent statistics for instrumentation
purposes (see `SHOW AGENT STATUS <../../show_agent_status.md>`__
statement). However, only the last 2 spans out of those are ever used
for HA/LB logic.

When there are no queries, master sends a regular ping command every
`ha\_ping\_interval <../../searchd_program_configuration_options/haping_interval.md>`__
milliseconds in order to have some statistics and at least check,
whether the remote host is still alive. ha\_ping\_interval defaults to
1000 msec. Setting it to 0 disables pings and statistics will only be
accumulated based on actual queries.

Example:
^^^^^^^^

::


    # sharding index over 4 servers total
    # in just 2 chunks but with 2 failover mirrors for each chunk
    # box1, box2 carry chunk1 as local
    # box3, box4 carry chunk2 as local

    # config on box1, box2
    agent = box3:9312|box4:9312:chunk2

    # config on box3, box4
    agent = box1:9312|box2:9312:chunk1

