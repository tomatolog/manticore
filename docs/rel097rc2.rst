.. raw:: html

   <div class="navheader">

A.41. Version 0.9.7-rc2, 15 dec 2006
`Prev <rel097.html>`__ 
Appendix A. Sphinx revision history
 `Next <rel097rc.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: A.41. Version 0.9.7-rc2, 15 dec 2006
   :name: a.41.version-0.9.7-rc2-15-dec-2006
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="itemizedlist">

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

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+---------------------------+-----------------------------------------+
| `Prev <rel097.html>`__              | `Up <changelog.html>`__   |  `Next <rel097rc.html>`__               |
+-------------------------------------+---------------------------+-----------------------------------------+
| A.40. Version 0.9.7, 02 apr 2007    | `Home <index.html>`__     |  A.42. Version 0.9.7-rc1, 26 oct 2006   |
+-------------------------------------+---------------------------+-----------------------------------------+

.. raw:: html

   </div>
