preopen\_indexes
~~~~~~~~~~~~~~~~

Whether to forcibly preopen all indexes on startup. Optional, default is
1 (preopen everything).

Starting with 2.0.1-beta, the default value for this option is now 1
(foribly preopen all indexes). In prior versions, it used to be 0 (use
per-index settings).

When set to 1, this directive overrides and enforces
`preopen <../../index_configuration_options/preopen.rst>`__ on all
indexes. They will be preopened, no matter what is the per-index
``preopen`` setting. When set to 0, per-index settings can take effect.
(And they default to 0.)

Pre-opened indexes avoid races between search queries and rotations that
can cause queries to fail occasionally. They also make ``searchd`` use
more file handles. In most scenarios it's therefore preferred and
recommended to preopen indexes.

Example:
^^^^^^^^

::


    preopen_indexes = 1

