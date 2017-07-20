Version 2.1.5-release, 22 jan 2014
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1848, infixes and morphology clash

-  fixed #1823, ``indextool`` fails to handle indexes with lemmatizer
   morphology

-  fixed #1799, crash in queries to distributed indexes with `GROUP
   BY <../select_syntax.md>`__ on multiple values

-  fixed #1718, ``expand_keywords`` option lost in disk chunks of RT
   indexes

-  fixed documentation on
   `rt\_flush\_period <../searchd_program_configuration_options/rtflush_period.md>`__

-  fixed network protocol issue which results in timeouts of
   ``libmysqlclient`` for big Manticore responses
