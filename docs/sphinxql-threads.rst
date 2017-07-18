.. raw:: html

   <div class="navheader">

8.44. SHOW THREADS syntax
`Prev <sphinxql-reload-plugins.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-reload-index.html>`__

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

.. rubric:: 8.44. SHOW THREADS syntax
   :name: show-threads-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW THREADS [ OPTION columns=width ]

SHOW THREADS statement, introduced in version 2.2.2-beta, lists all
currently active client threads, not counting system threads. It returns
a table with columns that describe:

.. raw:: html

   <div class="itemizedlist">

-  **thread id**
-  **connection protocol**, possible values are sphinxapi and sphinxql
-  **thread state**, possible values are handshake, net\_read,
   net\_write, query, net\_idle
-  **time** since the current state was changed (in seconds, with
   microsecond precision)
-  **information** about queries

.. raw:: html

   </div>

The ‘Info’ column will be cut at the width you’ve specified in the
‘columns=width’ option (notice the third row in the example table
below). This column will contain raw SphinxQL queries and, if there are
API queries, full text syntax and comments will be displayed. With an
API-snippet, the data size will be displayed along with the query.

.. code:: programlisting

    mysql> SHOW THREADS OPTION columns=50;
    +------+----------+-------+----------+----------------------------------------------------+
    | Tid  | Proto    | State | Time     | Info                                               |
    +------+----------+-------+----------+----------------------------------------------------+
    | 5168 | sphinxql | query | 0.000002 | show threads option columns=50                     |
    | 5175 | sphinxql | query | 0.000002 | select * from rt where match ( 'the box' )         |
    | 1168 | sphinxql | query | 0.000002 | select * from rt where match ( 'the box and faximi |
    +------+----------+-------+----------+----------------------------------------------------+
    3 row in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+------------------------------------+------------------------------------------+
| `Prev <sphinxql-reload-plugins.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-reload-index.html>`__   |
+--------------------------------------------+------------------------------------+------------------------------------------+
| 8.43. RELOAD PLUGINS syntax                | `Home <index.html>`__              |  8.45. RELOAD INDEX syntax               |
+--------------------------------------------+------------------------------------+------------------------------------------+

.. raw:: html

   </div>
