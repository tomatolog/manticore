Version 2.2.5-release, 06 oct 2014
----------------------------------

New minor features
~~~~~~~~~~~~~~~~~~

-  added OPTION `rand\_seed <../select_syntax.rst>`__ which affects ORDER
   BY RAND()

Bug fixes
~~~~~~~~~

-  fixed #2042, ``indextool`` fails with field mask on 32+ fields

-  fixed #2031, wrong encoding with UnixODBC/Oracle source

-  fixed #2056, several bugs in RLP tokenizer

-  fixed #2054, `SHOW THREADS <../show_threads_syntax.rst>`__ hangs if
   queries in prefork mode

-  fixed #2057, WARNING at ``indexer`` on duplicated wordforms

-  fixed #2066, snippet generation with
   `weight\_order <../additional_functionality/buildexcerpts.rst>`__
   enabled

-  fixed exception parsing in queries

-  fixed crash in config parser

-  fixed MySQL protocol response when daemon maxed out
