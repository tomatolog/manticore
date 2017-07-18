### agent_persistent {#agent-persistent}

Persistently connected remote agent declaration. Multi-value, optional, default is empty. Introduced in version 2.1.1-beta.

`agent_persistent` directive syntax matches that of the [agent](../../index_configuration_options/agent.md) directive. The only difference is that the master will &lt;b&gt;not&lt;/b&gt; open a new connection to the agent for every query and then close it. Rather, it will keep a connection open and attempt to reuse for the subsequent queries. The maximal number of such persistent connections per one agent host is limited by [persistent_connections_limit](../../searchd_program_configuration_options/persistentconnections_limit.md) option of searchd section.

Note, that you &lt;b&gt;have&lt;/b&gt; to set the last one in something greater than 0 if you want to use persistent agent connections. Otherwise - when [persistent_connections_limit](../../searchd_program_configuration_options/persistentconnections_limit.md) is not defined, it assumes the zero num of persistent connections, and &#039;agent_persistent&#039; acts exactly as simple &#039;agent&#039;.

Persistent master-agent connections reduce TCP port pressure, and save on connection handshakes. As of time of this writing, they are supported &lt;b&gt;only&lt;/b&gt; in workers=threads mode. In other modes, simple non-persistent connections (i.e., one connection per operation) will be used, and a warning will show up in the console.

#### Example: {#example}

```

agent_persistent = remotebox:9312:index2

```