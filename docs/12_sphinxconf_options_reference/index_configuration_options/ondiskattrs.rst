ondisk\_attrs
~~~~~~~~~~~~~

Allows for fine-grain control over how attributes are loaded into memory
when using indexes with external storage. It is now possible (since
version 2.2.1-beta) to keep attributes on disk. Although, the daemon
does map them to memory and the OS loads small chunks of data on demand.
This allows use of docinfo = extern instead of docinfo = inline, but
still leaves plenty of free memory for cases when you have large
collections of pooled attributes (string/JSON/MVA) or when you're using
many indexes per daemon that don't consume memory. It is not possible to
update attributes left on disk when this option is enabled and the
constraint of 4Gb of entries per pool is still in effect.

Note that this option also affects RT indexes. When it is enabled, all
atribute updates will be disabled, and also all disk chunks of RT
indexes will behave described above. However inserting and deleting of
docs from RT indexes is still possible with enabled ondisk\_attrs.

Possible values:
^^^^^^^^^^^^^^^^

-  0 - disabled and default value, all attributes are loaded in memory
   (the normal behaviour of docinfo = extern)
-  1 - all attributes stay on disk. Daemon loads no files (spa, spm,
   sps). This is the most memory conserving mode, however it is also the
   slowest as the whole doc-id-list and block index doesn't load.
-  pool - only pooled attributes stay on disk. Pooled attributes are
   string, MVA, and JSON attributes (sps, spm files). Scalar attributes
   stored in docinfo (spa file) load as usual.

This option does not affect indexing in any way, it only requires daemon
restart.

Example:
^^^^^^^^

::


    ondisk_attrs = pool #keep pooled attributes on disk

