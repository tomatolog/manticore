wordforms
~~~~~~~~~

Word forms dictionary. Optional, default is empty.

Word forms are applied after tokenizing the incoming text by
`charset\_table <../../index_configuration_options/charsettable.md>`__
rules. They essentially let you replace one word with another. Normally,
that would be used to bring different word forms to a single normal form
(eg. to normalize all the variants such as “walks”, “walked”, “walking”
to the normal form “walk”). It can also be used to implement stemming
exceptions, because stemming is not applied to words found in the forms
list.

Small enough files are stored in the index header, see `the section
called
“embedded\_limit” <../../index_configuration_options/embeddedlimit.md>`__
for details.

Dictionaries are used to normalize incoming words both during indexing
and searching. Therefore, to pick up changes in wordforms file it's
required to rotate index.

Word forms support in Manticore is designed to support big dictionaries
well. They moderately affect indexing speed: for instance, a dictionary
with 1 million entries slows down indexing about 1.5 times. Searching
speed is not affected at all. Additional RAM impact is roughly equal to
the dictionary file size, and dictionaries are shared across indexes:
ie. if the very same 50 MB wordforms file is specified for 10 different
indexes, additional ``searchd`` RAM usage will be about 50 MB.

Dictionary file should be in a simple plain text format. Each line
should contain source and destination word forms, in UTF-8 encoding,
separated by “greater” sign. Rules from the
`charset\_table <../../index_configuration_options/charsettable.md>`__
will be applied when the file is loaded. So basically it's as case
sensitive as your other full-text indexed data, ie. typically case
insensitive. Here's the file contents sample:

::


    walks > walk
    walked > walk
    walking > walk

There is a bundled ``spelldump`` utility that helps you create a
dictionary file in the format Manticore can read from source ``.dict`` and
``.aff`` dictionary files in ``ispell`` or ``MySpell`` format (as
bundled with OpenOffice).

You can map several source words to a single destination word. Because
the work happens on tokens, not the source text, differences in
whitespace and markup are ignored.

You can use “=>” instead of “>”. Comments (starting with “#” are also
allowed. Finally, if a line starts with a tilde (“~”) the wordform will
be applied after morphology, instead of before.

::


    core 2 duo > c2d
    e6600 > c2d
    core 2duo => c2d # Some people write '2duo' together...

You can specify multiple destination tokens:

::


    s02e02 > season 2 episode 2
    s3 e3 > season 3 episode 3

Example:
^^^^^^^^

::


    wordforms = /usr/local/sphinx/data/wordforms.txt
    wordforms = /usr/local/sphinx/data/alternateforms.txt
    wordforms = /usr/local/sphinx/private/dict*.txt

You can specify several files and not only just one. Masks can be used
as a pattern, and all matching files will be processed in simple
ascending order. (If multi-byte codepages are used, and file names can
include foreign characters, the resulting order may not be exactly
alphabetic.) If a same wordform definition is found in several files,
the latter one is used, and it overrides previous definitions.
