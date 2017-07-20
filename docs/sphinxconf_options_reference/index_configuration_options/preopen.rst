preopen
~~~~~~~

Whether to pre-open all index files, or open them per each query.
Optional, default is 0 (do not preopen).

This option tells ``searchd`` that it should pre-open all index files on
startup (or rotation) and keep them open while it runs. Currently, the
default mode is <b>not</b> to pre-open the files (this may change in the
future). Preopened indexes take a few (currently 2) file descriptors per
index. However, they save on per-query ``open()`` calls; and also they
are invulnerable to subtle race conditions that may happen during index
rotation under high load. On the other hand, when serving many indexes
(100s to 1000s), it still might be desired to open the on per-query
basis in order to save file descriptors.

This directive does not affect ``indexer`` in any way, it only affects
``searchd``.

Example:
^^^^^^^^

::


    preopen = 1

