### inplace_reloc_factor {#inplace-reloc-factor}

[In-place inversion](#inplace-reloc-factor) fine-tuning option. Controls relocation buffer size within indexing memory arena. Optional, default is 0.1. Introduced in version 0.9.9-rc1.

This directive does not affect `searchd` in any way, it only affects `indexer`.

#### Example: {#example}

```

inplace_reloc_factor = 0.1

```