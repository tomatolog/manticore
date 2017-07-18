### blend_chars {#blend-chars}

Blended characters list. Optional, default is empty. Introduced in version 1.10-beta.

Blended characters are indexed both as separators and valid characters. For instance, assume that &amp; is configured as blended and AT&amp;T occurs in an indexed document. Three different keywords will get indexed, namely &quot;at&amp;t&quot;, treating blended characters as valid, plus &quot;at&quot; and &quot;t&quot;, treating them as separators.

Positions for tokens obtained by replacing blended characters with whitespace are assigned as usual, so regular keywords will be indexed just as if there was no `blend_chars` specified at all. An additional token that mixes blended and non-blended characters will be put at the starting position. For instance, if the field contents are &quot;AT&amp;T company&quot; occurs in the very beginning of the text field, &quot;at&quot; will be given position 1, &quot;t&quot; position 2, &quot;company&quot; position 3, and &quot;AT&amp;T&quot; will also be given position 1 (&quot;blending&quot; with the opening regular keyword). Thus, querying for either AT&amp;T or just AT will match that document, and querying for &quot;AT T&quot; as a phrase also match it. Last but not least, phrase query for &quot;AT&amp;T company&quot; will _also_ match it, despite the position

Blended characters can overlap with special characters used in query syntax (think of T-Mobile or @twitter). Where possible, query parser will automatically handle blended character as blended. For instance, &quot;hello @twitter&quot; within quotes (a phrase operator) would handle @-sign as blended, because @-syntax for field operator is not allowed within phrases. Otherwise, the character would be handled as an operator. So you might want to escape the keywords.

Starting with version 2.0.1-beta, blended characters can be remapped, so that multiple different blended characters could be normalized into just one base form. This is useful when indexing multiple alternative Unicode codepoints with equivalent glyphs.

#### Example: {#example}

```

blend_chars = +, &, U+23
blend_chars = +, &->+ # 2.0.1 and above

```