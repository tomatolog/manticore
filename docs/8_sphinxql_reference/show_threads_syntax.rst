SHOW THREADS syntax
-------------------

::


    SHOW THREADS [ OPTION columns=width ]

SHOW THREADS statement, introduced in version 2.2.2-beta, lists all
currently active client threads, not counting system threads. It returns
a table with columns that describe:

-  <b>thread id</b>
-  <b>connection protocol</b>, possible values are sphinxapi and
   sphinxql
-  <b>thread state</b>, possible values are handshake, net\_read,
   net\_write, query, net\_idle
-  <b>time</b> since the current state was changed (in seconds, with
   microsecond precision)
-  <b>information</b> about queries

The ‘Info’ column will be cut at the width you've specified in the
‘columns=width’ option (notice the third row in the example table
below). This column will contain raw SphinxQL queries and, if there are
API queries, full text syntax and comments will be displayed. With an
API-snippet, the data size will be displayed along with the query.

::


    mysql> SHOW THREADS OPTION columns=50;
    +------+----------+-------+----------+----------------------------------------------------+
    | Tid  | Proto    | State | Time     | Info                                               |
    +------+----------+-------+----------+----------------------------------------------------+
    | 5168 | sphinxql | query | 0.000002 | show threads option columns=50                     |
    | 5175 | sphinxql | query | 0.000002 | select * from rt where match ( 'the box' )         |
    | 1168 | sphinxql | query | 0.000002 | select * from rt where match ( 'the box and faximi |
    +------+----------+-------+----------+----------------------------------------------------+
    3 row in set (0.00 sec)

