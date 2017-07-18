Version 2.1.6-release, 24 feb 2014
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1857, crash in arabic stemmer

-  fixed #1875, fixed crash on adding documents with long words in
   dict=keyword index with morphology and infixes enabled

-  fixed #1876, crash on words with large codepoints and infix searches

-  fixed #1880, crash on multiquery with one incorrect query

-  fixed #1882, race of periodic and forced FLUSHing on an RT index

-  fixed #1881, quorum syntax with ‘.’ as blended char

-  fixed evaluating of LCS by an expression ranker

-  fixed #1864, ``indexer`` crash on badly formed JSON, e.g.
   ‘[,1,2,3,4,]’

-  fixed #1853, incomplete `ORDER BY JSON <../select_syntax.rst>`__
   attribute in distributed indexes

-  fixed #1847, broken infix searches in RT indexes

-  fixed #1844, clash of mix cased attribute and field names at CSV
   source

-  fixed #1840, filter by [@uservar](../set\_syntax.rst) in distributes
   indexes

-  fixed #1832,#1833,#1834, some big endianess issues

-  fixed #1830, loss of
   `ondisk\_attrs <../index_configuration_options/ondiskattrs.rst>`__
   after rotation

-  fixed #1762, memory leak in
   `regexp\_filter <../index_configuration_options/regexpfilter.rst>`__

-  fixed #1759, ``indextool`` false positives on persistent MVA checking

-  fixed `GROUP BY <../select_syntax.rst>`__ id

-  fixed crash on sending empty snippet result

-  fixed index corruption in `UPDATE <../update_syntax.rst>`__ queries
   with non-existent attributes
