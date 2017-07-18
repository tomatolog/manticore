.. raw:: html

   <div class="navheader">

12.5.9. plugin\_dir
`Prev <conf-rlp-max-batch-docs.html>`__ 
12.5. Common section configuration options
 `Next <changelog.html>`__

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

.. rubric:: 12.5.9. plugin\_dir
   :name: plugin_dir
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Trusted location for the dynamic libraries (UDFs). Optional, default is
empty (no location). Introduced in version 2.0.1-beta.

Specifies the trusted directory from which the `UDF
libraries <sphinx-udfs.html>`__ can be loaded. Requires `workers =
thread <conf-workers.html>`__ to take effect.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    plugin_dir = /usr/local/sphinx/lib

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+----------------------------------------+
| `Prev <conf-rlp-max-batch-docs.html>`__    | `Up <confgroup-common.html>`__   |  `Next <changelog.html>`__             |
+--------------------------------------------+----------------------------------+----------------------------------------+
| 12.5.8. rlp\_max\_batch\_docs              | `Home <index.html>`__            |  Appendix A. Sphinx revision history   |
+--------------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
