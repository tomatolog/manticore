## Charsets, case folding, translation tables, and replacement rules {#charsets-case-folding-translation-tables-and-replacement-rules}

When indexing some index, Sphinx fetches documents from the specified sources, splits the text into words, and does case folding so that &quot;Abc&quot;, &quot;ABC&quot; and &quot;abc&quot; would be treated as the same word (or, to be pedantic, _term_).

To do that properly, Sphinx needs to know

*   what encoding is the source text in (and this encoding should always be UTF-8);

*   what characters are letters and what are not;

*   what letters should be folded to what letters.

This should be configured on a per-index basis using `[charset_table](../index_configuration_options/charsettable.md)` option. `[charset_table](../index_configuration_options/charsettable.md)` specifies the table that maps letter characters to their case folded versions. The characters that are not in the table are considered to be non-letters and will be treated as word separators when indexing or searching through this index.

Default tables currently include English and Russian characters. Please do submit your tables for other languages!

As of version 2.1.1-beta, you can also specify text pattern replacement rules. For example, given the rules

```

regexp_filter = \b(\d+)\" => \1 inch
regexp_filter = (BLUE|RED) => COLOR

```

the text &#039;RED TUBE 5&quot; LONG&#039; would be indexed as &#039;COLOR TUBE 5 INCH LONG&#039;, and &#039;PLANK 2&quot; x 4&quot;&#039; as &#039;PLANK 2 INCH x 4 INCH&#039;. Rules are applied in the given order. Text in queries is also replaced; a search for &quot;BLUE TUBE&quot; would actually become a search for &quot;COLOR TUBE&quot;. Note that Sphinx must be built with the --with-re2 option to use this feature.