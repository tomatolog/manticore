agent\_query\_timeout
~~~~~~~~~~~~~~~~~~~~~

Remote agent query timeout, in milliseconds. Optional, default is 3000
(ie. 3 seconds). Added in version 2.1.1-beta.

After connection, ``searchd`` will wait at most this much time for
remote queries to complete. This timeout is fully separate from
connection timeout; so the maximum possible delay caused by a remote
agent equals to the sum of ``agent_connection_timeout`` and
``agent_query_timeout``. Queries will <b>not</b> be retried if this
timeout is reached; a warning will be produced instead.

Example:
^^^^^^^^

::


    agent_query_timeout = 10000 # our query can be long, allow up to 10 sec

