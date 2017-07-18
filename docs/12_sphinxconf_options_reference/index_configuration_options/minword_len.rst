min\_word\_len
~~~~~~~~~~~~~~

Minimum indexed word length. Optional, default is 1 (index everything).

Only those words that are not shorter than this minimum will be indexed.
For instance, if min\_word\_len is 4, then ‘the’ won't be indexed, but
‘they’ will be.

Example:
^^^^^^^^

::


    min_word_len = 4

