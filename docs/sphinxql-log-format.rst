.. raw:: html

   <div class="navheader">

5.9.2. SphinxQL log format
`Prev <plain-log-format.html>`__ 
5.9. \ ``searchd`` query log formats
 `Next <sphinxql.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 5.9.2. SphinxQL log format
   :name: sphinxql-log-format
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

This is a new log format introduced in 2.0.1-beta, with the goals begin
logging everything and then some, and in a format easy to automate (for
instance, automatically replay). New format can either be enabled via
the `query\_log\_format <conf-query-log-format.html>`__ directive in the
configuration file, or switched back and forth on the fly with the
```SET GLOBAL query_log_format=...`` <sphinxql-set.html>`__ statement
via SphinxQL. In the new format, the example from the previous section
would look as follows. (Wrapped below for readability, but with just one
query per line in the actual log.)

.. code:: programlisting

    /* Fri Jun 29 21:17:58.609 2007 2011 conn 2 real 0.004 wall 0.004 found 35254 */
    SELECT * FROM lj WHERE MATCH('test') OPTION ranker=proximity;

    /* Fri Jun 29 21:20:34 2007.555 conn 3 real 0.024 wall 0.024 found 19886 */
    SELECT * FROM lj WHERE MATCH('test') GROUP BY channel_id
    OPTION ranker=proximity;

Note that **all** requests would be logged in this format, including
those sent via SphinxAPI and SphinxSE, not just those sent via SphinxQL.
Also note, that this kind of logging works only with plain log files and
will not work if you use ‘syslog’ for logging.

The features of SphinxQL log format compared to the default text one are
as follows.

.. raw:: html

   <div class="itemizedlist">

-  All request types should be logged. (This is still work in progress.)

-  Full statement data will be logged where possible.

-  Errors and warnings are logged.

-  The log should be automatically replayable via SphinxQL.

-  Additional performance counters (currently, per-agent distributed
   query times) are logged.

.. raw:: html

   </div>

Use sphinxql:compact\_in to shorten your IN() clauses in log if you have
too much values in it.

Every request (including both SphinxAPI and SphinxQL) request must
result in exactly one log line. All request types, including INSERT,
CALL SNIPPETS, etc will eventually get logged, though as of time of this
writing, that is a work in progress). Every log line must be a valid
SphinxQL statement that reconstructs the full request, except if the
logged request is too big and needs shortening for performance reasons.
Additional messages, counters, etc can be logged in the comments section
after the request.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+----------------------------------+----------------------------------------------+
| `Prev <plain-log-format.html>`__    | `Up <query-log-format.html>`__   |  `Next <sphinxql.html>`__                    |
+-------------------------------------+----------------------------------+----------------------------------------------+
| 5.9.1. Plain log format             | `Home <index.html>`__            |  5.10. MySQL protocol support and SphinxQL   |
+-------------------------------------+----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
