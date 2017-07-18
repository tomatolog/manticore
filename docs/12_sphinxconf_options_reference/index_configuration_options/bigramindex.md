### bigram_index {#bigram-index}

Bigram indexing mode. Optional, default is none. Added in 2.1.1-beta.

Bigram indexing is a feature to accelerate phrase searches. When indexing, it stores a document list for either all or some of the adjacent words pairs into the index. Such a list can then be used at searching time to significantly accelerate phrase or sub-phrase matching.

`bigram_index` controls the selection of specific word pairs. The known modes are:

*   `all`, index every single word pair. (NB: probably totally not worth it even on a moderately sized index, but added anyway for the sake of completeness.)

*   `first_freq`, only index word pairs where the _first_ word is in a list of frequent words (see [the section called “bigram_freq_words”](../../index_configuration_options/bigramfreq_words.md)). For example, with `bigram_freq_words = the, in, i, a`, indexing &quot;alone in the dark&quot; text will result in &quot;in the&quot; and &quot;the dark&quot; pairs being stored as bigrams, because they begin with a frequent keyword (either &quot;in&quot; or &quot;the&quot; respectively), but &quot;alone in&quot; would &lt;b&gt;not&lt;/b&gt; be indexed, because &quot;in&quot; is a _second_ word in that pair.

*   `both_freq`, only index word pairs where both words are frequent. Continuing with the same example, in this mode indexing &quot;alone in the dark&quot; would only store &quot;in the&quot; (the very worst of them all from searching perspective) as a bigram, but none of the other word pairs.

For most usecases, `both_freq` would be the best mode, but your mileage may vary.

#### Example: {#example}

```

bigram_freq_words = both_freq

```