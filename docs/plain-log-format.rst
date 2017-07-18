.. raw:: html

   <div class="navheader">

5.9.1. Plain log format
`Prev <query-log-format.html>`__ 
5.9. \ ``searchd`` query log formats
 `Next <sphinxql-log-format.html>`__

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

.. rubric:: 5.9.1. Plain log format
   :name: plain-log-format
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

By default, ``searchd`` logs all successfully executed search queries
into a query log file. Here’s an example:

.. code:: programlisting

    [Fri Jun 29 21:17:58 2007] 0.004 sec 0.004 sec [all/0/rel 35254 (0,20)] [lj] test
    [Fri Jun 29 21:20:34 2007] 0.024 sec 0.024 sec [all/0/rel 19886 (0,20) @channel_id] [lj] test

This log format is as follows:

.. code:: programlisting

    [query-date] real-time wall-time [match-mode/filters-count/sort-mode
        total-matches (offset,limit) @groupby-attr] [index-name] query

.. raw:: html

   <div class="itemizedlist">

-  real-time is a time measured just from start to finish of the query

-  wall-time like real-time but not including waiting for agents and
   merging result sets time

.. raw:: html

   </div>

Match mode can take one of the following values:

.. raw:: html

   <div class="itemizedlist">

-  “all” for SPH\_MATCH\_ALL mode;

-  “any” for SPH\_MATCH\_ANY mode;

-  “phr” for SPH\_MATCH\_PHRASE mode;

-  “bool” for SPH\_MATCH\_BOOLEAN mode;

-  “ext” for SPH\_MATCH\_EXTENDED mode;

-  “ext2” for SPH\_MATCH\_EXTENDED2 mode;

-  “scan” if the full scan mode was used, either by being specified with
   SPH\_MATCH\_FULLSCAN, or if the query was empty (as documented under
   `Matching Modes <matching-modes.html>`__)

.. raw:: html

   </div>

Sort mode can take one of the following values:

.. raw:: html

   <div class="itemizedlist">

-  “rel” for SPH\_SORT\_RELEVANCE mode;

-  “attr-” for SPH\_SORT\_ATTR\_DESC mode;

-  “attr+” for SPH\_SORT\_ATTR\_ASC mode;

-  “tsegs” for SPH\_SORT\_TIME\_SEGMENTS mode;

-  “ext” for SPH\_SORT\_EXTENDED mode.

.. raw:: html

   </div>

Additionally, if ``searchd`` was started with ``--iostats``, there will
be a block of data after where the index(es) searched are listed.

A query log entry might take the form of:

.. code:: programlisting

    [Fri Jun 29 21:17:58 2007] 0.004 sec [all/0/rel 35254 (0,20)] [lj]
       [ios=6 kb=111.1 ms=0.5] test

This additional block is information regarding I/O operations in
performing the search: the number of file I/O operations carried out,
the amount of data in kilobytes read from the index files and time spent
on I/O operations (although there is a background processing component,
the bulk of this time is the I/O operation time).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+----------------------------------+----------------------------------------+
| `Prev <query-log-format.html>`__        | `Up <query-log-format.html>`__   |  `Next <sphinxql-log-format.html>`__   |
+-----------------------------------------+----------------------------------+----------------------------------------+
| 5.9. \ ``searchd`` query log formats    | `Home <index.html>`__            |  5.9.2. SphinxQL log format            |
+-----------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
