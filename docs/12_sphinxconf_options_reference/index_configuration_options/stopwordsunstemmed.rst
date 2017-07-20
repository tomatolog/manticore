stopwords\_unstemmed
~~~~~~~~~~~~~~~~~~~~

Whether to apply stopwords before or after stemming. Optional, default
is 0 (apply stopword filter after stemming).

By default, stopwords are stemmed themselves, and applied to tokens
*after* stemming (or any other morphology processing). In other words,
by default, a token is stopped when stem(token) == stem(stopword). That
can lead to unexpected results when a token gets (erroneously) stemmed
to a stopped root. For example, ‘Andes’ gets stemmed to ‘and’ by our
current stemmer implementation, so when ‘and’ is a stopword, ‘Andes’ is
also stopped.

stopwords\_unstemmed directive fixes that issue. When it's enabled,
stopwords are applied before stemming (and therefore to the original
word forms), and the tokens are stopped when token == stopword.

Example:
^^^^^^^^

::


    stopwords_unstemmed = 1

