Version 2.1.8-release, 28 apr 2014
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1937, crash at `SENTENCE <../extended_query_syntax.rst>`__
   operator

-  fixed #1933, quorum operator works incorrectly if it's number is
   exception

-  fixed #1932, fixed daemon index recovery after failed rotation

-  fixed #1923, crash at ``indexer`` with ``dict=keywords``

-  fixed #1918, fixed crash while hitless words are used within fulltext
   operators which require hits

-  fixed #1878, daemon doesn't reset
   `regexp\_filter <../index_configuration_options/regexpfilter.rst>`__
   after rotation with
   `seamless\_rotate=0 <../searchd_program_configuration_options/seamlessrotate.rst>`__

-  fixed #1769, crash after unsuccessful
   `INSERT <../insert_and_replace_syntax.rst>`__ at RT index

-  fixed #1682, field end modifier doesn't work with words containing
   blended chars
