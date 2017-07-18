Version 2.2.7-release, 20 jan 2015
----------------------------------

Minor features
~~~~~~~~~~~~~~

-  added #2112, string equal comparison support for
   `IF() <../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-if>`__
   function (for JSON and string attributes)

-  added #2153,
   `IN() <../5_searching/expressions,_functions,_and_operators/comparison_functions.md#expr-func-in>`__
   support for mixed and top-level JSON arrays

Bug fixes
~~~~~~~~~

-  fixed #2158, crash at RT index after morphology changed to AOT after
   index was created

-  fixed #2155,
   `stopwords <../index_configuration_options/stopwords.md>`__ got
   missed on disk chunk save at RT index

-  fixed #2151, agents statistics missed in case of huge amount of
   agents

-  fixed #2139, escape all special characters in JSON result set,
   according to RFC 4627

-  fixed #2123, no pid file created in x64 release built with vs2012

-  fixed #2115, ``indexer`` crash on wordforms with multiple destination
   keywords

-  fixed #2050, multi result set doesn't work without ``libmysqlclient``

-  fixed #2003,
   `lemmatize\_XX\_all <../index_configuration_options/morphology.md>`__
   handling of short and exact words

-  fixed #1912, reduce ``indextool`` memory usage during a check of a
   huge index

-  fixed off by one errors in filtering of ``BIGINT`` attributes

-  fixed seamless rotation in
   `prefork <../searchd_program_configuration_options/workers.md>`__
   mode

-  fixed snippets crash with `blend
   chars <../index_configuration_options/blendchars.md>`__ at the
   beginning of a string
