## Using SphinxSE {#using-sphinxse}

To search via SphinxSE, you would need to create special ENGINE=SPHINX &quot;search table&quot;, and then SELECT from it with full text query put into WHERE clause for query column.

Let&#039;s begin with an example create statement and search query:

```

CREATE TABLE t1
(
    id          INTEGER UNSIGNED NOT NULL,
    weight      INTEGER NOT NULL,
    query       VARCHAR(3072) NOT NULL,
    group_id    INTEGER,
    INDEX(query)
) ENGINE=SPHINX CONNECTION="sphinx://localhost:9312/test";

SELECT * FROM t1 WHERE query='test it;mode=any';

```

First 3 columns of search table _must_ have a types of `INTEGER UNSINGED` or `BIGINT` for the 1st column (document id), `INTEGER` or `BIGINT` for the 2nd column (match weight), and `VARCHAR` or `TEXT` for the 3rd column (your query), respectively. This mapping is fixed; you can not omit any of these three required columns, or move them around, or change types. Also, query column must be indexed; all the others must be kept unindexed. Columns&#039; names are ignored so you can use arbitrary ones.

Additional columns must be either `INTEGER`, `TIMESTAMP`, `BIGINT`, `VARCHAR`, or `FLOAT`. They will be bound to attributes provided in Sphinx result set by name, so their names must match attribute names specified in `sphinx.conf`. If there&#039;s no such attribute name in Sphinx search results, column will have `NULL` values.

Special &quot;virtual&quot; attributes names can also be bound to SphinxSE columns. `_sph_` needs to be used instead of `@` for that. For instance, to obtain the values of `@groupby`, `@count`, or `@distinct` virtual attributes, use `_sph_groupby`, `_sph_count` or `_sph_distinct` column names, respectively.

`CONNECTION` string parameter can be used to specify default searchd host, port and indexes for queries issued using this table. If no connection string is specified in `CREATE TABLE`, index name &quot;*&quot; (ie. search all indexes) and localhost:9312 are assumed. Connection string syntax is as follows:

```

CONNECTION="sphinx://HOST:PORT/INDEXNAME"

```

You can change the default connection string later:

```

ALTER TABLE t1 CONNECTION="sphinx://NEWHOST:NEWPORT/NEWINDEXNAME";

```

You can also override all these parameters per-query.

As seen in example, both query text and search options should be put into WHERE clause on search query column (ie. 3rd column); the options are separated by semicolons; and their names from values by equality sign. Any number of options can be specified. Available options are:

*   query - query text;

*   mode - matching mode. Must be one of &quot;all&quot;, &quot;any&quot;, &quot;phrase&quot;, &quot;boolean&quot;, or &quot;extended&quot;. Default is &quot;all&quot;;

*   sort - match sorting mode. Must be one of &quot;relevance&quot;, &quot;attr_desc&quot;, &quot;attr_asc&quot;, &quot;time_segments&quot;, or &quot;extended&quot;. In all modes besides &quot;relevance&quot; attribute name (or sorting clause for &quot;extended&quot;) is also required after a colon:

    ```

    ... WHERE query='test;sort=attr_asc:group_id';
    ... WHERE query='test;sort=extended:@weight desc, group_id asc';

    ```

*   offset - offset into result set, default is 0;

*   limit - amount of matches to retrieve from result set, default is 20;

*   index - names of the indexes to search:

    ```

    ... WHERE query='test;index=test1;';
    ... WHERE query='test;index=test1,test2,test3;';

    ```

*   minid, maxid - min and max document ID to match;

*   weights - comma-separated list of weights to be assigned to Sphinx full-text fields:

    ```

    ... WHERE query='test;weights=1,2,3;';

    ```

*   filter, !filter - comma-separated attribute name and a set of values to match:

    ```

    # only include groups 1, 5 and 19
    ... WHERE query='test;filter=group_id,1,5,19;';

    # exclude groups 3 and 11
    ... WHERE query='test;!filter=group_id,3,11;';

    ```

*   range, !range - comma-separated (integer or bigint) Sphinx attribute name, and min and max values to match:

    ```

    # include groups from 3 to 7, inclusive
    ... WHERE query='test;range=group_id,3,7;';

    # exclude groups from 5 to 25
    ... WHERE query='test;!range=group_id,5,25;';

    ```

*   floatrange, !floatrange - comma-separated (floating point) Sphinx attribute name, and min and max values to match:

    ```

    # filter by a float size
    ... WHERE query='test;floatrange=size,2,3;';

    # pick all results within 1000 meter from geoanchor
    ... WHERE query='test;floatrange=@geodist,0,1000;';

    ```

*   maxmatches - per-query max matches value, as in max_matches parameter to [SetLimits()](../general_query_settings/setlimits.md) API call:

    ```

    ... WHERE query='test;maxmatches=2000;';

    ```

*   cutoff - maximum allowed matches, as in cutoff parameter to [SetLimits()](../general_query_settings/setlimits.md) API call:

    ```

    ... WHERE query='test;cutoff=10000;';

    ```

*   maxquerytime - maximum allowed query time (in milliseconds), as in [SetMaxQueryTime()](../general_query_settings/setmaxquerytime.md) API call:

    ```

    ... WHERE query='test;maxquerytime=1000;';

    ```

*   groupby - group-by function and attribute, corresponding to [SetGroupBy()](../group_by_settings/setgroupby.md) API call:

    ```

    ... WHERE query='test;groupby=day:published_ts;';
    ... WHERE query='test;groupby=attr:group_id;';

    ```

*   groupsort - group-by sorting clause:

    ```

    ... WHERE query='test;groupsort=@count desc;';

    ```

*   distinct - an attribute to compute COUNT(DISTINCT) for when doing group-by, as in [SetGroupDistinct()](../group_by_settings/setgroupdistinct.md) API call:

    ```

    ... WHERE query='test;groupby=attr:country_id;distinct=site_id';

    ```

*   indexweights - comma-separated list of index names and weights to use when searching through several indexes:

    ```

    ... WHERE query='test;indexweights=idx_exact,2,idx_stemmed,1;';

    ```

*   fieldweights - comma-separated list of per-field weights that can be used by the ranker:

    ```

    ... WHERE query='test;fieldweights=title,10,abstract,3,content,1;';

    ```

*   comment - a string to mark this query in query log (mapping to $comment parameter in [Query()](../querying/query.md) API call):

    ```

    ... WHERE query='test;comment=marker001;';

    ```

*   select - a string with expressions to compute (mapping to [SetSelect()](../general_query_settings/setselect.md) API call):

    ```

    ... WHERE query='test;select=2*a+3*b as myexpr;';

    ```

*   host, port - remote `searchd` host name and TCP port, respectively:

    ```

    ... WHERE query='test;host=sphinx-test.loc;port=7312;';

    ```

*   ranker - a ranking function to use with &quot;extended&quot; matching mode, as in [SetRankingMode()](../full-text_search_query_settings/setrankingmode.md) API call (the only mode that supports full query syntax). Known values are &quot;proximity_bm25&quot;, &quot;bm25&quot;, &quot;none&quot;, &quot;wordcount&quot;, &quot;proximity&quot;, &quot;matchany&quot;, &quot;fieldmask&quot;, &quot;sph04&quot; (starting with 1.10-beta), &quot;expr:EXPRESSION&quot; (starting with 2.0.4-release) syntax to support expression-based ranker (where EXPRESSION should be replaced with your specific ranking formula), and &quot;export:EXPRESSION&quot; (starting with 2.1.1-beta):

    ```

    ... WHERE query='test;mode=extended;ranker=bm25;';
    ... WHERE query='test;mode=extended;ranker=expr:sum(lcs);';

    ```

    The &quot;export&quot; ranker works exactly like ranker=expr, but it stores the per-document factor values, while ranker=expr discards them after computing the final WEIGHT() value. Note that ranker=export is meant to be used but rarely, only to train a ML (machine learning) function or to define your own ranking function by hand, and never in actual production. When using this ranker, you&#039;ll probably want to examine the output of the RANKFACTORS() function (added in version 2.1.1-beta) that produces a string with all the field level factors for each document.

    ```

        SELECT *, WEIGHT(), RANKFACTORS()
            FROM myindex
            WHERE MATCH('dog')
            OPTION ranker=export('100*bm25')

    ```

    would produce something like

    ```

    *************************** 1\. row ***************************
               id: 555617
        published: 1110067331
       channel_id: 1059819
            title: 7
          content: 428
         weight(): 69900
    rankfactors(): bm25=699, bm25a=0.666478, field_mask=2,
    doc_word_count=1, field1=(lcs=1, hit_count=4, word_count=1,
    tf_idf=1.038127, min_idf=0.259532, max_idf=0.259532, sum_idf=0.259532,
    min_hit_pos=120, min_best_span_pos=120, exact_hit=0,
    max_window_hits=1), word1=(tf=4, idf=0.259532)
    *************************** 2\. row ***************************
               id: 555313
        published: 1108438365
       channel_id: 1058561
            title: 8
          content: 249
         weight(): 68500
    rankfactors(): bm25=685, bm25a=0.675213, field_mask=3,
    doc_word_count=1, field0=(lcs=1, hit_count=1, word_count=1,
    tf_idf=0.259532, min_idf=0.259532, max_idf=0.259532, sum_idf=0.259532,
    min_hit_pos=8, min_best_span_pos=8, exact_hit=0, max_window_hits=1),
    field1=(lcs=1, hit_count=2, word_count=1, tf_idf=0.519063,
    min_idf=0.259532, max_idf=0.259532, sum_idf=0.259532, min_hit_pos=36,
    min_best_span_pos=36, exact_hit=0, max_window_hits=1), word1=(tf=3,
    idf=0.259532)

    ```

*   geoanchor - geodistance anchor, as in [SetGeoAnchor()](../result_set_filtering_settings/setgeoanchor.md) API call. Takes 4 parameters which are latitude and longitude attribute names, and anchor point coordinates respectively:

    ```

    ... WHERE query='test;geoanchor=latattr,lonattr,0.123,0.456';

    ```

One **very important** note that it is **much** more efficient to allow Sphinx to perform sorting, filtering and slicing the result set than to raise max matches count and use WHERE, ORDER BY and LIMIT clauses on MySQL side. This is for two reasons. First, Sphinx does a number of optimizations and performs better than MySQL on these tasks. Second, less data would need to be packed by searchd, transferred and unpacked by SphinxSE.

Starting with version 0.9.9-rc1, additional query info besides result set could be retrieved with `SHOW ENGINE SPHINX STATUS` statement:

```

mysql> SHOW ENGINE SPHINX STATUS;
+--------+-------+-------------------------------------------------+
| Type   | Name  | Status                                          |
+--------+-------+-------------------------------------------------+
| SPHINX | stats | total: 25, total found: 25, time: 126, words: 2 |
| SPHINX | words | sphinx:591:1256 soft:11076:15945                |
+--------+-------+-------------------------------------------------+
2 rows in set (0.00 sec)

```

This information can also be accessed through status variables. Note that this method does not require super-user privileges.

```

mysql> SHOW STATUS LIKE 'sphinx_%';
+--------------------+----------------------------------+
| Variable_name      | Value                            |
+--------------------+----------------------------------+
| sphinx_total       | 25                               |
| sphinx_total_found | 25                               |
| sphinx_time        | 126                              |
| sphinx_word_count  | 2                                |
| sphinx_words       | sphinx:591:1256 soft:11076:15945 |
+--------------------+----------------------------------+
5 rows in set (0.00 sec)

```

You could perform JOINs on SphinxSE search table and tables using other engines. Here&#039;s an example with &quot;documents&quot; from example.sql:

```

mysql> SELECT content, date_added FROM test.documents docs
-> JOIN t1 ON (docs.id=t1.id)
-> WHERE query="one document;mode=any";
+-------------------------------------+---------------------+
| content                             | docdate             |
+-------------------------------------+---------------------+
| this is my test document number two | 2006-06-17 14:04:28 |
| this is my test document number one | 2006-06-17 14:04:28 |
+-------------------------------------+---------------------+
2 rows in set (0.00 sec)

mysql> SHOW ENGINE SPHINX STATUS;
+--------+-------+---------------------------------------------+
| Type   | Name  | Status                                      |
+--------+-------+---------------------------------------------+
| SPHINX | stats | total: 2, total found: 2, time: 0, words: 2 |
| SPHINX | words | one:1:2 document:2:2                        |
+--------+-------+---------------------------------------------+
2 rows in set (0.00 sec)

```