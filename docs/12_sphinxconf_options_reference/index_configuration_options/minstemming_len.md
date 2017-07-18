### min_stemming_len {#min-stemming-len}

Minimum word length at which to enable stemming. Optional, default is 1 (stem everything). Introduced in version 0.9.9-rc1.

Stemmers are not perfect, and might sometimes produce undesired results. For instance, running &quot;gps&quot; keyword through Porter stemmer for English results in &quot;gp&quot;, which is not really the intent. `min_stemming_len` feature lets you suppress stemming based on the source word length, ie. to avoid stemming too short words. Keywords that are shorter than the given threshold will not be stemmed. Note that keywords that are exactly as long as specified &lt;b&gt;will&lt;/b&gt; be stemmed. So in order to avoid stemming 3-character keywords, you should specify 4 for the value. For more finely grained control, refer to [wordforms](../../index_configuration_options/wordforms.md) feature.

#### Example: {#example}

```

min_stemming_len = 4

```