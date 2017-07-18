.. raw:: html

   <div class="navheader">

8.49. SphinxQL upgrade notes, version 2.0.1-beta
`Prev <sphinxql-reserved-keywords.html>`__ 
Chapter 8. SphinxQL reference
 `Next <api-reference.html>`__

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

.. rubric:: 8.49. SphinxQL upgrade notes, version 2.0.1-beta
   :name: sphinxql-upgrade-notes-version-2.0.1-beta
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

This section only applies to existing applications that use SphinxQL
versions prior to 2.0.1-beta.

In previous versions, SphinxQL just wrapped around SphinxAPI and
inherited its magic columns and column set quirks. Essentially, SphinxQL
queries could return (slightly) different columns and in a (slightly)
different order than it was explicitly requested in the query. Namely,
``weight`` magic column (which is not a real column in any index) was
added at all times, and GROUP BY related ``@count``, ``@group``, and
``@distinct`` magic columns were conditionally added when grouping.
Also, the order of columns (attributes) in the result set was actually
taken from the index rather than the query. (So if you asked for columns
C, B, A in your query but they were in the A, B, C order in the index,
they would have been returned in the A, B, C order.)

In version 2.0.1-beta, we fixed that. SphinxQL is now more SQL compliant
(and will be further brought in as much compliance with standard SQL
syntax as possible).

The important changes are as follows:

.. raw:: html

   <div class="itemizedlist">

-  **``@ID`` magic name is deprecated in favor of ``ID``.** Document ID
   is considered an attribute.

-  **``WEIGHT`` is no longer implicitly returned**, because it is not
   actually a column (an index attribute), but rather an internal
   function computed per each row (a match). You have to explicitly ask
   for it, using the ``WEIGHT()`` function. (The requirement to alias
   the result will be lifted in the next release.)

   .. code:: programlisting

       SELECT id, WEIGHT() w FROM myindex WHERE MATCH('test')

-  **You can now use quoted reserved keywords as aliases.** The quote
   character is backtick (“\`”, ASCII code 96 decimal, 60 hex). One
   particularly useful example would be returning ``weight`` column like
   the old mode:

   .. code:: programlisting

       SELECT id, WEIGHT() `weight` FROM myindex WHERE MATCH('test')

-  The column order is now different and should now match the one
   explicitly defined in the query. So if you are accessing columns
   based on their position in the result set rather than the name (for
   instance, by using ``mysql_fetch_row()`` rather than
   ``mysql_fetch_assoc()`` in PHP), **check and fix the order of columns
   in your queries.**

-  ``SELECT *`` return the columns in index order, as it used to,
   including the ID column. However, **``SELECT *`` does not
   automatically return WEIGHT().** To update such queries in case you
   access columns by names, simply add it to the query:

   .. code:: programlisting

       SELECT *, WEIGHT() `weight` FROM myindex WHERE MATCH('test')

   Otherwise, i.e., in case you rely on column order, select ID, weight,
   and then other columns:

   .. code:: programlisting

       SELECT id, *, WEIGHT() `weight` FROM myindex WHERE MATCH('test')

-  **Magic ``@count`` and ``@distinct`` attributes are no longer
   implicitly returned**. You now have to explicitly ask for them when
   using GROUP BY. (Also note that you currently have to alias them;
   that requirement will be lifted in the future.)

   .. code:: programlisting

       SELECT gid, COUNT(*) q FROM myindex WHERE MATCH('test')
       GROUP BY gid ORDER BY q DESC

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+------------------------------------+----------------------------------+
| `Prev <sphinxql-reserved-keywords.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <api-reference.html>`__   |
+-----------------------------------------------+------------------------------------+----------------------------------+
| 8.48. List of SphinxQL reserved keywords      | `Home <index.html>`__              |  Chapter 9. API reference        |
+-----------------------------------------------+------------------------------------+----------------------------------+

.. raw:: html

   </div>
