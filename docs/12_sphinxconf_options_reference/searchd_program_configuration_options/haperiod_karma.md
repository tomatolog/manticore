### ha_period_karma {#ha-period-karma}

Agent mirror statistics window size, in seconds. Optional, default is 60. Added in 2.1.1-beta.

For a distributed index with agent mirrors in it (see more in ???), master tracks several different per-mirror counters. These counters are then used for failover and balancing. (Master picks the best mirror to use based on the counters.) Counters are accumulated in blocks of `ha_period_karma` seconds.

After beginning a new block, master may still use the accumulated values from the previous one, until the new one is half full. Thus, any previous history stops affecting the mirror choice after 1.5 times ha_period_karma seconds at most.

Despite that at most 2 blocks are used for mirror selection, upto 15 last blocks are actually stored, for instrumentation purposes. They can be inspected using [SHOW AGENT STATUS](../../show_agent_status.md) statement.

#### Example: {#example}

```

ha_period_karma = 120

```