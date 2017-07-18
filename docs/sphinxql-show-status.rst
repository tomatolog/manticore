.. raw:: html

   <div class="navheader">

8.5. SHOW STATUS syntax
`Prev <sphinxql-show-warnings.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-insert.html>`__

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

.. rubric:: 8.5. SHOW STATUS syntax
   :name: show-status-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW STATUS [ LIKE pattern ]

**SHOW STATUS**, introduced in version 0.9.9-rc2, displays a number of
useful performance counters. IO and CPU counters will only be available
if searchd was started with –iostats and –cpustats switches
respectively.

.. code:: programlisting

    mysql> SHOW STATUS;
    +--------------------+-------+
    | Counter            | Value |
    +--------------------+-------+
    | uptime             | 216   |
    | connections        | 3     |
    | maxed_out          | 0     |
    | command_search     | 0     |
    | command_excerpt    | 0     |
    | command_update     | 0     |
    | command_keywords   | 0     |
    | command_persist    | 0     |
    | command_status     | 0     |
    | agent_connect      | 0     |
    | agent_retry        | 0     |
    | queries            | 10    |
    | dist_queries       | 0     |
    | query_wall         | 0.075 |
    | query_cpu          | OFF   |
    | dist_wall          | 0.000 |
    | dist_local         | 0.000 |
    | dist_wait          | 0.000 |
    | query_reads        | OFF   |
    | query_readkb       | OFF   |
    | query_readtime     | OFF   |
    | avg_query_wall     | 0.007 |
    | avg_query_cpu      | OFF   |
    | avg_dist_wall      | 0.000 |
    | avg_dist_local     | 0.000 |
    | avg_dist_wait      | 0.000 |
    | avg_query_reads    | OFF   |
    | avg_query_readkb   | OFF   |
    | avg_query_readtime | OFF   |
    +--------------------+-------+
    29 rows in set (0.00 sec)

Starting from version 2.1.1-beta, an optional LIKE clause is supported.
Refer to `Section 8.3, “SHOW META syntax” <sphinxql-show-meta.html>`__
for its syntax details.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+------------------------------------+
| `Prev <sphinxql-show-warnings.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-insert.html>`__   |
+-------------------------------------------+------------------------------------+------------------------------------+
| 8.4. SHOW WARNINGS syntax                 | `Home <index.html>`__              |  8.6. INSERT and REPLACE syntax    |
+-------------------------------------------+------------------------------------+------------------------------------+

.. raw:: html

   </div>
