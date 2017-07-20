collation\_server
~~~~~~~~~~~~~~~~~

Default server collation. Optional, default is libc\_ci.

Specifies the default collation used for incoming requests. The
collation can be overridden on a per-query basis. Refer to `the section
called “Collations” <../../collations.md>`__ section for the list of
available collations and other details.

Example:
^^^^^^^^

::


    collation_server = utf8_ci

