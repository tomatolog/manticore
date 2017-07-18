exceptions
~~~~~~~~~~

Tokenizing exceptions file. Optional, default is empty.

Exceptions allow to map one or more tokens (including tokens with
characters that would normally be excluded) to a single keyword. They
are similar to
`wordforms <../../index_configuration_options/wordforms.html>`__ in that
they also perform mapping, but have a number of important differences.

Starting with version 2.1.1-beta small enough files are stored in the
index header, see `the section called
“embedded\_limit” <../../index_configuration_options/embeddedlimit.html>`__
for details.

Short summary of the differences is as follows:

-  exceptions are case sensitive, wordforms are not;

-  exceptions can use special characters that are <b>not</b> in
   charset\_table, wordforms fully obey charset\_table;

-  exceptions can underperform on huge dictionaries, wordforms handle
   millions of entries well.

The expected file format is also plain text, with one line per
exception, and the line format is as follows:

::


    map-from-tokens => map-to-token

Example file:

::


    at & t => at&t
    AT&T => AT&T
    Standarten   Fuehrer => standartenfuhrer
    Standarten Fuhrer => standartenfuhrer
    MS Windows => ms windows
    Microsoft Windows => ms windows
    C++ => cplusplus
    c++ => cplusplus
    C plus plus => cplusplus

All tokens here are case sensitive: they will <b>not</b> be processed by
`charset\_table <../../index_configuration_options/charsettable.html>`__
rules. Thus, with the example exceptions file above, “at&t” text will be
tokenized as two keywords “at” and “t”, because of lowercase letters. On
the other hand, “AT&T” will match exactly and produce single “AT&T”
keyword.

Note that this map-to keyword is a) always interpreted as a *single*
word, and b) is both case and space sensitive! In our sample, “ms
windows” query will *not* match the document with “MS Windows” text. The
query will be interpreted as a query for two keywords, “ms” and
“windows”. And what “MS Windows” gets mapped to is a *single* keyword
“ms windows”, with a space in the middle. On the other hand,
“standartenfuhrer” will retrieve documents with “Standarten Fuhrer” or
“Standarten Fuehrer” contents (capitalized exactly like this), or any
capitalization variant of the keyword itself, eg. “staNdarTenfUhreR”.
(It won't catch “standarten fuhrer”, however: this text does not match
any of the listed exceptions because of case sensitivity, and gets
indexed as two separate keywords.)

Whitespace in the map-from tokens list matters, but its amount does not.
Any amount of the whitespace in the map-form list will match any other
amount of whitespace in the indexed document or query. For instance, “AT
& T” map-from token will match “AT & T” text, whatever the amount of
space in both map-from part and the indexed text. Such text will
therefore be indexed as a special “AT&T” keyword, thanks to the very
f.html entry from the sample.

Exceptions also allow to capture special characters (that are exceptions
from general
`charset\_table <../../index_configuration_options/charsettable.html>`__
rules; hence the name). Assume that you generally do not want to treat
‘+’ as a valid character, but still want to be able search for some
exceptions from this rule such as ‘C++’. The sample above will do just
that, totally independent of what characters are in the table and what
are not.

Exceptions are applied to raw incoming document and query data during
indexing and searching respectively. Therefore, to pick up changes in
the file it's required to reindex and restart ``searchd``.

Example:
^^^^^^^^

::


    exceptions = /usr/local/sphinx/data/exceptions.txt

