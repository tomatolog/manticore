inplace\_docinfo\_gap
~~~~~~~~~~~~~~~~~~~~~

`In-place
inversion <../../index_configuration_options/inplaceenable.md>`__
fine-tuning option. Controls preallocated docinfo gap size. Optional,
default is 0. Introduced in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

Example:
^^^^^^^^

::


    inplace_docinfo_gap = 1M

