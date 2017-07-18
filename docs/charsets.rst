.. raw:: html

   <div class="navheader">

3.7. Charsets, case folding, translation tables, and replacement rules
`Prev <data-restrictions.html>`__ 
Chapter 3. Indexing
 `Next <sql.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 3.7. Charsets, case folding, translation tables, and
   replacement rules
   :name: charsets-case-folding-translation-tables-and-replacement-rules
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

When indexing some index, Sphinx fetches documents from the specified
sources, splits the text into words, and does case folding so that
“Abc”, “ABC” and “abc” would be treated as the same word (or, to be
pedantic, *term*).

To do that properly, Sphinx needs to know

.. raw:: html

   <div class="itemizedlist">

-  what encoding is the source text in (and this encoding should always
   be UTF-8);

-  what characters are letters and what are not;

-  what letters should be folded to what letters.

.. raw:: html

   </div>

This should be configured on a per-index basis using ``charset_table``
option. ``charset_table`` specifies the table that maps letter
characters to their case folded versions. The characters that are not in
the table are considered to be non-letters and will be treated as word
separators when indexing or searching through this index.

Default tables currently include English and Russian characters. Please
do submit your tables for other languages!

As of version 2.1.1-beta, you can also specify text pattern replacement
rules. For example, given the rules

.. code:: programlisting

    regexp_filter = \b(\d+)\" => \1 inch
    regexp_filter = (BLUE|RED) => COLOR

the text ‘RED TUBE 5" LONG’ would be indexed as ‘COLOR TUBE 5 INCH
LONG’, and ’PLANK 2" x 4“‘ as ’PLANK 2 INCH x 4 INCH’. Rules are applied
in the given order. Text in queries is also replaced; a search for ”BLUE
TUBE" would actually become a search for “COLOR TUBE”. Note that Sphinx
must be built with the –with-re2 option to use this feature.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+--------------------------+----------------------------------------------+
| `Prev <data-restrictions.html>`__       | `Up <indexing.html>`__   |  `Next <sql.html>`__                         |
+-----------------------------------------+--------------------------+----------------------------------------------+
| 3.6. Restrictions on the source data    | `Home <index.html>`__    |  3.8. SQL data sources (MySQL, PostgreSQL)   |
+-----------------------------------------+--------------------------+----------------------------------------------+

.. raw:: html

   </div>
