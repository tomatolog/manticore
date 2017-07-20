inplace\_write\_factor
~~~~~~~~~~~~~~~~~~~~~~

`In-place inversion <#inplace-write-factor>`__ fine-tuning option.
Controls in-place write buffer size within indexing memory arena.
Optional, default is 0.1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

Example:
^^^^^^^^

::


    inplace_write_factor = 0.1

