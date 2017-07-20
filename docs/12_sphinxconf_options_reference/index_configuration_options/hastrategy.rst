ha\_strategy
~~~~~~~~~~~~

Agent mirror selection strategy, for load balancing. Optional, default
is random.

The strategy used for mirror selection, or in other words, choosing a
specific `agent mirror <../../index_configuration_options/agent.md>`__
in a distributed index. Essentially, this directive controls how exactly
master does the load balancing between the configured mirror agent
nodes. The following strategies are implemented:

Simple random balancing
^^^^^^^^^^^^^^^^^^^^^^^

::

    ha_strategy = random

The default balancing mode. Simple linear random distribution among the
mirrors. That is, equal selection probability are assigned to every
mirror. Kind of similar to round-robin (RR), but unlike RR, does not
impose a strict selection order.

Adaptive randomized balancing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default simple random strategy does not take mirror status, error
rate, and, most importantly, actual response latencies into account. So
to accommodate for heterogeneous clusters and/or temporary spikes in
agent node load, we have a group of balancing strategies that
dynamically adjusts the probabilities based on the actual query
latencies observed by the master.

The adaptive strategies based on <b>latency-weighted probabilities</b>
basically work as follows:

-  latency stats are accumulated, in blocks of ha\_period\_karma
   seconds;

-  once per karma period, latency-weighted probabilities get recomputed;

-  once per request (including ping requests), “dead or alive” flag is
   adjusted.

Currently, we begin with equal probabilities (or percentages, for
brevity), and on every step, scale them by the inverse of the latencies
observed during the last “karma” period, and then renormalize them. For
example, if during the first 60 seconds after the master startup 4
mirrors had latencies of 10, 5, 30, and 3 msec/query respectively, the
first adjustment step would go as follow:

-  initial percentages: 0.25, 0.25, 0.25, 0.2%;

-  observed latencies: 10 ms, 5 ms, 30 ms, 3 ms;

-  inverse latencies: 0.1, 0.2, 0.0333, 0.333;

-  scaled percentages: 0.025, 0.05, 0.008333, 0.0833;

-  renormalized percentages: 0.15, 0.30, 0.05, 0.50.

Meaning that the 1st mirror would have a 15% chance of being chosen
during the next karma period, the 2nd one a 30% chance, the 3rd one
(slowest at 30 ms) only a 5% chance, and the 4th and the fastest one (at
3 ms) a 50% chance. Then, after that period, the second adjustment step
would update those chances again, and so on.

The rationale here is, once the <b>observed latencies</b> stabilize, the
<b>latency weighted probabilities</b> stabilize as well. So all these
adjustment iterations are supposed to converge at a point where the
average latencies are (roughly) equal over all mirrors.

::

    ha_strategy = nodeads

Latency-weighted probabilities, but dead mirrors are excluded from the
selection. “Dead” mirror is defined as a mirror that resulted in
multiple hard errors (eg. network failure, or no answer, etc) in a row.

::

    ha_strategy = noerrors

Latency-weighted probabilities, but mirrors with worse errors/success
ratio are excluded from the selection.

Round-robin balancing
^^^^^^^^^^^^^^^^^^^^^

::

    ha_strategy = roundrobin

Simple round-robin selection, that is, selecting the 1st mirror in the
list, then the 2nd one, then the 3rd one, etc, and then repeating the
process once the last mirror in the list is reached. Unlike with the
randomized strategies, RR imposes a strict querying order (1, 2, 3, ..,
N-1, N, 1, 2, 3, … and so on) and *guarantees* that no two subsequent
queries will be sent to the same mirror.
