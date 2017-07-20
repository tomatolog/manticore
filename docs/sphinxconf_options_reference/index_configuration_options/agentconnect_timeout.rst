agent\_connect\_timeout
~~~~~~~~~~~~~~~~~~~~~~~

Remote agent connection timeout, in milliseconds. Optional, default is
1000 (ie. 1 second).

When connecting to remote agents, ``searchd`` will wait at most this
much time for connect() call to complete successfully. If the timeout is
reached but connect() does not complete, and
`retries <../../general_api_functions/setretries.md>`__ are enabled,
retry will be initiated.

Example:
^^^^^^^^

::


    agent_connect_timeout = 300

