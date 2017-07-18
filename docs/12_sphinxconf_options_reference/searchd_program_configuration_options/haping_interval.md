### ha_ping_interval {#ha-ping-interval}

Interval between agent mirror pings, in milliseconds. Optional, default is 1000. Added in 2.1.1-beta.

For a distributed index with agent mirrors in it (see more in ???), master sends all mirrors a ping command during the idle periods. This is to track the current agent status (alive or dead, network roundtrip, etc). The interval between such pings is defined by this directive.

To disable pings, set ha_ping_interval to 0.

#### Example: {#example}

```

ha_ping_interval = 0

```