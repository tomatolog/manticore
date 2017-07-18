CREATE PLUGIN syntax
--------------------

::


    CREATE PLUGIN plugin_name TYPE 'plugin_type' SONAME 'plugin_library'

Added in 2.2.2-beta. Loads the given library (if it is not loaded yet)
and loads the specified plugin from it. As of 2.2.2-beta, the known
plugin types are:

-  ranker

-  index\_token\_filter

-  query\_token\_filter

Refer to `the section called “Sphinx plugins” <../sphinx_plugins.html>`__
for more information regarding writing the plugins.

::


    mysql> CREATE PLUGIN myranker TYPE 'ranker' SONAME 'myplugins.so';
    Query OK, 0 rows affected (0.00 sec)

