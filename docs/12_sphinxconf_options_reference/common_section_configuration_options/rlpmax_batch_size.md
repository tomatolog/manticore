### rlp_max_batch_size {#rlp-max-batch-size}

Maximum total size of documents batched before processing them by the RLP. Optional, default is 51200. Do not set this value to more than 10Mb because sphinx splits large documents to 10Mb chunks before processing them by the RLP. This option has effect only if `morphology = rlp_chinese_batched` is specified. Added in 2.2.1-beta.

#### Example: {#example}

```

rlp_max_batch_size = 100k

```