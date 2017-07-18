Version 2.0.6-release, 22 oct 2012
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1322, J connector seems to be broken in rel20 , but works in
   trunk

-  fixed #1321, ‘set names utf8’ passes, but ‘set names utf-8’ doesn't
   because of syntax error ‘-’

-  fixed #1318, unhandled float comparison operators at filter

-  fixed #1317, FD leaks on thread seamless rotation

-  fixed #1313, crash on stopping daemon with incorrect RT index config

-  fixed #1306, ‘jolly roger ;)’, and ‘(((((((((9 brackets)’ crashes
   ``searchd``

-  fixed #1304, OS X debug compilation

-  fixed #1302, daemon random crashes on OS X

-  fixed #1301, ``indexer`` fails to send rotate signal

-  fixed #1300, lost index settings on attach

-  fixed #1299, daemon failed to rotate
   `ATTACH <../attach_index_syntax.html>`__\ ed plain index

-  fixed #1289, `SENTENCE <../extended_query_syntax.html>`__ or
   `PARAGRAPH <../extended_query_syntax.html>`__ searching leak memory

-  fixes #1285, crash on running ``searchd`` with ``syslog`` and
   ``watchdog``

-  fixed #1279, linking against explicitly disabled iconv. Also added
   ``--with-libexpat`` to config options, which sometimes required on
   systems without XML support

-  fixed #1278, broken
   `unixODBC <../data_source_configuration_options/odbcdsn.html>`__
   detection in configure script.

-  fixed #1277, broken build on some toolchains (like uClibc) where not
   defined ``LLONG_MIN``, added ``ULLONG_MAX``

-  fixed #1274, large ``spa`` ( >4GB ) file hasn't loaded

-  fixed #1269, crash at RT index with
   `MVA <../mva_multi-valued_attributes.html>`__ from disk chunk
   previously updated

-  fixed #1268, unuseful warning removed

-  fixed #1264, string and MVA attributes aliasing works again

-  fixed #1254, its now possible to add indexes using
   `–rotate <../indexer_command_reference.html>`__

-  fixed #1249, `SphinxQL <../8_sphinxql_reference/README.html>`__
   unusable with PHP >= 5.4.5

-  fixed #1246, attributes of 100 character length not being saved

-  fixed #1234, case sensitive `GROUP BY <../select_syntax.html>`__
   attribute

-  fixed #1216, typos,
   `mem\_limit <../indexer_program_configuration_options/memlimit.html>`__
   default size and `RT
   documentation <../4_real-time_indexes/README.html>`__

-  fixed #1148, RT documentation updated

-  fixed #1140, mem\_limit default value

-  fixed #1138, updated documentation on
   `sql\_attr\_string <../data_source_configuration_options/sqlattr_string.html>`__

-  fixed #1129, snippets vs empty files and empty filenames

-  fixed #1123, configure compatibility fix

-  fixed #1122, 64bit
   `sql\_range\_step <../data_source_configuration_options/sqlrange_step.html>`__

-  fixed #1082, crashes and deadlocks on OS X with ``workers=threads``
   and field leak of read-write lock

-  fixed #1081, select only count distinct attr1 but group by attr2

-  fixed #1064, mistake while working with timestamp functions

-  fixed #1043, inaccurate distinct count in case many indexes or
   distributed index

-  fixed #1042, arithmetic expressions overflow

-  fixed #1007, Russian stemming on big endian systems

-  fixed #986, asserting in
   `SetRankingMode <../full-text_search_query_settings/setrankingmode.html>`__
   (PHP API)

-  fixed #975, incorrect ranking in some rare cases

-  fixed #967, Python API type checking error

-  fixed #934, API vs fullscan vs non-empty query

-  fixed #899, error if using
   `SetFilterRange <../result_set_filtering_settings/setfilterrange.html>`__
   as HAVING from SQL

-  fixed #867, ``indexer`` accepts index names starting with digit or \_

-  fixed #699, signed vs unsigned 64-bit DocIDs in SphinxQL

-  fixed #668, now ignoring single @ character (incorrect field
   operator)

-  fixed #611, @! operator vs non-existent field, updated documentation

-  fixed #412, multiple ``--filter`` arguments work as they should in
   search utility

-  fixed #108, support for system libstemmer library. The sources of
   libstemmer placed into ``libstemmer_c`` is preferred, but the system
   lib will be tried if no sources found

-  fixed `ORDER BY <../select_syntax.html>`__ output at query log with
   SphinxQL mode

-  fixed documentation entry about
   `sql\_joined\_field <../data_source_configuration_options/sqljoined_field.html>`__

-  fixed sample config file

-  fixed x64 configurations for libstemmer
