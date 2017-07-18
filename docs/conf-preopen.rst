.. raw:: html

   <div class="navheader">

12.2.36. preopen
`Prev <conf-agent-query-timeout.html>`__ 
12.2. Index configuration options
 `Next <conf-inplace-enable.html>`__

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

.. rubric:: 12.2.36. preopen
   :name: preopen
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Whether to pre-open all index files, or open them per each query.
Optional, default is 0 (do not preopen).

This option tells ``searchd`` that it should pre-open all index files on
startup (or rotation) and keep them open while it runs. Currently, the
default mode is **not** to pre-open the files (this may change in the
future). Preopened indexes take a few (currently 2) file descriptors per
index. However, they save on per-query ``open()`` calls; and also they
are invulnerable to subtle race conditions that may happen during index
rotation under high load. On the other hand, when serving many indexes
(100s to 1000s), it still might be desired to open the on per-query
basis in order to save file descriptors.

This directive does not affect ``indexer`` in any way, it only affects
``searchd``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    preopen = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+---------------------------------+----------------------------------------+
| `Prev <conf-agent-query-timeout.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-inplace-enable.html>`__   |
+---------------------------------------------+---------------------------------+----------------------------------------+
| 12.2.35. agent\_query\_timeout              | `Home <index.html>`__           |  12.2.37. inplace\_enable              |
+---------------------------------------------+---------------------------------+----------------------------------------+

.. raw:: html

   </div>
