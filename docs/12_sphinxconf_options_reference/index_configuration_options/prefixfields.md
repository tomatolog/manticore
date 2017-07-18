### prefix_fields {#prefix-fields}

The list of full-text fields to limit prefix indexing to. Applies to dict=crc only. Optional, default is empty (index all fields in prefix mode).

Because prefix indexing impacts both indexing and searching performance, it might be desired to limit it to specific full-text fields only: for instance, to provide prefix searching through URLs, but not through page contents. prefix_fields specifies what fields will be prefix-indexed; all other fields will be indexed in normal mode. The value format is a comma-separated list of field names.

#### Example: {#example}

```

prefix_fields = url, domain

```