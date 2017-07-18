.. raw:: html

   <div class="navheader">

8.40. CREATE PLUGIN syntax
`Prev <sphinxql-show-databases.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-drop-plugin.html>`__

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

.. rubric:: 8.40. CREATE PLUGIN syntax
   :name: create-plugin-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    CREATE PLUGIN plugin_name TYPE 'plugin_type' SONAME 'plugin_library'

Added in 2.2.2-beta. Loads the given library (if it is not loaded yet)
and loads the specified plugin from it. As of 2.2.2-beta, the known
plugin types are:

.. raw:: html

   <div class="itemizedlist">

-  ranker

-  index\_token\_filter

-  query\_token\_filter

.. raw:: html

   </div>

Refer to `Section 6.2, “Sphinx plugins” <sphinx-plugins.html>`__ for
more information regarding writing the plugins.

.. code:: programlisting

    mysql> CREATE PLUGIN myranker TYPE 'ranker' SONAME 'myplugins.so';
    Query OK, 0 rows affected (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+------------------------------------+-----------------------------------------+
| `Prev <sphinxql-show-databases.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-drop-plugin.html>`__   |
+--------------------------------------------+------------------------------------+-----------------------------------------+
| 8.39. SHOW DATABASES syntax                | `Home <index.html>`__              |  8.41. DROP PLUGIN syntax               |
+--------------------------------------------+------------------------------------+-----------------------------------------+

.. raw:: html

   </div>
