bigram\_index
~~~~~~~~~~~~~

Bigram indexing mode. Optional, default is none. Added in 2.1.1-beta.

Bigram indexing is a feature to accelerate phrase searches. When
indexing, it stores a document list for either all or some of the
adjacent words pairs into the index. Such a list can then be used at
searching time to significantly accelerate phrase or sub-phrase
matching.

``bigram_index`` controls the selection of specific word pairs. The
known modes are:

-  ``all``, index every single word pair. (NB: probably totally not
   worth it even on a moderately sized index, but added anyway for the
   sake of completeness.)

-  ``first_freq``, only index word pairs where the *first* word is in a
   list of frequent words (see `the section called
   “bigram\_freq\_words” <../../index_configuration_options/bigramfreq_words.md>`__).
   For example, with ``bigram_freq_words = the, in, i, a``, indexing
   “alone in the dark” text will result in “in the” and “the dark” pairs
   being stored as bigrams, because they begin with a frequent keyword
   (either “in” or “the” respectively), but “alone in” would <b>not</b>
   be indexed, because “in” is a *second* word in that pair.

-  ``both_freq``, only index word pairs where both words are frequent.
   Continuing with the same example, in this mode indexing “alone in the
   dark” would only store “in the” (the very worst of them all from
   searching perspective) as a bigram, but none of the other word pairs.

For most usecases, ``both_freq`` would be the best mode, but your
mileage may vary.

Example:
^^^^^^^^

::


    bigram_freq_words = both_freq

