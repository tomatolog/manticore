bigram\_freq\_words
~~~~~~~~~~~~~~~~~~~

A list of keywords considered “frequent” when indexing bigrams.
Optional, default is empty. Added in 2.1.1-beta.

Bigram indexing is a feature to accelerate phrase searches. When
indexing, it stores a document list for either all or some of the
adjacent words pairs into the index. Such a list can then be used at
searching time to significantly accelerate phrase or sub-phrase
matching.

Some of the bigram indexing modes (see `the section called
“bigram\_index” <../../index_configuration_options/bigramindex.md>`__)
require to define a list of frequent keywords. These are <b>not</b> to
be confused with stopwords! Stopwords are completely eliminated when
both indexing and searching. Frequent keywords are only used by bigrams
to determine whether to index a current word pair or not.

``bigram_freq_words`` lets you define a list of such keywords.

Example:
^^^^^^^^

::


    bigram_freq_words = the, a, you, i

