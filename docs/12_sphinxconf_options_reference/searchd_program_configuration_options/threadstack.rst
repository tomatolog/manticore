thread\_stack
~~~~~~~~~~~~~

Per-thread stack size. Optional, default is 1M.

In the ``workers = threads`` mode, every request is processed with a
separate thread that needs its own stack space. By default, 1M per
thread are allocated for stack. However, extremely complex search
requests might eventually exhaust the default stack and require more.
For instance, a query that matches a thousands of keywords (either
directly or through term expansion) can eventually run out of stack.
``searchd`` attempts to estimate the expected stack use, and blocks the
potentially dangerous queries. To process such queries, you can either
set the thread stack size by using the ``thread_stack`` directive (or
switch to a different ``workers`` setting if that is possible).

A query with N levels of nesting is estimated to require approximately
30+0.16\*N KB of stack, meaning that the default 64K is enough for
queries with upto 250 levels, 150K for upto 700 levels, etc. If the
stack size limit is not met, ``searchd`` fails the query and reports the
required stack size in the error message.

Example:
^^^^^^^^

::


    thread_stack = 256K

