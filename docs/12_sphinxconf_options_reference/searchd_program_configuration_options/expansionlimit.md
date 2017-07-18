### expansion_limit {#expansion-limit}

The maximum number of expanded keywords for a single wildcard. Optional, default is 0 (no limit). Introduced in version 2.0.1-beta.

When doing substring searches against indexes built with `dict = keywords` enabled, a single wildcard may potentially result in thousands and even millions of matched keywords (think of matching &#039;a*&#039; against the entire Oxford dictionary). This directive lets you limit the impact of such expansions. Setting `expansion_limit = N` restricts expansions to no more than N of the most frequent matching keywords (per each wildcard in the query).

#### Example: {#example}

```

expansion_limit = 16

```