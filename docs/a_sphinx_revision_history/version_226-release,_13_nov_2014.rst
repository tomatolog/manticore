Version 2.2.6-release, 13 nov 2014
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #2104,
   `ALL() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.html#expr-func-all>`__/ANY()/INDEXOF()
   support for distributed indexes

-  fixed #2102, show agent status misses warnings from agents

-  fixed #2100, crash of ``indexer`` while loading stopwords with
   tokenizer plugin

-  fixed #2098, arbitrary JSON subkeys and IS NULL for distributed
   indexes

-  fixed #2097, escaping of field-start modifier

-  fixed possibly memory leak in plugin creation function

-  indexation of duplicate documents
