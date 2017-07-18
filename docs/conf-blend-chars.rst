.. raw:: html

   <div class="navheader">

12.2.47. blend\_chars
`Prev <conf-expand-keywords.html>`__ 
12.2. Index configuration options
 `Next <conf-blend-mode.html>`__

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

.. rubric:: 12.2.47. blend\_chars
   :name: blend_chars
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Blended characters list. Optional, default is empty. Introduced in
version 1.10-beta.

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
“hello @twitter” within quotes (a phrase operator) would handle @-sign
as blended, because @-syntax for field operator is not allowed within
phrases. Otherwise, the character would be handled as an operator. So
you might want to escape the keywords.

Starting with version 2.0.1-beta, blended characters can be remapped, so
that multiple different blended characters could be normalized into just
one base form. This is useful when indexing multiple alternative Unicode
codepoints with equivalent glyphs.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    blend_chars = +, &, U+23
    blend_chars = +, &->+ # 2.0.1 and above

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+---------------------------------+------------------------------------+
| `Prev <conf-expand-keywords.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-blend-mode.html>`__   |
+-----------------------------------------+---------------------------------+------------------------------------+
| 12.2.46. expand\_keywords               | `Home <index.html>`__           |  12.2.48. blend\_mode              |
+-----------------------------------------+---------------------------------+------------------------------------+

.. raw:: html

   </div>
