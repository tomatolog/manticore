.. raw:: html

   <div class="navheader">

12.4.36. thread\_stack
`Prev <conf-rt-flush-period.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-expansion-limit.html>`__

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

.. rubric:: 12.4.36. thread\_stack
   :name: thread_stack
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Per-thread stack size. Optional, default is 1M. Introduced in version
2.0.1-beta.

In the ``workers = threads`` mode, every request is processed with a
separate thread that needs its own stack space. By default, 1M per
thread are allocated for stack. However, extremely complex search
requests might eventually exhaust the default stack and require more.
For instance, a query that matches a thousands of keywords (either
directly or through term expansion) can eventually run out of stack.
Previously, that resulted in crashes. Starting with 2.0.1-beta,
``searchd`` attempts to estimate the expected stack use, and blocks the
potentially dangerous queries. To process such queries, you can either
the thread stack size by using the ``thread_stack`` directive (or switch
to a different ``workers`` setting if that is possible).

A query with N levels of nesting is estimated to require approximately
30+0.16\*N KB of stack, meaning that the default 64K is enough for
queries with upto 250 levels, 150K for upto 700 levels, etc. If the
stack size limit is not met, ``searchd`` fails the query and reports the
required stack size in the error message.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    thread_stack = 256K

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+-----------------------------------+-----------------------------------------+
| `Prev <conf-rt-flush-period.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-expansion-limit.html>`__   |
+-----------------------------------------+-----------------------------------+-----------------------------------------+
| 12.4.35. rt\_flush\_period              | `Home <index.html>`__             |  12.4.37. expansion\_limit              |
+-----------------------------------------+-----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
