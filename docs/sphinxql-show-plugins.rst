.. raw:: html

   <div class="navheader">

8.42. SHOW PLUGINS syntax
`Prev <sphinxql-drop-plugin.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-reload-plugins.html>`__

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

.. rubric:: 8.42. SHOW PLUGINS syntax
   :name: show-plugins-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW PLUGINS

Added in 2.2.2-beta. Displays all the loaded plugins and UDFs. “Type”
column should be one of the udf, ranker, index\_token\_filter, or
query\_token\_filter. “Users” column is the number of thread that are
currently using that plugin in a query. “Extra” column is intended for
various additional plugin-type specific information; currently, it shows
the return type for the UDFs and is empty for all the other plugin
types.

.. code:: programlisting

    mysql> SHOW PLUGINS;
    +------+----------+----------------+-------+-------+
    | Type | Name     | Library        | Users | Extra |
    +------+----------+----------------+-------+-------+
    | udf  | sequence | udfexample.dll | 0     | INT   |
    +------+----------+----------------+-------+-------+
    1 row in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+------------------------------------+--------------------------------------------+
| `Prev <sphinxql-drop-plugin.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-reload-plugins.html>`__   |
+-----------------------------------------+------------------------------------+--------------------------------------------+
| 8.41. DROP PLUGIN syntax                | `Home <index.html>`__              |  8.43. RELOAD PLUGINS syntax               |
+-----------------------------------------+------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
