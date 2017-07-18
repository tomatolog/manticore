index\_sp
~~~~~~~~~

Whether to detect and index sentence and paragraph boundaries. Optional,
default is 0 (do not detect and index). Introduced in version
2.0.1-beta.

This directive enables sentence and paragraph boundary indexing. It's
required for the SENTENCE and PARAGRAPH operators to work. Sentence
boundary detection is based on plain text analysis, so you only need to
set ``index_sp = 1`` to enable it. Paragraph detection is however based
on HTML markup, and happens in the `HTML
stripper <../../index_configuration_options/htmlstrip.rst>`__. So to
index paragraph locations you also need to enable the stripper by
specifying ``html_strip = 1``. Both types of boundaries are detected
based on a few built-in rules enumerated just below.

Sentence boundary detection rules are as follows.

-  Question and exclamation signs (? and !) are always a sentence
   boundary.

-  Trailing dot (.) is a sentence boundary, except:

   -  When followed by a letter. That's considered a part of an
      abbreviation (as in “S.T.A.L.K.E.R” or “Goldman Sachs S.p.A.”).

   -  When followed by a comma. That's considered an abbreviation
      followed by a comma (as in “Telecom Italia S.p.A., founded in
      1994”).

   -  When followed by a space and a small letter. That's considered an
      abbreviation within a sentence (as in “News Corp. announced in
      February”).

   -  When preceded by a space and a capital letter, and followed by a
      space. That's considered a middle initial (as in “John D. Doe”).

Paragraph boundaries are inserted at every block-level HTML tag. Namely,
those are (as taken from HTML 4 standard) ADDRESS, BLOCKQUOTE, CAPTION,
CENTER, DD, DIV, DL, DT, H1, H2, H3, H4, H5, LI, MENU, OL, P, PRE,
TABLE, TBODY, TD, TFOOT, TH, THEAD, TR, and UL.

Both sentences and paragraphs increment the keyword position counter by
1.

Example:
^^^^^^^^

::


    index_sp = 1

