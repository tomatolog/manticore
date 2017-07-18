### agent_retry_count {#agent-retry-count}

Integer, specifies how many times sphinx will try to connect and query remote agents in distributed index before reporting fatal query error. Default is 0 (i.e. no retries). This value may be also specified on per-query basis using &#039;OPTION retry_count=XXX&#039; clause. If per-query option exists, it will override the one specified in config.

Note, that if you use [agent mirrors](../../index_configuration_options/agent.md) in definition of your distributed index, then before every attempt of connect sphinx will select different mirror, according to specified [ha_strategy](../../index_configuration_options/hastrategy.md)specified.

For example, if you have 10 mirrors, and surely know, that at least one of them alive, then you can definitely take the answer to a correct query, specifying options `ha_strategy = roundrobin` and `agent_retry_count = 9` in your config.