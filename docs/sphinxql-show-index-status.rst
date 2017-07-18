.. raw:: html

   <div class="navheader">

8.35. SHOW INDEX STATUS syntax
`Prev <sphinxql-show-profile.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-index-settings.html>`__

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

.. rubric:: 8.35. SHOW INDEX STATUS syntax
   :name: show-index-status-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW INDEX index_name STATUS

Added in version 2.1.1-beta. Displays various per-index statistics.
Currently, those include:

.. raw:: html

   <div class="itemizedlist">

-  **indexed\_documents** and **indexed\_bytes**, number of the
   documents indexed and their text size in bytes, respectively.
-  **field\_tokens\_XXX**, sums of per-field lengths (in tokens) over
   the entire index (that is used internally in BM25A and BM25F
   functions for ranking purposes). Only available for indexes built
   with index\_field\_lengths=1.
-  **ram\_bytes**, total size (in bytes) of the RAM-resident index
   portion.
-  queries time statistics of last 1 minute, 5 minutes, 15 minutes and
   total since daemon start;data is encapsulated as a JSON object which
   includes number of queries, min,max,avg,95 and 99 percentile values;
   introduced in 2.3.2-beta
-  queries found rows statistics of last 1 minute, 5 minutes, 15 minutes
   and total since daemon start;data is encapsulated as a JSON object
   which includes number of queries, min,max,avg,95 and 99 percentile
   values; introduced in 2.3.2-beta

.. raw:: html

   </div>

.. code:: programlisting

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

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+------------------------------------+-------------------------------------------------+
| `Prev <sphinxql-show-profile.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-index-settings.html>`__   |
+------------------------------------------+------------------------------------+-------------------------------------------------+
| 8.34. SHOW PROFILE syntax                | `Home <index.html>`__              |  8.36. SHOW INDEX SETTINGS syntax               |
+------------------------------------------+------------------------------------+-------------------------------------------------+

.. raw:: html

   </div>
