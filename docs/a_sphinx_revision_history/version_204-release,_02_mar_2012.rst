Version 2.0.4-release, 02 mar 2012
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #605, pack vs mysql compress

-  fixed #783, #862, #917, #985, #990, #1032 documentation bugs

-  fixed #885, bitwise AND/OR were not available via API

-  fixed #984, crash on indexing data with MAGIC\_CODE\_ZONE symbol

-  fixed #1004, RT index loses words from dictionary on segments merging
   with ``id64`` enabled

-  fixed #1035, daemon doesn't properly handle FDs in case of socket
   overflow FD\_SETSIZE ( \*nix, ``preopen_indexes=0``,
   ``workers=threads`` )

-  fixed #1038, quoted string for API select

-  fixed #1046, head SPZ overflow, snippet generation at non fast with
   SPZ

-  fixed #1048, distributed index can't sort  filter because of missed
   attributes

-  fixed #1050, expression ranker vs agents

-  fixed #1051, added `MVA64 <../mva_multi-valued_attributes.md>`__
   support to `UDFs <../sphinx_udfs_user_defined_functions.md>`__

-  fixed #1054, `max\_query\_time <../select_syntax.md>`__ not handled
   properly on searching at `RT
   index <../4_real-time_indexes/README.md>`__

-  fixed #1055,
   `expansion\_limit <../searchd_program_configuration_options/expansionlimit.md>`__
   on searching at RT disk chunks

-  fixed #1057, daemon crashes on generating snippet with 0 documents
   provided

-  fixed #1060,
   `load\_files\_scattered <../additional_functionality/buildexcerpts.md>`__
   don't work

-  fixed #1065, libsphinxclient vs distribute index (agents)

-  fixed #1067, modifiers were not escaped in legacy query emulation

-  fixed #1071, master - agent communication got slower for a large
   query

-  fixed #1076, #1077, (redundant copying, and a possible mutex leak
   with uservars)

-  fixed #1078, ``blended`` vs FIELD\_END

-  fixed #1084 crash  index corruption on loading persist MVA

-  fixed #1091, RT attach of plain index with string  MVA attributes
   prior regular attributes

-  fixed #1092, update got binloged with wrong TID

-  fixed #1098, crash on creating large expression

-  fixed #1099, cleaning up temporary files on fail of indexing

-  fixed #1100, missing
   `xmlpipe\_attr\_bigint <../data_source_configuration_options/xmlpipeattr_bigint.md>`__
   config directive

-  fixed #1101, now ignoring dashes within keywords when dash is not in
   charset\_table

-  fixed #1103, ``ZONE`` operator incorrectly works on more than one
   keywords in a simple zone

-  fixed #1106, optimized ``WHERE id=value``,
   ``WHERE id IN (values_list)`` clauses used in ``SELECT``, ``UPDATE``
   statements

-  fixed #1112, Sphinx doesn't work out-of-the-box because the collision
   of ``binlog_path`` option

-  fixed #1116, crash on ``FLUSH RTINDEX`` unknown-index-name

-  fixed #1117, occasional RT headers corruption (leading to crashes
   and/or missing results)

-  fixed #1119, missing expression ranker support in SphinxSE

-  fixed #1120, negative `total\_found <../querying/README.md>`__, docs
   and hits counter on huge indexes
