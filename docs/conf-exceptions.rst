.. raw:: html

   <div class="navheader">

12.2.14. exceptions
`Prev <conf-embedded-limit.html>`__ 
12.2. Index configuration options
 `Next <conf-min-word-len.html>`__

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

.. rubric:: 12.2.14. exceptions
   :name: exceptions
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Tokenizing exceptions file. Optional, default is empty.

Exceptions allow to map one or more tokens (including tokens with
characters that would normally be excluded) to a single keyword. They
are similar to `wordforms <conf-wordforms.html>`__ in that they also
perform mapping, but have a number of important differences.

Starting with version 2.1.1-beta small enough files are stored in the
index header, see `Section 12.2.13,
“embedded\_limit” <conf-embedded-limit.html>`__ for details.

Short summary of the differences is as follows:

.. raw:: html

   <div class="itemizedlist">

-  exceptions are case sensitive, wordforms are not;

-  exceptions can use special characters that are **not** in
   charset\_table, wordforms fully obey charset\_table;

-  exceptions can underperform on huge dictionaries, wordforms handle
   millions of entries well.

.. raw:: html

   </div>

The expected file format is also plain text, with one line per
exception, and the line format is as follows:

.. code:: programlisting

    map-from-tokens => map-to-token

Example file:

.. code:: programlisting

    at & t => at&t
    AT&T => AT&T
    Standarten   Fuehrer => standartenfuhrer
    Standarten Fuhrer => standartenfuhrer
    MS Windows => ms windows
    Microsoft Windows => ms windows
    C++ => cplusplus
    c++ => cplusplus
    C plus plus => cplusplus

All tokens here are case sensitive: they will **not** be processed by
`charset\_table <conf-charset-table.html>`__ rules. Thus, with the
example exceptions file above, “at&t” text will be tokenized as two
keywords “at” and “t”, because of lowercase letters. On the other hand,
“AT&T” will match exactly and produce single “AT&T” keyword.

Note that this map-to keyword is a) always interpreted as a *single*
word, and b) is both case and space sensitive! In our sample, “ms
windows” query will *not* match the document with “MS Windows” text. The
query will be interpreted as a query for two keywords, “ms” and
“windows”. And what “MS Windows” gets mapped to is a *single* keyword
“ms windows”, with a space in the middle. On the other hand,
“standartenfuhrer” will retrieve documents with “Standarten Fuhrer” or
“Standarten Fuehrer” contents (capitalized exactly like this), or any
capitalization variant of the keyword itself, eg. “staNdarTenfUhreR”.
(It won’t catch “standarten fuhrer”, however: this text does not match
any of the listed exceptions because of case sensitivity, and gets
indexed as two separate keywords.)

Whitespace in the map-from tokens list matters, but its amount does not.
Any amount of the whitespace in the map-form list will match any other
amount of whitespace in the indexed document or query. For instance,
“AT & T” map-from token will match “AT    &  T” text, whatever the
amount of space in both map-from part and the indexed text. Such text
will therefore be indexed as a special “AT&T” keyword, thanks to the
very first entry from the sample.

Exceptions also allow to capture special characters (that are exceptions
from general `charset\_table <conf-charset-table.html>`__ rules; hence
the name). Assume that you generally do not want to treat ‘+’ as a valid
character, but still want to be able search for some exceptions from
this rule such as ‘C++’. The sample above will do just that, totally
independent of what characters are in the table and what are not.

Exceptions are applied to raw incoming document and query data during
indexing and searching respectively. Therefore, to pick up changes in
the file it’s required to reindex and restart ``searchd``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    exceptions = /usr/local/sphinx/data/exceptions.txt

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+---------------------------------+--------------------------------------+
| `Prev <conf-embedded-limit.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-min-word-len.html>`__   |
+----------------------------------------+---------------------------------+--------------------------------------+
| 12.2.13. embedded\_limit               | `Home <index.html>`__           |  12.2.15. min\_word\_len             |
+----------------------------------------+---------------------------------+--------------------------------------+

.. raw:: html

   </div>
