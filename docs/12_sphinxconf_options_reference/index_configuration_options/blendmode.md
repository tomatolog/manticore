### blend_mode {#blend-mode}

Blended tokens indexing mode. Optional, default is `trim_none`. Introduced in version 2.0.1-beta.

By default, tokens that mix blended and non-blended characters get indexed in there entirety. For instance, when both at-sign and an exclamation are in `blend_chars`, &quot;@dude!&quot; will get result in two tokens indexed: &quot;@dude!&quot; (with all the blended characters) and &quot;dude&quot; (without any). Therefore &quot;@dude&quot; query will _not_ match it.

`blend_mode` directive adds flexibility to this indexing behavior. It takes a comma-separated list of options.

```

blend_mode = option [, option [, ...]]
option = trim_none | trim_head | trim_tail | trim_both | skip_pure

```

Options specify token indexing variants. If multiple options are specified, multiple variants of the same token will be indexed. Regular keywords (resulting from that token by replacing blended with whitespace) are always be indexed.

*   trim_none
*   Index the entire token.

*   trim_head
*   Trim heading blended characters, and index the resulting token.

*   trim_tail
*   Trim trailing blended characters, and index the resulting token.

*   trim_both
*   Trim both heading and trailing blended characters, and index the resulting token.

*   skip_pure
*   Do not index the token if it&#039;s purely blended, that is, consists of blended characters only.

Returning to the &quot;@dude!&quot; example above, setting `blend_mode = trim_head, trim_tail` will result in two tokens being indexed, &quot;@dude&quot; and &quot;dude!&quot;. In this particular example, `trim_both` would have no effect, because trimming both blended characters results in &quot;dude&quot; which is already indexed as a regular keyword. Indexing &quot;@U.S.A.&quot; with `trim_both` (and assuming that dot is blended two) would result in &quot;U.S.A&quot; being indexed. Last but not least, `skip_pure` enables you to fully ignore sequences of blended characters only. For example, &quot;one @@@ two&quot; would be indexed exactly as &quot;one two&quot;, and match that as a phrase. That is not the case by default because a fully blended token gets indexed and offsets the second keyword position.

Default behavior is to index the entire token, equivalent to `blend_mode = trim_none`.

#### Example: {#example}

```

blend_mode = trim_tail, skip_pure

```