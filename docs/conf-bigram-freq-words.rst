.. raw:: html

   <div class="navheader">

12.2.61. bigram\_freq\_words
`Prev <conf-ha-strategy.html>`__ 
12.2. Index configuration options
 `Next <conf-bigram-index.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.2.61. bigram\_freq\_words
   :name: bigram_freq_words
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A list of keywords considered “frequent” when indexing bigrams.
Optional, default is empty. Added in 2.1.1-beta.

Bigram indexing is a feature to accelerate phrase searches. When
indexing, it stores a document list for either all or some of the
adjacent words pairs into the index. Such a list can then be used at
searching time to significantly accelerate phrase or sub-phrase
matching.

Some of the bigram indexing modes (see `Section 12.2.62,
“bigram\_index” <conf-bigram-index.html>`__) require to define a list of
frequent keywords. These are **not** to be confused with stopwords!
Stopwords are completely eliminated when both indexing and searching.
Frequent keywords are only used by bigrams to determine whether to index
a current word pair or not.

``bigram_freq_words`` lets you define a list of such keywords.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    bigram_freq_words = the, a, you, i

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+---------------------------------+--------------------------------------+
| `Prev <conf-ha-strategy.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-bigram-index.html>`__   |
+-------------------------------------+---------------------------------+--------------------------------------+
| 12.2.60. ha\_strategy               | `Home <index.html>`__           |  12.2.62. bigram\_index              |
+-------------------------------------+---------------------------------+--------------------------------------+

.. raw:: html

   </div>
