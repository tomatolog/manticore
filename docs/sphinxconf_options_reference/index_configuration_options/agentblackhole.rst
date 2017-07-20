agent\_blackhole
~~~~~~~~~~~~~~~~

Remote blackhole agent declaration in the `distributed
index <../../distributed_searching.md>`__. Multi-value, optional,
default is empty.

``agent_blackhole`` lets you fire-and-forget queries to remote agents.
That is useful for debugging (or just testing) production clusters: you
can setup a separate debugging/testing searchd instance, and forward the
requests to this instance from your production master (aggregator)
instance without interfering with production work. Master searchd will
attempt to connect and query blackhole agent normally, but it will
neither wait nor process any responses. Also, all network errors on
blackhole agents will be ignored. The value format is completely
identical to regular
`agent <../../index_configuration_options/agent.md>`__ directive.

Example:
^^^^^^^^

::


    agent_blackhole = testbox:9312:testindex1,testindex2

