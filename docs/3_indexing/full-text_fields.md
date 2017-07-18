## Full-text fields {#full-text-fields}

Full-text fields (or just _fields_ for brevity) are the textual document contents that get indexed by Sphinx, and can be (quickly) searched for keywords.

Fields are named, and you can limit your searches to a single field (eg. search through &quot;title&quot; only) or a subset of fields (eg. to &quot;title&quot; and &quot;abstract&quot; only). Sphinx index format generally supports up to 256 fields. However, up to version 2.0.1-beta indexes were forcibly limited by 32 fields, because of certain complications in the matching engine. Full support for up to 256 fields was added in version 2.0.2-beta.

Note that the original contents of the fields are &lt;b&gt;not&lt;/b&gt; stored in the Sphinx index. The text that you send to Sphinx gets processed, and a full-text index (a special data structure that enables quick searches for a keyword) gets built from that text. But the original text contents are then simply discarded. Sphinx assumes that you store those contents elsewhere anyway.

Moreover, it is impossible to _fully_ reconstruct the original text, because the specific whitespace, capitalization, punctuation, etc will all be lost during indexing. It is theoretically possible to partially reconstruct a given document from the Sphinx full-text index, but that would be a slow process (especially if the [CRC dictionary](../index_configuration_options/dict.md) is used, which does not even store the original keywords and works with their hashes instead).