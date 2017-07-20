SQL data sources (MySQL, PostgreSQL)
------------------------------------

With all the SQL drivers, indexing generally works as follows.

-  connection to the database is established;

-  pre-query (see `the section called
   “sql\_query\_pre” <../data_source_configuration_options/sqlquery_pre.md>`__)
   is executed to perform any necessary initial setup, such as setting
   per-connection encoding with MySQL;

-  main query (see `the section called
   “sql\_query” <../data_source_configuration_options/sqlquery.md>`__)
   is executed and the rows it returns are indexed;

-  post-query (see `the section called
   “sql\_query\_post” <../data_source_configuration_options/sqlquery_post.md>`__)
   is executed to perform any necessary cleanup;

-  connection to the database is closed;

-  indexer does the sorting phase (to be pedantic, index-type specific
   post-processing);

-  connection to the database is established again;

-  post-index query (see `the section called
   “sql\_query\_post\_index” <../data_source_configuration_options/sqlquery_post_index.md>`__)
   is executed to perform any necessary final cleanup;

-  connection to the database is closed again.

Most options, such as database user/host/password, are straightforward.
However, there are a few subtle things, which are discussed in more
detail here.

Ranged queries
~~~~~~~~~~~~~~

Main query, which needs to fetch all the documents, can impose a read
lock on the whole table and stall the concurrent queries (eg. INSERTs to
MyISAM table), waste a lot of memory for result set, etc. To avoid this,
Manticore supports so-called *ranged queries*. With ranged queries, Manticore
first fetches min and max document IDs from the table, and then
substitutes different ID intervals into main query text and runs the
modified query to fetch another chunk of documents. Here's an example.

Example 3.1. Ranged query usage example
                                       

::


    # in sphinx.conf

    sql_query_range = SELECT MIN(id),MAX(id) FROM documents
    sql_range_step = 1000
    sql_query = SELECT * FROM documents WHERE id>=$start AND id<=$end

If the table contains document IDs from 1 to, say, 2345, then sql\_query
would be run three times:

1. with ``$start`` replaced with 1 and ``$end`` replaced with 1000;

2. with ``$start`` replaced with 1001 and ``$end`` replaced with 2000;

3. with ``$start`` replaced with 2001 and ``$end`` replaced with 2345.

Obviously, that's not much of a difference for 2000-row table, but when
it comes to indexing 10-million-row MyISAM table, ranged queries might
be of some help.

``sql_query_post`` vs. ``sql_query_post_index``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The difference between post-query and post-index query is in that
post-query is run immediately when Manticore received all the documents,
but further indexing **may** still fail for some other reason. On the
contrary, by the time the post-index query gets executed, it is
**guaranteed** that the indexing was successful. Database connection is
dropped and re-established because sorting phase can be very lengthy and
would just timeout otherwise.
