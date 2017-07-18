.. raw:: html

   <div class="navheader">

A.42. Version 0.9.7-rc1, 26 oct 2006
`Prev <rel097rc2.html>`__ 
Appendix A. Sphinx revision history
 `Next <rel096.html>`__

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

.. rubric:: A.42. Version 0.9.7-rc1, 26 oct 2006
   :name: a.42.version-0.9.7-rc1-26-oct-2006
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="itemizedlist">

-  added alpha index merging code

-  added an option to decrease ``max_matches`` per-query

-  added an option to specify IP address for searchd to listen on

-  added support for unlimited amount of configured sources and indexes

-  added support for group-by queries

-  added support for /2 range modifier in charset\_table

-  added support for arbitrary amount of document attributes

-  added logging filter count and index name

-  added ``--with-debug`` option to configure to compile in debug mode

-  added ``-DNDEBUG`` when compiling in default mode

-  improved search time (added doclist size hints, in-memory wordlist
   cache, and used VLB coding everywhere)

-  improved (refactored) SQL driver code (adding new drivers should be
   very easy now)

-  improved exceprts generation

-  fixed issue with empty sources and ranged queries

-  fixed querying purely remote distributed indexes

-  fixed suffix length check in English stemmer in some cases

-  fixed UTF-8 decoder for codes over U+20000 (for CJK)

-  fixed UTF-8 encoder for 3-byte sequences (for CJK)

-  fixed overshort (less than ``min_word_len``) words prepended to next
   field

-  fixed source connection order (indexer does not connect to all
   sources at once now)

-  fixed line numbering in config parser

-  fixed some issues with index rotation

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+---------------------------+-------------------------------------+
| `Prev <rel097rc2.html>`__               | `Up <changelog.html>`__   |  `Next <rel096.html>`__             |
+-----------------------------------------+---------------------------+-------------------------------------+
| A.41. Version 0.9.7-rc2, 15 dec 2006    | `Home <index.html>`__     |  A.43. Version 0.9.6, 24 jul 2006   |
+-----------------------------------------+---------------------------+-------------------------------------+

.. raw:: html

   </div>
