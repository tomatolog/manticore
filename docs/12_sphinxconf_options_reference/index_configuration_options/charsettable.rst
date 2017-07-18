charset\_table
~~~~~~~~~~~~~~

Accepted characters table, with case folding rules. Optional, default
value are latin and cyrillic characters.

charset\_table is the main workhorse of Sphinx tokenizing process, ie.
the process of extracting keywords from document text or query text. It
controls what characters are accepted as valid and what are not, and how
the accepted characters should be transformed (eg. should the case be
removed or not).

You can think of charset\_table as of a big table that has a mapping for
each and every of 100K+ characters in Unicode. By default, every
character maps to 0, which means that it does not occur within keywords
and should be treated as a separator. Once mentioned in the table,
character is mapped to some other character (most frequently, either to
itself or to a lowercase letter), and is treated as a valid keyword
part.

The expected value format is a commas-separated list of mappings. Two
simplest mappings simply declare a character as valid, and map a single
character to another single character, respectively. But specifying the
whole table in such form would result in bloated and barely manageable
specifications. So there are several syntax shortcuts that let you map
ranges of characters at once. The complete list is as follows:

-  A->a
-  Single char mapping, declares source char ‘A’ as allowed to occur
   within keywords and maps it to destination char ‘a’ (but does *not*
   declare ‘a’ as allowed).

-  A..Z->a..z
-  Range mapping, declares all chars in source range as allowed and maps
   them to the destination range. Does *not* declare destination range
   as allowed. Also checks ranges' lengths (the lengths must be equal).

-  a
-  Stray char mapping, declares a character as allowed and maps it to
   itself. Equivalent to a->a single char mapping.

-  a..z
-  Stray range mapping, declares all characters in range as allowed and
   maps them to themselves. Equivalent to a..z->a..z range mapping.

-  A..Z/2
-  Checkerboard range map. Maps every pair of chars to the second char.
   More formally, declares odd characters in range as allowed and maps
   them to the even ones; also declares even characters as allowed and
   maps them to themselves. For instance, A..Z/2 is equivalent to A->B,
   B->B, C->D, D->D, …, Y->Z, Z->Z. This mapping shortcut is helpful for
   a number of Unicode blocks where uppercase and lowercase letters go
   in such interleaved order instead of contiguous chunks.

Control characters with codes from 0 to 31 are always treated as
separators. Characters with codes 32 to 127, ie. 7-bit ASCII characters,
can be used in the mappings as is. To avoid configuration file encoding
issues, 8-bit ASCII characters and Unicode characters must be specified
in U+xxx form, where ‘xxx’ is hexadecimal codepoint number. This form
can also be used for 7-bit ASCII characters to encode special ones: eg.
use U+20 to encode space, U+2E to encode dot, U+2C to encode comma.

Starting with 2.2.3-beta, aliases “english” and “russian” are allowed at
control character mapping.

Example:
^^^^^^^^

::


    # default are English and Russian letters
    charset_table = 0..9, A..Z->a..z, _, a..z, \
        U+410..U+42F->U+430..U+44F, U+430..U+44F, U+401->U+451, U+451

    # english charset defined with alias
    charset_table = 0..9, english, _

