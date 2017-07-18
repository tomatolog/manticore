Version 0.9.7-rc2, 15 dec 2006
------------------------------

-  added support for extended matching mode (query language)

-  added support for extended sorting mode (sorting clauses)

-  added support for SBCS excerpts

-  added ``mmap()ing`` for attributes and wordlist (improves search
   time, speeds up ``fork()`` greatly)

-  fixed attribute name handling to be case insensitive

-  fixed default compiler options to simplify post-mortem debugging
   (added ``-g``, removed ``-fomit-frame-pointer``)

-  fixed rare memory leak

-  fixed “hello hello” queries in “match phrase” mode

-  fixed issue with excerpts, texts and overlong queries

-  fixed logging multiple index name (no longer tokenized)

-  fixed trailing stopword not flushed from tokenizer

-  fixed boolean evaluation

-  fixed pidfile being wrongly ``unlink()ed`` on ``bind()`` failure

-  fixed ``--with-mysql-includes/libs`` (they conflicted with well-known
   paths)

-  fixes for 64-bit platforms
