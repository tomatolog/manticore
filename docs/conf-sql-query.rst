.. raw:: html

   <div class="navheader">

12.1.12. sql\_query
`Prev <conf-sql-query-pre.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-joined-field.html>`__

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

.. rubric:: 12.1.12. sql\_query
   :name: sql_query
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Main document fetch query. Mandatory, no default value. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

There can be only one main query. This is the query which is used to
retrieve documents from SQL server. You can specify up to 32 full-text
fields (formally, upto SPH\_MAX\_FIELDS from sphinx.h), and an arbitrary
amount of attributes. All of the columns that are neither document ID
(the first one) nor attributes will be full-text indexed.

Document ID **MUST** be the very first field, and it **MUST BE UNIQUE
UNSIGNED POSITIVE (NON-ZERO, NON-NEGATIVE) INTEGER NUMBER**. It can be
either 32-bit or 64-bit, depending on how you built Sphinx; by default
it builds with 32-bit IDs support but ``--enable-id64`` option to
``configure`` allows to build with 64-bit document and word IDs support.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_query = \
        SELECT id, group_id, UNIX_TIMESTAMP(date_added) AS date_added, \
            title, content \
        FROM documents

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+----------------------------------+------------------------------------------+
| `Prev <conf-sql-query-pre.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-joined-field.html>`__   |
+---------------------------------------+----------------------------------+------------------------------------------+
| 12.1.11. sql\_query\_pre              | `Home <index.html>`__            |  12.1.13. sql\_joined\_field             |
+---------------------------------------+----------------------------------+------------------------------------------+

.. raw:: html

   </div>
