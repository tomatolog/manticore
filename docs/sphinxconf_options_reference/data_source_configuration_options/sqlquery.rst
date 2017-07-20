sql\_query
~~~~~~~~~~

Main document fetch query. Mandatory, no default value. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

There can be only one main query. This is the query which is used to
retrieve documents from SQL server. You can specify up to 32 full-text
fields (formally, upto SPH\_MAX\_FIELDS from sphinx.h), and an arbitrary
amount of attributes. All of the columns that are neither document ID
(the first one) nor attributes will be full-text indexed.

Document ID **MUST** be the very first field, and it **MUST BE UNIQUE
UNSIGNED POSITIVE (NON-ZERO, NON-NEGATIVE) INTEGER NUMBER**. It can be
either 32-bit or 64-bit, depending on how you built Manticore; by default
it builds with 32-bit IDs support but ``--enable-id64`` option to
``configure`` allows to build with 64-bit document and word IDs support.

Example:
^^^^^^^^

::


    sql_query = \
        SELECT id, group_id, UNIX_TIMESTAMP(date_added) AS date_added, \
            title, content \
        FROM documents

