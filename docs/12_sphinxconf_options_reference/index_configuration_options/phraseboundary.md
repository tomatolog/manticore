### phrase_boundary {#phrase-boundary}

Phrase boundary characters list. Optional, default is empty.

This list controls what characters will be treated as phrase boundaries, in order to adjust word positions and enable phrase-level search emulation through proximity search. The syntax is similar to [charset_table](../../index_configuration_options/charsettable.md). Mappings are not allowed and the boundary characters must not overlap with anything else.

On phrase boundary, additional word position increment (specified by [phrase_boundary_step](../../index_configuration_options/phraseboundary_step.md)) will be added to current word position. This enables phrase-level searching through proximity queries: words in different phrases will be guaranteed to be more than phrase_boundary_step distance away from each other; so proximity search within that distance will be equivalent to phrase-level search.

Phrase boundary condition will be raised if and only if such character is followed by a separator; this is to avoid abbreviations such as S.T.A.L.K.E.R or URLs being treated as several phrases.

#### Example: {#example}

```

phrase_boundary = ., ?, !, U+2026 # horizontal ellipsis

```