CREATE PLUGIN syntax
--------------------

::


    CREATE PLUGIN plugin_name TYPE 'plugin_type' SONAME 'plugin_library'

Loads the given library (if it is not loaded yet) and loads the
specified plugin from it. The known plugin types are:

-  ranker

-  index\_token\_filter

-  query\_token\_filter

Refer to `the section called “Manticore plugins” <../sphinx_plugins.md>`__
for more information regarding writing the plugins.

::


    mysql> CREATE PLUGIN myranker TYPE 'ranker' SONAME 'myplugins.so';
    Query OK, 0 rows affected (0.00 sec)

