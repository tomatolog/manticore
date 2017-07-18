### persistent_connections_limit {#persistent-connections-limit}

The maximum # of simultaneous persistent connections to remote [persistent agents](../../index_configuration_options/agentpersistent.md). Each time connecting agent defined under &#039;agent_persistent&#039; we try to reuse existing connection (if any), or connect and save the connection for the future. However we can&#039;t hold unlimited # of such persistent connections, since each one holds a worker on agent size (and finally we&#039;ll receive the &#039;maxed out&#039; error, when all of them are busy). This very directive limits the number. It affects the num of connections to each agent&#039;s host, across all distributed indexes.

It is reasonable to set the value equal or less than [max_children](../../searchd_program_configuration_options/maxchildren.md) option of the agents.

#### Example: {#example}

```

persistent_connections_limit = 29 # assume that each host of agents has max_children = 30 (or 29).

```