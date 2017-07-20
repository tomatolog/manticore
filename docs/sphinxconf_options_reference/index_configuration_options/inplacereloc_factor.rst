inplace\_reloc\_factor
~~~~~~~~~~~~~~~~~~~~~~

`In-place inversion <#inplace-reloc-factor>`__ fine-tuning option.
Controls relocation buffer size within indexing memory arena. Optional,
default is 0.1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

Example:
^^^^^^^^

::


    inplace_reloc_factor = 0.1

