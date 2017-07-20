SHOW INDEX STATUS syntax
------------------------

::


    SHOW INDEX index_name STATUS

Displays various per-index statistics. Currently, those include:

-  <b>indexed\_documents</b> and <b>indexed\_bytes</b>, number of the
   documents indexed and their text size in bytes, respectively.
-  <b>field\_tokens\_XXX</b>, sums of per-field lengths (in tokens) over
   the entire index (that is used internally in BM25A and BM25F
   functions for ranking purposes). Only available for indexes built
   with index\_field\_lengths=1.
-  <b>ram\_bytes</b>, total size (in bytes) of the RAM-resident index
   portion.
-  queries time statistics of last 1 minute, 5 minutes, 15 minutes and
   total since daemon start;data is encapsulated as a JSON object which
   includes number of queries, min,max,avg,95 and 99 percentile values.
-  queries found rows statistics of last 1 minute, 5 minutes, 15 minutes
   and total since daemon start;data is encapsulated as a JSON object
   which includes number of queries, min,max,avg,95 and 99 percentile
   values.

::


    mysql> SHOW INDEX lj STATUS;
    +--------------------+-------------+
    | Variable_name      | Value       |
    +--------------------+-------------+
    | index_type         | disk        |
    | indexed_documents  | 2495219     |
    | indexed_bytes      | 10380483879 |
    | field_tokens_title | 6999145     |
    | field_tokens_body  | 1501825050  |
    | total_tokens       | 1508824195  |
    | ram_bytes          | 305963599   |
    | disk_bytes         | 5455804365  |
    | mem_limit          | 536870912   |
    +--------------------+-------------+
    8 rows in set (0.00 sec)

