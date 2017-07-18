.. raw:: html

   <div class="navheader">

8.41. DROP PLUGIN syntax
`Prev <sphinxql-create-plugin.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-plugins.html>`__

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

.. rubric:: 8.41. DROP PLUGIN syntax
   :name: drop-plugin-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    DROP PLUGIN plugin_name TYPE 'plugin_type'

Added in 2.2.2-beta. Markes the specified plugin for unloading. The
unloading is **not** immediate, because the concurrent queries might be
using it. However, after a DROP new queries will not be able to use it.
Then, once all the currently executing queries using it are completed,
the plugin will be unloaded. Once all the plugins from the given library
are unloaded, the library is also automatically unloaded.

.. code:: programlisting

    mysql> DROP PLUGIN myranker TYPE 'ranker';
    Query OK, 0 rows affected (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+------------------------------------------+
| `Prev <sphinxql-create-plugin.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-plugins.html>`__   |
+-------------------------------------------+------------------------------------+------------------------------------------+
| 8.40. CREATE PLUGIN syntax                | `Home <index.html>`__              |  8.42. SHOW PLUGINS syntax               |
+-------------------------------------------+------------------------------------+------------------------------------------+

.. raw:: html

   </div>
