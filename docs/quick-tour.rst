.. raw:: html

   <div class="navheader">

2.7. Quick Sphinx usage tour
`Prev <sphinx-deprecations-defaults.html>`__ 
Chapter 2. Installation
 `Next <indexing.html>`__

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

.. rubric:: 2.7. Quick Sphinx usage tour
   :name: quick-sphinx-usage-tour
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

All the example commands below assume that you installed Sphinx in
``/usr/local/sphinx``, so ``searchd`` can be found in
``/usr/local/sphinx/bin/searchd``.

To use Sphinx, you will need to:

.. raw:: html

   <div class="orderedlist">

1. Create a configuration file.

   Default configuration file name is ``sphinx.conf``. All Sphinx
   programs look for this file in current working directory by default.

   Sample configuration file, ``sphinx.conf.dist``, which has all the
   options documented, is created by ``configure``. Copy and edit that
   sample file to make your own configuration: (assuming Sphinx is
   installed into ``/usr/local/sphinx/``)

   .. raw:: html

      <div class="literallayout">

   **``$ cd /usr/local/sphinx/etc $ cp sphinx.conf.dist sphinx.conf $ vi sphinx.conf``**

   .. raw:: html

      </div>

   Sample configuration file is setup to index ``documents`` table from
   MySQL database ``test``; so there’s ``example.sql`` sample data file
   to populate that table with a few documents for testing purposes:

   .. raw:: html

      <div class="literallayout">

   **``$ mysql -u test < /usr/local/sphinx/etc/example.sql``**

   .. raw:: html

      </div>

2. Run the indexer to create full-text index from your data:

   .. raw:: html

      <div class="literallayout">

   **``$ cd /usr/local/sphinx/etc $ /usr/local/sphinx/bin/indexer --all``**

   .. raw:: html

      </div>

3. Query your newly created index!

.. raw:: html

   </div>

Now query your indexes!

Connect to server:

.. raw:: html

   <div class="literallayout">

**``$ mysql -h0 -P9306``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT * FROM test1 WHERE MATCH('my document');``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``INSERT INTO rt VALUES (1, 'this is', 'a sample text', 11);``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``INSERT INTO rt VALUES (2, 'some more', 'text here', 22);``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT gid/11 FROM rt WHERE MATCH('text') GROUP BY gid;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT * FROM rt ORDER BY gid DESC;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SHOW TABLES;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT *, WEIGHT() FROM test1 WHERE MATCH('"document one"/1');SHOW META;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SET profiling=1;SELECT * FROM test1 WHERE id IN (1,2,4);SHOW PROFILE;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT id, id%3 idd FROM test1 WHERE MATCH('this is | nothing') GROUP BY idd;SHOW PROFILE;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT id FROM test1 WHERE MATCH('is this a good plan?');SHOW PLAN;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT COUNT(*) c, id%3 idd FROM test1 GROUP BY idd HAVING COUNT(*)>1;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``SELECT COUNT(*) FROM test1;``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``CALL KEYWORDS ('one two three', 'test1');``**

.. raw:: html

   </div>

.. raw:: html

   <div class="literallayout">

**``CALL KEYWORDS ('one two three', 'test1', 1);``**

.. raw:: html

   </div>

Happy searching!

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------------------------+------------------------------+-----------------------------+
| `Prev <sphinx-deprecations-defaults.html>`__                     | `Up <installation.html>`__   |  `Next <indexing.html>`__   |
+------------------------------------------------------------------+------------------------------+-----------------------------+
| 2.6. Sphinx deprecations and changes in default configuration    | `Home <index.html>`__        |  Chapter 3. Indexing        |
+------------------------------------------------------------------+------------------------------+-----------------------------+

.. raw:: html

   </div>
