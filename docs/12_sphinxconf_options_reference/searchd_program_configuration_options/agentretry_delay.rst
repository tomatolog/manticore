agent\_retry\_delay
~~~~~~~~~~~~~~~~~~~

Integer, in milliseconds. Specifies the delay sphinx rest before
retrying to query a remote agent in case it fails. The value has sense
only if non-zero
`agent\_retry\_count <../../searchd_program_configuration_options/agentretry_count.rst>`__
or non-zero per-query OPTION retry\_count specified. Default is 500.
This value may be also specified on per-query basis using ‘OPTION
retry\_delay=XXX’ clause. If per-query option exists, it will override
the one specified in config.
