### infix_fields {#infix-fields}

The list of full-text fields to limit infix indexing to. Applies to dict=crc only. Optional, default is empty (index all fields in infix mode).

Similar to [prefix_fields](../../index_configuration_options/prefixfields.md), but lets you limit infix-indexing to given fields.

#### Example: {#example}

```

infix_fields = url, domain

```