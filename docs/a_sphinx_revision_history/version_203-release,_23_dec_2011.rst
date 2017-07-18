Version 2.0.3-release, 23 dec 2011
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1031, SphinxQL parsing syntax for MVA at insert  replace
   statements

-  fixed #1027, stalls on attribute update in high-concurrency load

-  fixed #1026, daemon crash on malformed API command

-  fixed #1021, ``max_children`` option has been ignored with
   ``worker=threads``

-  fixed #1020, crash on large attribute files loading

-  fixed #1014, crash on rotation when index has been removed from
   config file (``worker=threads``, \*nix box)

-  fixed #1001, broken MVA files in RT index while saving disk chunk

-  fixed #995, crash on empty MVA updates

-  fixed #994, crash on daemon shutdown with ``seamless_rotate=0`` and
   ``workers=threads``

-  fixed #993, #998, crash on replay ``DELETE`` statement vs RT index
   with ``dict=keywords``, fixed sequential ``INSERT`` into
   ``dict=keywords`` index right after ``INSERT`` into ``dict=crc``
   index

-  fixed #991, crash on indexing mssql source with ``mssql_unicode``
   enabled

-  fixed #983, #950, crash on host name lookup (SphinxSE with MySQL 5.5)

-  fixed #981, snippet inconsistency with ``allow_empty=0``

-  fixed #980, broken index produced by index merge in rare cases

-  fixed #971, absent error message at master on agent “maxed out”

-  fixed #695, #815, #835, #866, malformed warnings in SphinxQL

-  fixed build of SphinxSE with MySQL 5.1

-  fixed crash log for ‘fork’ and ‘prefork’ workers
