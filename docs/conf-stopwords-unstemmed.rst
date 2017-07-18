.. raw:: html

   <div class="navheader">

12.2.65. stopwords\_unstemmed
`Prev <conf-regexp-filter.html>`__ 
12.2. Index configuration options
 `Next <conf-global-idf.html>`__

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

.. rubric:: 12.2.65. stopwords\_unstemmed
   :name: stopwords_unstemmed
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Whether to apply stopwords before or after stemming. Optional, default
is 0 (apply stopword filter after stemming). Added in 2.1.1-beta.

By default, stopwords are stemmed themselves, and applied to tokens
*after* stemming (or any other morphology processing). In other words,
by default, a token is stopped when stem(token) == stem(stopword). That
can lead to unexpected results when a token gets (erroneously) stemmed
to a stopped root. For example, ‘Andes’ gets stemmed to ‘and’ by our
current stemmer implementation, so when ‘and’ is a stopword, ‘Andes’ is
also stopped.

stopwords\_unstemmed directive fixes that issue. When it’s enabled,
stopwords are applied before stemming (and therefore to the original
word forms), and the tokens are stopped when token == stopword.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    stopwords_unstemmed = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------+------------------------------------+
| `Prev <conf-regexp-filter.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-global-idf.html>`__   |
+---------------------------------------+---------------------------------+------------------------------------+
| 12.2.64. regexp\_filter               | `Home <index.html>`__           |  12.2.66. global\_idf              |
+---------------------------------------+---------------------------------+------------------------------------+

.. raw:: html

   </div>
