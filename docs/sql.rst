.. raw:: html

   <div class="navheader">

3.8. SQL data sources (MySQL, PostgreSQL)
`Prev <charsets.html>`__ 
Chapter 3. Indexing
 `Next <xmlpipe2.html>`__

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

.. rubric:: 3.8. SQL data sources (MySQL, PostgreSQL)
   :name: sql-data-sources-mysql-postgresql
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

With all the SQL drivers, indexing generally works as follows.

.. raw:: html

   <div class="itemizedlist">

-  connection to the database is established;

-  pre-query (see `Section 12.1.11,
   “sql\_query\_pre” <conf-sql-query-pre.html>`__) is executed to
   perform any necessary initial setup, such as setting per-connection
   encoding with MySQL;

-  main query (see `Section 12.1.12,
   “sql\_query” <conf-sql-query.html>`__) is executed and the rows it
   returns are indexed;

-  post-query (see `Section 12.1.28,
   “sql\_query\_post” <conf-sql-query-post.html>`__) is executed to
   perform any necessary cleanup;

-  connection to the database is closed;

-  indexer does the sorting phase (to be pedantic, index-type specific
   post-processing);

-  connection to the database is established again;

-  post-index query (see `Section 12.1.29,
   “sql\_query\_post\_index” <conf-sql-query-post-index.html>`__) is
   executed to perform any necessary final cleanup;

-  connection to the database is closed again.

.. raw:: html

   </div>

Most options, such as database user/host/password, are straightforward.
However, there are a few subtle things, which are discussed in more
detail here.

.. rubric:: Ranged queries
   :name: ranged-queries

Main query, which needs to fetch all the documents, can impose a read
lock on the whole table and stall the concurrent queries (eg. INSERTs to
MyISAM table), waste a lot of memory for result set, etc. To avoid this,
Sphinx supports so-called *ranged queries*. With ranged queries, Sphinx
first fetches min and max document IDs from the table, and then
substitutes different ID intervals into main query text and runs the
modified query to fetch another chunk of documents. Here’s an example.

.. raw:: html

   <div class="example">

**Example 3.1. Ranged query usage example**

.. raw:: html

   <div class="example-contents">

.. code:: programlisting

    # in sphinx.conf

    sql_query_range = SELECT MIN(id),MAX(id) FROM documents
    sql_range_step = 1000
    sql_query = SELECT * FROM documents WHERE id>=$start AND id<=$end

.. raw:: html

   </div>

.. raw:: html

   </div>

If the table contains document IDs from 1 to, say, 2345, then sql\_query
would be run three times:

.. raw:: html

   <div class="orderedlist">

1. with ``$start`` replaced with 1 and ``$end`` replaced with 1000;

2. with ``$start`` replaced with 1001 and ``$end`` replaced with 2000;

3. with ``$start`` replaced with 2001 and ``$end`` replaced with 2345.

.. raw:: html

   </div>

Obviously, that’s not much of a difference for 2000-row table, but when
it comes to indexing 10-million-row MyISAM table, ranged queries might
be of some help.

.. rubric:: \ ``sql_query_post`` vs. ``sql_query_post_index``
   :name: sql_query_post-vs.-sql_query_post_index

The difference between post-query and post-index query is in that
post-query is run immediately when Sphinx received all the documents,
but further indexing **may** still fail for some other reason. On the
contrary, by the time the post-index query gets executed, it is
**guaranteed** that the indexing was successful. Database connection is
dropped and re-established because sorting phase can be very lengthy and
would just timeout otherwise.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------------------------------------+--------------------------+------------------------------+
| `Prev <charsets.html>`__                                                  | `Up <indexing.html>`__   |  `Next <xmlpipe2.html>`__    |
+---------------------------------------------------------------------------+--------------------------+------------------------------+
| 3.7. Charsets, case folding, translation tables, and replacement rules    | `Home <index.html>`__    |  3.9. xmlpipe2 data source   |
+---------------------------------------------------------------------------+--------------------------+------------------------------+

.. raw:: html

   </div>
