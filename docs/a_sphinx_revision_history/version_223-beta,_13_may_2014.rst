Version 2.2.3-beta, 13 may 2014
-------------------------------

New features
~~~~~~~~~~~~

-  added `#1920 <http://sphinxsearch.com/bugs/view.php?id=1920>`__,
   `charset\_table <../index_configuration_options/charsettable.md>`__
   aliases

-  added `#1887 <http://sphinxsearch.com/bugs/view.php?id=1887>`__,
   filtering over string attributes

-  added `#1860 <http://sphinxsearch.com/bugs/view.php?id=1860>`__,
   `USERVARs <../set_syntax.md>`__ for distributed indexes

-  added `#1689 <http://sphinxsearch.com/bugs/view.php?id=1689>`__,
   `GROUP BY JSON <../select_syntax.md>`__ attributes

-  added `FACET <../select_syntax.md>`__ keyword

-  added Go MySQL connector support

-  added `IDF boost <../extended_query_syntax.md>`__ keyword modifier

-  added `MAYBE <../extended_query_syntax.md>`__ fulltext operator

Optimizations and removals
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  improved speed of concurrent insertion in RT indexes

-  removed
   `max\_matches <../sphinx_deprecations_and_changes_in_default_configu.md>`__
   config key

Bug fixes
~~~~~~~~~

-  fixed #1946,
   `IN() <../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-in>`__
   function support for string attributes

-  fixed #1942, crash in `SHOW THREADS <../show_threads_syntax.md>`__
   command

-  fixed #1922, crash on snippet generation for queries with duplicated
   words

-  fixed #1919,
   `TSV <../tsvpipecsvpipe_tabcomma_separated_values_data_sour.md>`__
   bitcount attributes indexation issue

-  fixed #1916, `COUNT(\*) <../select_syntax.md>`__ with empty result
   set

-  fixed #1910, JSON parsing issue

-  fixed #1906, `ZONE <../extended_query_syntax.md>`__ constraints for
   expanded terms

-  fixed #1904, race condition in RT indexes on saving disk chunk

-  fixed #1899, crash on `CALL KEYWORDS <../call_keywords_syntax.md>`__

-  fixed #1893, ``searchd`` crashes on expressions like 'a<<(\*!b)'

-  fixed #1884, crash with `SNIPPET() <../select_syntax.md>`__ function
   over distributed index

-  fixed #1883, crash at expanded keyword with hitless index

-  fixed #1870, crash on `ORDER BY JSON <../select_syntax.md>`__
   attributes

-  fixed template index removing on rotation
