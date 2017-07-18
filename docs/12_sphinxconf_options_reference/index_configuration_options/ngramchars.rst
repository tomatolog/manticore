ngram\_chars
~~~~~~~~~~~~

N-gram characters list. Optional, default is empty.

To be used in conjunction with in
`ngram\_len <../../index_configuration_options/ngramlen.rst>`__, this
list defines characters, sequences of which are subject to N-gram
extraction. Words comprised of other characters will not be affected by
N-gram indexing feature. The value format is identical to
`charset\_table <../../index_configuration_options/charsettable.rst>`__.

Example:
^^^^^^^^

::


    ngram_chars = U+3000..U+2FA1F

