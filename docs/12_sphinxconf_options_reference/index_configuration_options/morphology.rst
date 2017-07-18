morphology
~~~~~~~~~~

A list of morphology preprocessors (stemmers or lemmatizers) to apply.
Optional, default is empty (do not apply any preprocessor).

Morphology preprocessors can be applied to the words being indexed to
replace different forms of the same word with the base, normalized form.
For instance, English stemmer will normalize both “dogs” and “dog” to
“dog”, making search results for both searches the same.

There are 3 different morphology preprocessors that Sphinx implements:
lemmatizers, stemmers, and phonetic algorithms.

-  Lemmatizer reduces a keyword form to a so-called lemma, a proper
   normal form, or in other words, a valid natural language root word.
   For example, “running” could be reduced to “run”, the infinitive verb
   form, and “octopi” would be reduced to “octopus”, the singular noun
   form. Note that sometimes a word form can have multiple corresponding
   root words. For instance, by looking at “dove” it is not possible to
   tell whether this is a past tense of “dive” the verb as in “He dove
   into a pool.”, or “dove” the noun as in “White dove flew over the
   cuckoo's nest.” In this case lemmatizer can generate all the possible
   root forms.

-  Stemmer reduces a keyword form to a so-called stem by removing and/or
   replacing certain well-known suffixes. The resulting stem is however
   <b>not</b>guaranteed to be a valid word on itself. For instance, with
   a Porter English stemmers “running” would still reduce to “run”,
   which is fine, but “business” would reduce to “busi”, which is not a
   word, and “octopi” would not reduce at all. Stemmers are essentially
   (much) simpler but still pretty good replacements of full-blown
   lemmatizers.

-  Phonetic algorithms replace the words with specially crafted phonetic
   codes that are equal even when the words original are different, but
   phonetically close.

The morphology processors that come with our own built-in Sphinx
implementations are:

-  English, Russian, and German lemmatizers;

-  English, Russian, Arabic, and Czech stemmers;

-  SoundEx and MetaPhone phonetic algorithms.

You can also link with <b>libstemmer</b> library for even more stemmers
(see details below). With libstemmer, Sphinx also supports morphological
processing for more than 15 other languages. Binary packages should come
prebuilt with libstemmer support, too.

Lemmatizer support was added in version 2.1.1-beta, starting with a
Russian lemmatizer. English and German lemmatizers were then added in
version 2.2.1-beta.

Lemmatizers require a dictionary that needs to be additionally
downloaded from the Sphinx website. That dictionary needs to be
installed in a directory specified by
`lemmatizer\_base <../../common_section_configuration_options/lemmatizerbase.html>`__
directive. Also, there is a
`lemmatizer\_cache <../../indexer_program_configuration_options/lemmatizercache.html>`__
directive that lets you speed up lemmatizing (and therefore indexing) by
spending more RAM for, basically, an uncompressed cache of a dictionary.

Chinese segmentation using Rosette Linguistics Platform was added in
2.2.1-beta. It is a much more precise but slower way (compared to
n-grams) to segment Chinese documents.
``[charset_table](../../index_configuration_options/charsettable.html)``
must contain all Chinese characters except Chinese punctuation marks
because incoming documents are f.html processed by sphinx tokenizer and
then the result is processed by RLP. Sphinx performs per-token language
detection on the incoming documents. If token language is identified as
Chinese, it will only be processed the RLP, even if multiple morphology
processors are specified. Otherwise, it will be processed by all the
morphology processors specified in the “morphology” option. Rosette
Linguistics Platform must be installed and configured and sphinx must be
built with a –with-rlp switch. See also
``[rlp_root](../../common_section_configuration_options/rlproot.html)``,
``[rlp_environment](../../common_section_configuration_options/rlpenvironment.html)``
and ``[rlp_context](../../index_configuration_options/rlpcontext.html)``
options. A batched version of RLP segmentation is also available
(``rlp_chinese_batched``). It provides the same functionality as the
basic ``rlp_chinese`` segmentation, but enables batching documents
before processing them by the RLP. Processing several documents at once
can result in a substantial indexing speedup if the documents are small
(for example, less than 1k). See also
``[rlp_max_batch_size](../../common_section_configuration_options/rlpmax_batch_size.html)``
and
``[rlp_max_batch_docs](../../common_section_configuration_options/rlpmax_batch_docs.html)``
options.

Additional stemmers provided by
`Snowball <http://snowball.tartarus.org/>`__ project
`libstemmer <http://snowball.tartarus.org/dist/libstemmer_c.tgz>`__
library can be enabled at compile time using ``--with-libstemmer``
``configure`` option. Built-in English and Russian stemmers should be
faster than their libstemmer counterparts, but can produce slightly
different results, because they are based on an older version.

Soundex implementation matches that of MySQL. Metaphone implementation
is based on Double Metaphone algorithm and indexes the primary code.

Built-in values that are available for use in ``morphology`` option are
as follows:

-  none - do not perform any morphology processing;

-  lemmatize\_ru - apply Russian lemmatizer and pick a single root form
   (added in 2.1.1-beta);

-  lemmatize\_en - apply English lemmatizer and pick a single root form
   (added in 2.2.1-beta);

-  lemmatize\_de - apply German lemmatizer and pick a single root form
   (added in 2.2.1-beta);

-  lemmatize\_ru\_all - apply Russian lemmatizer and index all possible
   root forms (added in 2.1.1-beta);

-  lemmatize\_en\_all - apply English lemmatizer and index all possible
   root forms (added in 2.2.1-beta);

-  lemmatize\_de\_all - apply German lemmatizer and index all possible
   root forms (added in 2.2.1-beta);

-  stem\_en - apply Porter's English stemmer;

-  stem\_ru - apply Porter's Russian stemmer;

-  stem\_enru - apply Porter's English and Russian stemmers;

-  stem\_cz - apply Czech stemmer;

-  stem\_ar - apply Arabic stemmer (added in 2.1.1-beta);

-  soundex - replace keywords with their SOUNDEX code;

-  metaphone - replace keywords with their METAPHONE code.

-  rlp\_chinese - apply Chinese text segmentation using Rosette
   Linguistics Platform

-  rlp\_chinese\_batched - apply Chinese text segmentation using Rosette
   Linguistics Platform with document batching

Additional values provided by libstemmer are in ‘libstemmer\_XXX’
format, where XXX is libstemmer algorithm codename (refer to
``libstemmer_c/libstemmer/modules.txt`` for a complete list).

Several stemmers can be specified (comma-separated). They will be
applied to incoming words in the order they are listed, and the
processing will stop once one of the stemmers actually modifies the
word. Also when
`wordforms <../../index_configuration_options/wordforms.html>`__ feature
is enabled the word will be looked up in word forms dictionary f.html,
and if there is a matching entry in the dictionary, stemmers will not be
applied at all. Or in other words,
`wordforms <../../index_configuration_options/wordforms.html>`__ can be
used to implement stemming exceptions.

Example:
^^^^^^^^

::


    morphology = stem_en, libstemmer_sv

