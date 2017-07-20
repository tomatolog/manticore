Version 2.0.8-release, 26 apr 2013
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1515, log strings over 2KB were clipped when
   `query\_log\_format=plain <../searchd_program_configuration_options/querylog_format.md>`__

-  fixed #1514, RT index disk chunk lose attribute update on daemon
   restart

-  fixed #1512, crash while formatting log messages

-  fixed #1511, crash on indexing PostgreSQL data source with
   `MVA <../mva_multi-valued_attributes.md>`__ attributes

-  fixed #1509,
   `blend\_chars <../index_configuration_options/blendchars.md>`__ vs
   incomplete multi-form and overshort

-  fixed #1504, RT binlog replay vs descending tid on update

-  fixed #1499, ``sql_field_str2wordcount`` actually is int, not string

-  fixed #1498, now working with exceptions starting with number too

-  fixed #1496, multiple destination keywords in wordform

-  fixed #1494, lost ‘mod’, ‘%’ operations in select list. Also
   corrected few typers in the doc.

-  fixed #1490,
   `expand\_keywords <../index_configuration_options/expandkeywords.md>`__
   vs prefix

-  fixed #1487, ``id`` in expression fixed

-  fixed #1483, snippets limits fix

-  fixed #1481, shebang config changes check on rotation

-  fixed #1479, port handling in `PHP Manticore
   API <../9_api_reference/README.md>`__

-  fixed #1474, daemon crash at ManticoreQL packet overflows
   `max\_packet\_size <../searchd_program_configuration_options/maxpacket_size.md>`__

-  fixed #1472, crash on loading index to ``indextool`` for check

-  fixed #1465,
   `expansion\_limit <../searchd_program_configuration_options/expansionlimit.md>`__
   got lost in index rotation

-  fixed #1427, #1506, utf8 3 and 4-bytes codepoints

-  fixed #1405, between with mixed int float values
