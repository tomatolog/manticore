### ngram_chars {#ngram-chars}

N-gram characters list. Optional, default is empty.

To be used in conjunction with in [ngram_len](../../index_configuration_options/ngramlen.md), this list defines characters, sequences of which are subject to N-gram extraction. Words comprised of other characters will not be affected by N-gram indexing feature. The value format is identical to [charset_table](../../index_configuration_options/charsettable.md).

#### Example: {#example}

```

ngram_chars = U+3000..U+2FA1F

```