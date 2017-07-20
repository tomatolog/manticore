source
~~~~~~

Adds document source to local index. Multi-value, mandatory.

Specifies document source to get documents from when the current index
is indexed. There must be at least one source. There may be multiple
sources, without any restrictions on the source types: ie. you can pull
part of the data from MySQL server, part from PostgreSQL, part from the
filesystem using xmlpipe2 wrapper.

However, there are some restrictions on the source data. First, document
IDs must be globally unique across all sources. If that condition is not
met, you might get unexpected search results. Second, source schemas
must be the same in order to be stored within the same index.

No source ID is stored automatically. Therefore, in order to be able to
tell what source the matched document came from, you will need to store
some additional information yourself. Two typical approaches include:

1. mangling document ID and encoding source ID in it:

   ::


       source src1
       {
           sql_query = SELECT id*10+1, ... FROM table1
           ...
       }

       source src2
       {
           sql_query = SELECT id*10+2, ... FROM table2
           ...
       }

2. storing source ID simply as an attribute:

   ::


       source src1
       {
           sql_query = SELECT id, 1 AS source_id FROM table1
           sql_attr_uint = source_id
           ...
       }

       source src2
       {
           sql_query = SELECT id, 2 AS source_id FROM table2
           sql_attr_uint = source_id
           ...
       }

Example:
^^^^^^^^

::


    source = srcpart1
    source = srcpart2
    source = srcpart3

