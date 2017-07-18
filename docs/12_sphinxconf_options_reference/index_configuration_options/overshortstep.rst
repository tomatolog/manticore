overshort\_step
~~~~~~~~~~~~~~~

Position increment on overshort (less that
`min\_word\_len <../../index_configuration_options/minword_len.rst>`__)
keywords. Optional, allowed values are 0 and 1, default is 1. Introduced
in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

Example:
^^^^^^^^

::


    overshort_step = 1

