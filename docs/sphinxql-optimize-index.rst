.. raw:: html

   <div class="navheader">

8.37. OPTIMIZE INDEX syntax
`Prev <sphinxql-show-index-settings.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-plan.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 8.37. OPTIMIZE INDEX syntax
   :name: optimize-index-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    OPTIMIZE INDEX index_name

Available since version 2.1.1-beta, OPTIMIZE statement enqueues a RT
index for optimization in a background thread.

Over time, RT indexes can grow fragmented into many disk chunks and/or
tainted with deleted, but unpurged data, impacting search performance.
When that happens, they can be optimized. Basically, the optimization
pass merges together disk chunks pairs, purging off documents suppressed
by K-list as it goes.

That is a lengthy and IO intensive process, so to limit the impact, all
the actual merge work is executed serially in a special background
thread, and the OPTIMIZE statement simply adds a job to its queue.
Currently, there is no way to check the index or queue status (that
might be added in the future to the SHOW INDEX STATUS and SHOW STATUS
statements respectively). The optimization thread can be IO-throttled,
you can control the maximum number of IOs per second and the maximum IO
size with `rt\_merge\_iops <conf-rt-merge-iops.html>`__ and
`rt\_merge\_maxiosize <conf-rt-merge-maxiosize.html>`__ directives
respectively. The optimization jobs queue is lost on daemon crash.

The RT index being optimized stays online and available for both
searching and updates at (almost) all times during the optimization. It
gets locked (very) briefly every time that a pair of disk chunks is
merged successfully, to rename the old and the new files, and update the
index header.

At the moment, OPTIMIZE needs to be issued manually, the indexes will
*not* be optimized automatically. That might change in the future
releases.

.. code:: programlisting

    mysql> OPTIMIZE INDEX rt;
    Query OK, 0 rows affected (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------------+------------------------------------+---------------------------------------+
| `Prev <sphinxql-show-index-settings.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-plan.html>`__   |
+-------------------------------------------------+------------------------------------+---------------------------------------+
| 8.36. SHOW INDEX SETTINGS syntax                | `Home <index.html>`__              |  8.38. SHOW PLAN syntax               |
+-------------------------------------------------+------------------------------------+---------------------------------------+

.. raw:: html

   </div>
