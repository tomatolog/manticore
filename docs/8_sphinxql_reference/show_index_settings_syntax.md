## SHOW INDEX SETTINGS syntax {#show-index-settings-syntax}

```

SHOW INDEX index_name[.N | CHUNK N] SETTINGS

```

Displays per-index settings in a `sphinx.conf` compliant file format, similar to the [--dumpconfig](../indextool_command_reference.md) option of the indextool. The report provides a breakdown of all the index settings, including tokenizer and dictionary options. You may also specify a particular [chunk number](../index_configuration_options/rtmem_limit.md) for the RT indexes.