infix\_fields
~~~~~~~~~~~~~

The list of full-text fields to limit infix indexing to. Applies to
dict=crc only. Optional, default is empty (index all fields in infix
mode).

Similar to
`prefix\_fields <../../index_configuration_options/prefixfields.md>`__,
but lets you limit infix-indexing to given fields.

Example:
^^^^^^^^

::


    infix_fields = url, domain

