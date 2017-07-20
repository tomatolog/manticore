ha\_ping\_interval
~~~~~~~~~~~~~~~~~~

Interval between agent mirror pings, in milliseconds. Optional, default
is 1000.

For a distributed index with agent mirrors in it (see more in `remote
agents <../../index_configuration_options/agent.md>`__), master sends
all mirrors a ping command during the idle periods. This is to track the
current agent status (alive or dead, network roundtrip, etc). The
interval between such pings is defined by this directive.

To disable pings, set ha\_ping\_interval to 0.

Example:
^^^^^^^^

::


    ha_ping_interval = 0

