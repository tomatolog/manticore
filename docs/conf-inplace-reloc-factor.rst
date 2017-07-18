.. raw:: html

   <div class="navheader">

12.2.40. inplace\_reloc\_factor
`Prev <conf-inplace-docinfo-gap.html>`__ 
12.2. Index configuration options
 `Next <conf-inplace-write-factor.html>`__

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

.. rubric:: 12.2.40. inplace\_reloc\_factor
   :name: inplace_reloc_factor
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

`In-place inversion <conf-inplace-reloc-factor.html>`__ fine-tuning
option. Controls relocation buffer size within indexing memory arena.
Optional, default is 0.1. Introduced in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    inplace_reloc_factor = 0.1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+---------------------------------+----------------------------------------------+
| `Prev <conf-inplace-docinfo-gap.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-inplace-write-factor.html>`__   |
+---------------------------------------------+---------------------------------+----------------------------------------------+
| 12.2.39. inplace\_docinfo\_gap              | `Home <index.html>`__           |  12.2.41. inplace\_write\_factor             |
+---------------------------------------------+---------------------------------+----------------------------------------------+

.. raw:: html

   </div>
