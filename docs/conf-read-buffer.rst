.. raw:: html

   <div class="navheader">

12.4.21. read\_buffer
`Prev <conf-listen-backlog.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-read-unhinted.html>`__

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

.. rubric:: 12.4.21. read\_buffer
   :name: read_buffer
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Per-keyword read buffer size. Optional, default is 256K.

For every keyword occurrence in every search query, there are two
associated read buffers (one for document list and one for hit list).
This setting lets you control their sizes, increasing per-query RAM use,
but possibly decreasing IO time.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    read_buffer = 1M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+-----------------------------------+---------------------------------------+
| `Prev <conf-listen-backlog.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-read-unhinted.html>`__   |
+----------------------------------------+-----------------------------------+---------------------------------------+
| 12.4.20. listen\_backlog               | `Home <index.html>`__             |  12.4.22. read\_unhinted              |
+----------------------------------------+-----------------------------------+---------------------------------------+

.. raw:: html

   </div>
