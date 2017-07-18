### exceptions {#exceptions}

Tokenizing exceptions file. Optional, default is empty.

Exceptions allow to map one or more tokens (including tokens with characters that would normally be excluded) to a single keyword. They are similar to [wordforms](../../index_configuration_options/wordforms.md) in that they also perform mapping, but have a number of important differences.

Starting with version 2.1.1-beta small enough files are stored in the index header, see [the section called “embedded_limit”](../../index_configuration_options/embeddedlimit.md) for details.

Short summary of the differences is as follows:

*   exceptions are case sensitive, wordforms are not;

*   exceptions can use special characters that are &lt;b&gt;not&lt;/b&gt; in charset_table, wordforms fully obey charset_table;

*   exceptions can underperform on huge dictionaries, wordforms handle millions of entries well.

The expected file format is also plain text, with one line per exception, and the line format is as follows:

```

map-from-tokens => map-to-token

```

Example file:

```

at & t => at&t
AT&T => AT&T
Standarten   Fuehrer => standartenfuhrer
Standarten Fuhrer => standartenfuhrer
MS Windows => ms windows
Microsoft Windows => ms windows
C++ => cplusplus
c++ => cplusplus
C plus plus => cplusplus

```

All tokens here are case sensitive: they will &lt;b&gt;not&lt;/b&gt; be processed by [charset_table](../../index_configuration_options/charsettable.md) rules. Thus, with the example exceptions file above, &quot;at&amp;t&quot; text will be tokenized as two keywords &quot;at&quot; and &quot;t&quot;, because of lowercase letters. On the other hand, &quot;AT&amp;T&quot; will match exactly and produce single &quot;AT&amp;T&quot; keyword.

Note that this map-to keyword is a) always interpreted as a _single_ word, and b) is both case and space sensitive! In our sample, &quot;ms windows&quot; query will _not_ match the document with &quot;MS Windows&quot; text. The query will be interpreted as a query for two keywords, &quot;ms&quot; and &quot;windows&quot;. And what &quot;MS Windows&quot; gets mapped to is a _single_ keyword &quot;ms windows&quot;, with a space in the middle. On the other hand, &quot;standartenfuhrer&quot; will retrieve documents with &quot;Standarten Fuhrer&quot; or &quot;Standarten Fuehrer&quot; contents (capitalized exactly like this), or any capitalization variant of the keyword itself, eg. &quot;staNdarTenfUhreR&quot;. (It won&#039;t catch &quot;standarten fuhrer&quot;, however: this text does not match any of the listed exceptions because of case sensitivity, and gets indexed as two separate keywords.)

Whitespace in the map-from tokens list matters, but its amount does not. Any amount of the whitespace in the map-form list will match any other amount of whitespace in the indexed document or query. For instance, &quot;AT &amp; T&quot; map-from token will match &quot;AT    &amp;  T&quot; text, whatever the amount of space in both map-from part and the indexed text. Such text will therefore be indexed as a special &quot;AT&amp;T&quot; keyword, thanks to the very first entry from the sample.

Exceptions also allow to capture special characters (that are exceptions from general [charset_table](../../index_configuration_options/charsettable.md) rules; hence the name). Assume that you generally do not want to treat &#039;+&#039; as a valid character, but still want to be able search for some exceptions from this rule such as &#039;C++&#039;. The sample above will do just that, totally independent of what characters are in the table and what are not.

Exceptions are applied to raw incoming document and query data during indexing and searching respectively. Therefore, to pick up changes in the file it&#039;s required to reindex and restart `searchd`.

#### Example: {#example}

```

exceptions = /usr/local/sphinx/data/exceptions.txt

```