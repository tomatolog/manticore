persistent\_connections\_limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The maximum # of simultaneous persistent connections to remote
`persistent
agents <../../index_configuration_options/agentpersistent.md>`__. Each
time connecting agent defined under ‘agent\_persistent’ we try to reuse
existing connection (if any), or connect and save the connection for the
future. However we can't hold unlimited # of such persistent
connections, since each one holds a worker on agent size (and finally
we'll receive the ‘maxed out’ error, when all of them are busy). This
very directive limits the number. It affects the num of connections to
each agent's host, across all distributed indexes.

It is reasonable to set the value equal or less than
`max\_children <../../searchd_program_configuration_options/maxchildren.md>`__
option of the agents.

Example:
^^^^^^^^

::


    persistent_connections_limit = 29 # assume that each host of agents has max_children = 30 (or 29).

