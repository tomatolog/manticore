ManticoreQL log format
~~~~~~~~~~~~~~~~~~~

This new log format introduced with the goals begin logging everything
and then some, and in a format easy to automate (for instance,
automatically replay). ManticoreQL log format can either be enabled via the
`query\_log\_format <../../searchd_program_configuration_options/querylog_format.md>`__
directive in the configuration file, or switched back and forth on the
fly with the
```SET GLOBAL query_log_format=...`` <../../set_syntax.md>`__ statement
via ManticoreQL. In the new format, the example from the previous section
would look as follows. (Wrapped below for readability, but with just one
query per line in the actual log.)

::


    /* Fri Jun 29 21:17:58.609 2007 2011 conn 2 real 0.004 wall 0.004 found 35254 */
    SELECT * FROM lj WHERE MATCH('test') OPTION ranker=proximity;

    /* Fri Jun 29 21:20:34 2007.555 conn 3 real 0.024 wall 0.024 found 19886 */
    SELECT * FROM lj WHERE MATCH('test') GROUP BY channel_id
    OPTION ranker=proximity;

Note that <b>all</b> requests would be logged in this format, including
those sent via ManticoreAPI and ManticoreSE, not just those sent via ManticoreQL.
Also note, that this kind of logging works only with plain log files and
will not work if you use ‘syslog’ service for logging.

The features of ManticoreQL log format compared to the default text one are
as follows.

-  All request types should be logged. (This is still work in progress.)

-  Full statement data will be logged where possible.

-  Errors and warnings are logged.

-  The log should be automatically replayable via ManticoreQL.

-  Additional performance counters (currently, per-agent distributed
   query times) are logged.

Use sphinxql:compact\_in to shorten your IN() clauses in log if you have
too much values in it.

Every request (including both ManticoreAPI and ManticoreQL) request must
result in exactly one log line. All request types, including INSERT,
CALL SNIPPETS, etc will eventually get logged, though as of time of this
writing, that is a work in progress). Every log line must be a valid
ManticoreQL statement that reconstructs the full request, except if the
logged request is too big and needs shortening for performance reasons.
Additional messages, counters, etc can be logged in the comments section
after the request.
