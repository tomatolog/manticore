RunQueries
~~~~~~~~~~

<b>Prototype:</b> function RunQueries ()

Connect to searchd, runs a batch of all queries added using
``AddQuery()``, obtains and returns the result sets. Returns false and
sets ``GetLastError()`` message on general error (such as network I/O
failure). Returns a plain array of result sets on success.

Each result set in the returned array is exactly the same as the result
set returned from ```Query()`` <../../querying/query.rst>`__.

Note that the batch query request itself almost always succeeds - unless
there's a network error, blocking index rotation in progress, or another
general failure which prevents the whole request from being processed.

However individual queries within the batch might very well fail. In
this case their respective result sets will contain non-empty
``&quot;error&quot;`` message, but no matches or query statistics. In
the extreme case all queries within the batch could fail. There still
will be no general error reported, because API was able to successfully
connect to ``searchd``, submit the batch, and receive the results - but
every result set will have a specific error message.
