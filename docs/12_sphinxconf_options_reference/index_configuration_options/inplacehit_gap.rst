inplace\_hit\_gap
~~~~~~~~~~~~~~~~~

`In-place
inversion <../../index_configuration_options/inplaceenable.html>`__
fine-tuning option. Controls preallocated hitlist gap size. Optional,
default is 0. Introduced in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

Example:
^^^^^^^^

::


    inplace_hit_gap = 1M

