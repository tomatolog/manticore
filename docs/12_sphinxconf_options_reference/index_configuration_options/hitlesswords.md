### hitless_words {#hitless-words}

Hitless words list. Optional, allowed values are &#039;all&#039;, or a list file name. Introduced in version 1.10-beta.

By default, Sphinx full-text index stores not only a list of matching documents for every given keyword, but also a list of its in-document positions (aka hitlist). Hitlists enables phrase, proximity, strict order and other advanced types of searching, as well as phrase proximity ranking. However, hitlists for specific frequent keywords (that can not be stopped for some reason despite being frequent) can get huge and thus slow to process while querying. Also, in some cases we might only care about boolean keyword matching, and never need position-based searching operators (such as phrase matching) nor phrase ranking.

`hitless_words` lets you create indexes that either do not have positional information (hitlists) at all, or skip it for specific keywords.

Hitless index will generally use less space than the respective regular index (about 1.5x can be expected). Both indexing and searching should be faster, at a cost of missing positional query and ranking support. When searching, positional queries (eg. phrase queries) will be automatically converted to respective non-positional (document-level) or combined queries. For instance, if keywords &quot;hello&quot; and &quot;world&quot; are hitless, &quot;hello world&quot; phrase query will be converted to (hello &amp; world) bag-of-words query, matching all documents that mention either of the keywords but not necessarily the exact phrase. And if, in addition, keywords &quot;simon&quot; and &quot;says&quot; are not hitless, &quot;simon says hello world&quot; will be converted to (&quot;simon says&quot; &amp; hello &amp; world) query, matching all documents that contain &quot;hello&quot; and &quot;world&quot; anywhere in the document, and also &quot;simon says&quot; as an exact phrase.

#### Example: {#example}

```

hitless_words = all

```