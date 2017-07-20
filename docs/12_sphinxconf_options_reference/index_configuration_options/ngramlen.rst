ngram\_len
~~~~~~~~~~

N-gram lengths for N-gram indexing. Optional, default is 0 (disable
n-gram indexing). Known values are 0 and 1 (other lengths to be
implemented).

N-grams provide basic CJK (Chinese, Japanese, Korean) support for
unsegmented texts. The issue with CJK searching is that there could be
no clear separators between the words. Ideally, the texts would be
filtered through a special program called segmenter that would insert
separators in proper locations. However, segmenters are slow and error
prone, and it's common to index contiguous groups of N characters, or
n-grams, instead.

When this feature is enabled, streams of CJK characters are indexed as
N-grams. For example, if incoming text is “ABCDEF” (where A to F
represent some CJK characters) and length is 1, in will be indexed as if
it was “A B C D E F”. (With length equal to 2, it would produce “AB BC
CD DE EF”; but only 1 is supported at the moment.) Only those characters
that are listed in
`ngram\_chars <../../index_configuration_options/ngramchars.md>`__ table
will be split this way; other ones will not be affected.

Note that if search query is segmented, ie. there are separators between
individual words, then wrapping the words in quotes and using extended
mode will result in proper matches being found even if the text was
<b>not</b> segmented. For instance, assume that the original query is BC
DEF. After wrapping in quotes on the application side, it should look
like “BC” “DEF” (*with* quotes). This query will be passed to Sphinx and
internally split into 1-grams too, resulting in “B C” “D E F” query,
still with quotes that are the phrase matching operator. And it will
match the text even though there were no separators in the text.

Even if the search query is not segmented, Sphinx should still produce
good results, thanks to phrase based ranking: it will pull closer phrase
matches (which in case of N-gram CJK words can mean closer
multi-character word matches) to the top.

Example:
^^^^^^^^

::


    ngram_len = 1

