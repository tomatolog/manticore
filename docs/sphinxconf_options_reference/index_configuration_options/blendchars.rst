blend\_chars
~~~~~~~~~~~~

Blended characters list. Optional, default is empty.

Blended characters are indexed both as separators and valid characters.
For instance, assume that & is configured as blended and AT&T occurs in
an indexed document. Three different keywords will get indexed, namely
“at&t”, treating blended characters as valid, plus “at” and “t”,
treating them as separators.

Positions for tokens obtained by replacing blended characters with
whitespace are assigned as usual, so regular keywords will be indexed
just as if there was no ``blend_chars`` specified at all. An additional
token that mixes blended and non-blended characters will be put at the
starting position. For instance, if the field contents are “AT&T
company” occurs in the very beginning of the text field, “at” will be
given position 1, “t” position 2, “company” position 3, and “AT&T” will
also be given position 1 (“blending” with the opening regular keyword).
Thus, querying for either AT&T or just AT will match that document, and
querying for “AT T” as a phrase also match it. Last but not least,
phrase query for “AT&T company” will *also* match it, despite the
position

Blended characters can overlap with special characters used in query
syntax (think of T-Mobile or @twitter). Where possible, query parser
will automatically handle blended character as blended. For instance,
“hello @twitter&quot; within quotes (a phrase operator) would handle
@-sign as blended, because @-syntax for field operator is not allowed
within phrases. Otherwise, the character would be handled as an
operator. So you might want to escape the keywords.

Blended characters can be remapped, so that multiple different blended
characters could be normalized into just one base form. This is useful
when indexing multiple alternative Unicode codepoints with equivalent
glyphs.

Example:
^^^^^^^^

::


    blend_chars = +, &, U+23
    blend_chars = +, &->+

