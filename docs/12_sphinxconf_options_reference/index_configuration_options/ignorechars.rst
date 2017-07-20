ignore\_chars
~~~~~~~~~~~~~

Ignored characters list. Optional, default is empty.

Useful in the cases when some characters, such as soft hyphenation mark
(U+00AD), should be not just treated as separators but rather fully
ignored. For example, if ‘-’ is simply not in the charset\_table,
“abc-def” text will be indexed as “abc” and “def” keywords. On the
contrary, if ‘-’ is added to ignore\_chars list, the same text will be
indexed as a single “abcdef” keyword.

The syntax is the same as for
`charset\_table <../../index_configuration_options/charsettable.md>`__,
but it's only allowed to declare characters, and not allowed to map
them. Also, the ignored characters must not be present in
charset\_table.

Example:
^^^^^^^^

::


    ignore_chars = U+AD

