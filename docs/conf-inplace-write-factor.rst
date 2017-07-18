.. raw:: html

   <div class="navheader">

12.2.41. inplace\_write\_factor
`Prev <conf-inplace-reloc-factor.html>`__ 
12.2. Index configuration options
 `Next <conf-index-exact-words.html>`__

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

.. rubric:: 12.2.41. inplace\_write\_factor
   :name: inplace_write_factor
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

`In-place inversion <conf-inplace-write-factor.html>`__ fine-tuning
option. Controls in-place write buffer size within indexing memory
arena. Optional, default is 0.1. Introduced in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    inplace_write_factor = 0.1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+---------------------------------+-------------------------------------------+
| `Prev <conf-inplace-reloc-factor.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-index-exact-words.html>`__   |
+----------------------------------------------+---------------------------------+-------------------------------------------+
| 12.2.40. inplace\_reloc\_factor              | `Home <index.html>`__           |  12.2.42. index\_exact\_words             |
+----------------------------------------------+---------------------------------+-------------------------------------------+

.. raw:: html

   </div>
