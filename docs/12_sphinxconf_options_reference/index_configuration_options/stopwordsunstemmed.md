### stopwords_unstemmed {#stopwords-unstemmed}

Whether to apply stopwords before or after stemming. Optional, default is 0 (apply stopword filter after stemming). Added in 2.1.1-beta.

By default, stopwords are stemmed themselves, and applied to tokens _after_ stemming (or any other morphology processing). In other words, by default, a token is stopped when stem(token) == stem(stopword). That can lead to unexpected results when a token gets (erroneously) stemmed to a stopped root. For example, &#039;Andes&#039; gets stemmed to &#039;and&#039; by our current stemmer implementation, so when &#039;and&#039; is a stopword, &#039;Andes&#039; is also stopped.

stopwords_unstemmed directive fixes that issue. When it&#039;s enabled, stopwords are applied before stemming (and therefore to the original word forms), and the tokens are stopped when token == stopword.

#### Example: {#example}

```

stopwords_unstemmed = 1

```