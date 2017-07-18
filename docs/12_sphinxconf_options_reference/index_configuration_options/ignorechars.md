### ignore_chars {#ignore-chars}

Ignored characters list. Optional, default is empty.

Useful in the cases when some characters, such as soft hyphenation mark (U+00AD), should be not just treated as separators but rather fully ignored. For example, if &#039;-&#039; is simply not in the charset_table, &quot;abc-def&quot; text will be indexed as &quot;abc&quot; and &quot;def&quot; keywords. On the contrary, if &#039;-&#039; is added to ignore_chars list, the same text will be indexed as a single &quot;abcdef&quot; keyword.

The syntax is the same as for [charset_table](../../index_configuration_options/charsettable.md), but it&#039;s only allowed to declare characters, and not allowed to map them. Also, the ignored characters must not be present in charset_table.

#### Example: {#example}

```

ignore_chars = U+AD

```