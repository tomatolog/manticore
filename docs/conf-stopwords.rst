.. raw:: html

   <div class="navheader">

12.2.11. stopwords
`Prev <conf-min-stemming-len.html>`__ 
12.2. Index configuration options
 `Next <conf-wordforms.html>`__

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

.. rubric:: 12.2.11. stopwords
   :name: stopwords
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Stopword files list (space separated). Optional, default is empty.

Stopwords are the words that will not be indexed. Typically you’d put
most frequent words in the stopwords list because they do not add much
value to search results but consume a lot of resources to process.

You can specify several file names, separated by spaces. All the files
will be loaded. Stopwords file format is simple plain text. The encoding
must be UTF-8. File data will be tokenized with respect to
`charset\_table <conf-charset-table.html>`__ settings, so you can use
the same separators as in the indexed data.

The `stemmers <conf-morphology.html>`__ will normally be applied when
parsing stopwords file. That might however lead to undesired results.
Starting with 2.1.1-beta, you can turn that off with
`stopwords\_unstemmed <conf-stopwords-unstemmed.html>`__.

Starting with version 2.1.1-beta small enough files are stored in the
index header, see `Section 12.2.13,
“embedded\_limit” <conf-embedded-limit.html>`__ for details.

While stopwords are not indexed, they still do affect the keyword
positions. For instance, assume that “the” is a stopword, that document
1 contains the line “in office”, and that document 2 contains “in the
office”. Searching for “in office” as for exact phrase will only return
the first document, as expected, even though “the” in the second one is
stopped. That behavior can be tweaked through the
`stopword\_step <conf-stopword-step.html>`__ directive.

Stopwords files can either be created manually, or semi-automatically.
``indexer`` provides a mode that creates a frequency dictionary of the
index, sorted by the keyword frequency, see ``--buildstops`` and
``--buildfreqs`` switch in `Section 7.1, “\ ``indexer`` command
reference” <ref-indexer.html>`__. Top keywords from that dictionary can
usually be used as stopwords.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    stopwords = /usr/local/sphinx/data/stopwords.txt
    stopwords = stopwords-ru.txt stopwords-en.txt

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------------+-----------------------------------+
| `Prev <conf-min-stemming-len.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-wordforms.html>`__   |
+------------------------------------------+---------------------------------+-----------------------------------+
| 12.2.10. min\_stemming\_len              | `Home <index.html>`__           |  12.2.12. wordforms               |
+------------------------------------------+---------------------------------+-----------------------------------+

.. raw:: html

   </div>
