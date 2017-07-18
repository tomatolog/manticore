predicted\_time\_costs
~~~~~~~~~~~~~~~~~~~~~~

Costs for the query time prediction model, in nanoseconds. Optional,
default is “doc=64, hit=48, skip=2048, match=64” (without the quotes).
Added in 2.1.1-beta.

Terminating queries before completion based on their execution time (via
either
`SetMaxQueryTime() <../../general_query_settings/setmaxquerytime.html>`__
API call, or `SELECT … OPTION
max\_query\_time <../../select_syntax.html>`__ SphinxQL statement) is a
nice safety net, but it comes with an inborn drawback: indeterministic
(unstable) results. That is, if you repeat the very same (complex)
search query with a time limit several times, the time limit will get
hit at different stages, and you will get *different* result sets.

Starting with 2.1.1-beta, there is a new option, `SELECT … OPTION
max\_predicted\_time <../../select_syntax.html>`__, that lets you limit
the query time *and* get stable, repeatable results. Instead of
regularly checking the actual current time while evaluating the query,
which is indeterministic, it predicts the current running time using a
simple linear model instead:

::


    predicted_time =
        doc_cost * processed_documents +
        hit_cost * processed_hits +
        skip_cost * skiplist_jumps +
        match_cost * found_matches

The query is then terminated early when the ``predicted_time`` reaches a
given limit.

Of course, this is not a hard limit on the actual time spent (it is,
however, a hard limit on the amount of *processing* work done), and a
simple linear model is in no way an ideally precise one. So the wall
clock time *may* be either below or over the target limit. However, the
error margins are quite acceptable: for instance, in our experiments
with a 100 msec target limit the majority of the test queries fell into
a 95 to 105 msec range, and *all* of the queries were in a 80 to 120
msec range. Also, as a nice side effect, using the modeled query time
instead of measuring actual run time results in somewhat less
gettimeofday() calls, too.

No two server makes and models are identical, so
``predicted_time_costs`` directive lets you configure the costs for the
model above. For convenience, they are integers, counted in nanoseconds.
(The limit in max\_predicted\_time is counted in milliseconds, and
having to specify cost values as 0.000128 ms instead of 128 ns is
somewhat more error prone.) It is not necessary to specify all 4 costs
at once, as the missed one will take the default values. However, we
strongly suggest to specify all of them, for readability.

Example:
^^^^^^^^

::


    predicted_time_costs = doc=128, hit=96, skip=4096, match=128

