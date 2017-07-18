### ngram_len {#ngram-len}

N-gram lengths for N-gram indexing. Optional, default is 0 (disable n-gram indexing). Known values are 0 and 1 (other lengths to be implemented).

N-grams provide basic CJK (Chinese, Japanese, Korean) support for unsegmented texts. The issue with CJK searching is that there could be no clear separators between the words. Ideally, the texts would be filtered through a special program called segmenter that would insert separators in proper locations. However, segmenters are slow and error prone, and it&#039;s common to index contiguous groups of N characters, or n-grams, instead.

When this feature is enabled, streams of CJK characters are indexed as N-grams. For example, if incoming text is &quot;ABCDEF&quot; (where A to F represent some CJK characters) and length is 1, in will be indexed as if it was &quot;A B C D E F&quot;. (With length equal to 2, it would produce &quot;AB BC CD DE EF&quot;; but only 1 is supported at the moment.) Only those characters that are listed in [ngram_chars](../../index_configuration_options/ngramchars.md) table will be split this way; other ones will not be affected.

Note that if search query is segmented, ie. there are separators between individual words, then wrapping the words in quotes and using extended mode will result in proper matches being found even if the text was &lt;b&gt;not&lt;/b&gt; segmented. For instance, assume that the original query is BC DEF. After wrapping in quotes on the application side, it should look like &quot;BC&quot; &quot;DEF&quot; (_with_ quotes). This query will be passed to Sphinx and internally split into 1-grams too, resulting in &quot;B C&quot; &quot;D E F&quot; query, still with quotes that are the phrase matching operator. And it will match the text even though there were no separators in the text.

Even if the search query is not segmented, Sphinx should still produce good results, thanks to phrase based ranking: it will pull closer phrase matches (which in case of N-gram CJK words can mean closer multi-character word matches) to the top.

#### Example: {#example}

```

ngram_len = 1

```