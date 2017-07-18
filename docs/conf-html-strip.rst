.. raw:: html

   <div class="navheader">

12.2.27. html\_strip
`Prev <conf-phrase-boundary-step.html>`__ 
12.2. Index configuration options
 `Next <conf-html-index-attrs.html>`__

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

.. rubric:: 12.2.27. html\_strip
   :name: html_strip
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Whether to strip HTML markup from incoming full-text data. Optional,
default is 0. Known values are 0 (disable stripping) and 1 (enable
stripping).

Both HTML tags and entities and considered markup and get processed.

HTML tags are removed, their contents (i.e., everything between <P> and
</P>) are left intact by default. You can choose to keep and index
attributes of the tags (e.g., HREF attribute in an A tag, or ALT in an
IMG one). Several well-known inline tags are completely removed, all
other tags are treated as block level and replaced with whitespace. For
example, ‘te<B>st</B>’ text will be indexed as a single keyword ‘test’,
however, ‘te<P>st</P>’ will be indexed as two keywords ‘te’ and ‘st’.
Known inline tags are as follows: A, B, I, S, U, BASEFONT, BIG, EM,
FONT, IMG, LABEL, SMALL, SPAN, STRIKE, STRONG, SUB, SUP, TT.

HTML entities get decoded and replaced with corresponding UTF-8
characters. Stripper supports both numeric forms (such as &#239;) and
text forms (such as &oacute; or &nbsp;). All entities as specified by
HTML4 standard are supported.

Stripping should work with properly formed HTML and XHTML, but, just as
most browsers, may produce unexpected results on malformed input (such
as HTML with stray <’s or unclosed >’s).

Only the tags themselves, and also HTML comments, are stripped. To strip
the contents of the tags too (eg. to strip embedded scripts), see
`html\_remove\_elements <conf-html-remove-elements.html>`__ option.
There are no restrictions on tag names; ie. everything that looks like a
valid tag start, or end, or a comment will be stripped.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    html_strip = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+---------------------------------+------------------------------------------+
| `Prev <conf-phrase-boundary-step.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-html-index-attrs.html>`__   |
+----------------------------------------------+---------------------------------+------------------------------------------+
| 12.2.26. phrase\_boundary\_step              | `Home <index.html>`__           |  12.2.28. html\_index\_attrs             |
+----------------------------------------------+---------------------------------+------------------------------------------+

.. raw:: html

   </div>
