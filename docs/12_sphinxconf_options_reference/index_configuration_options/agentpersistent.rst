agent\_persistent
~~~~~~~~~~~~~~~~~

Persistently connected remote agent declaration. Multi-value, optional,
default is empty. Introduced in version 2.1.1-beta.

``agent_persistent`` directive syntax matches that of the
`agent <../../index_configuration_options/agent.md>`__ directive. The
only difference is that the master will <b>not</b> open a new connection
to the agent for every query and then close it. Rather, it will keep a
connection open and attempt to reuse for the subsequent queries. The
maximal number of such persistent connections per one agent host is
limited by
`persistent\_connections\_limit <../../searchd_program_configuration_options/persistentconnections_limit.md>`__
option of searchd section.

Note, that you <b>have</b> to set the last one in something greater than
0 if you want to use persistent agent connections. Otherwise - when
`persistent\_connections\_limit <../../searchd_program_configuration_options/persistentconnections_limit.md>`__
is not defined, it assumes the zero num of persistent connections, and
‘agent\_persistent’ acts exactly as simple ‘agent’.

Persistent master-agent connections reduce TCP port pressure, and save
on connection handshakes. As of time of this writing, they are supported
<b>only</b> in workers=threads mode. In other modes, simple
non-persistent connections (i.e., one connection per operation) will be
used, and a warning will show up in the console.

Example:
^^^^^^^^

::


    agent_persistent = remotebox:9312:index2

