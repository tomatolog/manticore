### inplace_hit_gap {#inplace-hit-gap}

[In-place inversion](../../index_configuration_options/inplaceenable.md) fine-tuning option. Controls preallocated hitlist gap size. Optional, default is 0. Introduced in version 0.9.9-rc1.

This directive does not affect `searchd` in any way, it only affects `indexer`.

#### Example: {#example}

```

inplace_hit_gap = 1M

```