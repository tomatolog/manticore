.. raw:: html

   <div class="navheader">

Sphinx 2.3.3-dev reference manual
 
 
 `Next <intro.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="book" lang="en">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. rubric:: Free open-source SQL full-text search engine
   :name: free-open-source-sql-full-text-search-engine
   :class: subtitle

.. raw:: html

   </div>

.. raw:: html

   <div>

Copyright © 2001-2016 Andrew Aksyonoff

.. raw:: html

   </div>

.. raw:: html

   <div>

Copyright © 2008-2016 Sphinx Technologies Inc, http://sphinxsearch.com

.. raw:: html

   </div>

.. raw:: html

   </div>

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="toc">

**Table of Contents**

`1. Introduction <intro.html>`__
`1.1. About <about.html>`__
`1.2. Sphinx features <features.html>`__
`1.3. Where to get Sphinx <getting.html>`__
`1.4. License <license.html>`__
`1.5. Credits <credits.html>`__
`1.6. History <history.html>`__
`2. Installation <installation.html>`__
`2.1. Supported systems <supported-system.html>`__
`2.2. Compiling Sphinx from source <compiling-from-source.html>`__
`2.3. Installing Sphinx packages on Debian and
Ubuntu <installing-debian.html>`__
`2.4. Installing Sphinx packages on RedHat and
CentOS <installing-redhat.html>`__
`2.5. Installing Sphinx on Windows <installing-windows.html>`__
`2.6. Sphinx deprecations and changes in default
configuration <sphinx-deprecations-defaults.html>`__
`2.7. Quick Sphinx usage tour <quick-tour.html>`__
`3. Indexing <indexing.html>`__
`3.1. Data sources <sources.html>`__
`3.2. Full-text fields <fields.html>`__
`3.3. Attributes <attributes.html>`__
`3.4. MVA (multi-valued attributes) <mva.html>`__
`3.5. Indexes <indexes.html>`__
`3.6. Restrictions on the source data <data-restrictions.html>`__
`3.7. Charsets, case folding, translation tables, and replacement
rules <charsets.html>`__
`3.8. SQL data sources (MySQL, PostgreSQL) <sql.html>`__
`3.9. xmlpipe2 data source <xmlpipe2.html>`__
`3.10. tsvpipe\\csvpipe (Tab\\Comma Separated Values) data
source <xsvpipe.html>`__
`3.11. Live index updates <live-updates.html>`__
`3.12. Delta index updates <delta-updates.html>`__
`3.13. Index merging <index-merging.html>`__
`4. Real-time indexes <rt-indexes.html>`__
`4.1. RT indexes overview <rt-overview.html>`__
`4.2. Known caveats with RT indexes <rt-caveats.html>`__
`4.3. RT index internals <rt-internals.html>`__
`4.4. Binary logging <rt-binlog.html>`__
`5. Searching <searching.html>`__
`5.1. Matching modes <matching-modes.html>`__
`5.2. Boolean query syntax <boolean-syntax.html>`__
`5.3. Extended query syntax <extended-syntax.html>`__
`5.4. Search results ranking <weighting.html>`__
`5.5. Expressions, functions, and operators <expressions.html>`__
`5.6. Sorting modes <sorting-modes.html>`__
`5.7. Grouping (clustering) search results <clustering.html>`__
`5.8. Distributed searching <distributed.html>`__
`5.9. ``searchd`` query log formats <query-log-format.html>`__
`5.10. MySQL protocol support and SphinxQL <sphinxql.html>`__
`5.11. HTTP protocol <http-rest.html>`__
`5.12. Multi-queries <multi-queries.html>`__
`5.13. Collations <collations.html>`__
`5.14. Query cache <qcache.html>`__
`6. Extending Sphinx <extending-sphinx.html>`__
`6.1. Sphinx UDFs (User Defined Functions) <sphinx-udfs.html>`__
`6.2. Sphinx plugins <sphinx-plugins.html>`__
`6.3. Ranker plugins <ranker-plugins.html>`__
`7. Command line tools reference <command-line-tools.html>`__
`7.1. ``indexer`` command reference <ref-indexer.html>`__
`7.2. ``searchd`` command reference <ref-searchd.html>`__
`7.3. ``spelldump`` command reference <ref-spelldump.html>`__
`7.4. ``indextool`` command reference <ref-indextool.html>`__
`7.5. ``wordbreaker`` command reference <ref-wordbreaker.html>`__
`8. SphinxQL reference <sphinxql-reference.html>`__
`8.1. SELECT syntax <sphinxql-select.html>`__
`8.2. SELECT @@system\_variable syntax <sphinxql-select-sysvar.html>`__
`8.3. SHOW META syntax <sphinxql-show-meta.html>`__
`8.4. SHOW WARNINGS syntax <sphinxql-show-warnings.html>`__
`8.5. SHOW STATUS syntax <sphinxql-show-status.html>`__
`8.6. INSERT and REPLACE syntax <sphinxql-insert.html>`__
`8.7. REPLACE syntax <sphinxql-replace.html>`__
`8.8. DELETE syntax <sphinxql-delete.html>`__
`8.9. SET syntax <sphinxql-set.html>`__
`8.10. SET TRANSACTION syntax <sphinxql-set-transaction.html>`__
`8.11. BEGIN, COMMIT, and ROLLBACK syntax <sphinxql-commit.html>`__
`8.12. BEGIN syntax <sphinxql-begin.html>`__
`8.13. ROLLBACK syntax <sphinxql-rollback.html>`__
`8.14. CALL SNIPPETS syntax <sphinxql-call-snippets.html>`__
`8.15. CALL KEYWORDS syntax <sphinxql-call-keywords.html>`__
`8.16. CALL QSUGGEST syntax <sphinxql-call-qsuggest.html>`__
`8.17. CALL SUGGEST syntax <sphinxql-call-suggest.html>`__
`8.18. SHOW TABLES syntax <sphinxql-show-tables.html>`__
`8.19. DESCRIBE syntax <sphinxql-describe.html>`__
`8.20. CREATE FUNCTION syntax <sphinxql-create-function.html>`__
`8.21. DROP FUNCTION syntax <sphinxql-drop-function.html>`__
`8.22. SHOW VARIABLES syntax <sphinxql-show-variables.html>`__
`8.23. SHOW COLLATION syntax <sphinxql-show-collation.html>`__
`8.24. SHOW CHARACTER SET syntax <sphinxql-show-character-set.html>`__
`8.25. UPDATE syntax <sphinxql-update.html>`__
`8.26. ALTER syntax <sphinxql-attach.html>`__
`8.27. ATTACH INDEX syntax <sphinxql-attach-index.html>`__
`8.28. FLUSH RTINDEX syntax <sphinxql-flush-rtindex.html>`__
`8.29. FLUSH RAMCHUNK syntax <sphinxql-flush-ramchunk.html>`__
`8.30. FLUSH ATTRIBUTES syntax <sphinxql-flush-attributes.html>`__
`8.31. FLUSH HOSTNAMES syntax <sphinxql-flush-hostnames.html>`__
`8.32. TRUNCATE RTINDEX syntax <sphinxql-truncate-rtindex.html>`__
`8.33. SHOW AGENT STATUS <sphinxql-show-agent-status.html>`__
`8.34. SHOW PROFILE syntax <sphinxql-show-profile.html>`__
`8.35. SHOW INDEX STATUS syntax <sphinxql-show-index-status.html>`__
`8.36. SHOW INDEX SETTINGS syntax <sphinxql-show-index-settings.html>`__
`8.37. OPTIMIZE INDEX syntax <sphinxql-optimize-index.html>`__
`8.38. SHOW PLAN syntax <sphinxql-show-plan.html>`__
`8.39. SHOW DATABASES syntax <sphinxql-show-databases.html>`__
`8.40. CREATE PLUGIN syntax <sphinxql-create-plugin.html>`__
`8.41. DROP PLUGIN syntax <sphinxql-drop-plugin.html>`__
`8.42. SHOW PLUGINS syntax <sphinxql-show-plugins.html>`__
`8.43. RELOAD PLUGINS syntax <sphinxql-reload-plugins.html>`__
`8.44. SHOW THREADS syntax <sphinxql-threads.html>`__
`8.45. RELOAD INDEX syntax <sphinxql-reload-index.html>`__
`8.46. Multi-statement queries <sphinxql-multi-queries.html>`__
`8.47. Comment syntax <sphinxql-comment-syntax.html>`__
`8.48. List of SphinxQL reserved
keywords <sphinxql-reserved-keywords.html>`__
`8.49. SphinxQL upgrade notes, version
2.0.1-beta <sphinxql-upgrading-magics.html>`__
`9. API reference <api-reference.html>`__
`9.1. General API functions <api-funcgroup-general.html>`__
`9.2. General query
settings <api-funcgroup-general-query-settings.html>`__
`9.3. Full-text search query
settings <api-funcgroup-fulltext-query-settings.html>`__
`9.4. Result set filtering settings <api-funcgroup-filtering.html>`__
`9.5. GROUP BY settings <api-funcgroup-groupby.html>`__
`9.6. Querying <api-funcgroup-querying.html>`__
`9.7. Additional
functionality <api-funcgroup-additional-functionality.html>`__
`9.8. Persistent connections <api-funcgroup-pconn.html>`__
`10. MySQL storage engine (SphinxSE) <sphinxse.html>`__
`10.1. SphinxSE overview <sphinxse-overview.html>`__
`10.2. Installing SphinxSE <sphinxse-installing.html>`__
`10.3. Using SphinxSE <sphinxse-using.html>`__
`10.4. Building snippets (excerpts) via
MySQL <sphinxse-snippets.html>`__
`11. Reporting bugs <reporting-bugs.html>`__
`12. ``sphinx.conf`` options reference <conf-reference.html>`__
`12.1. Data source configuration options <confgroup-source.html>`__
`12.2. Index configuration options <confgroup-index.html>`__
`12.3. ``indexer`` program configuration
options <confgroup-indexer.html>`__
`12.4. ``searchd`` program configuration
options <confgroup-searchd.html>`__
`12.5. Common section configuration options <confgroup-common.html>`__
`A. Sphinx revision history <changelog.html>`__
`A.1. Version 2.3.2-beta, 09 sep 2016 <rel232.html>`__
`A.2. Version 2.3.1-beta, 03 mar 2015 <rel231.html>`__
`A.3. Version 2.2.11-release, 19 jul 2016 <rel2211.html>`__
`A.4. Version 2.2.10-release, 07 sep 2015 <rel2210.html>`__
`A.5. Version 2.2.9-release, 16 apr 2015 <rel229.html>`__
`A.6. Version 2.2.8-release, 09 mar 2015 <rel228.html>`__
`A.7. Version 2.2.7-release, 20 jan 2015 <rel227.html>`__
`A.8. Version 2.2.6-release, 13 nov 2014 <rel226.html>`__
`A.9. Version 2.2.5-release, 06 oct 2014 <rel225.html>`__
`A.10. Version 2.2.4-release, 11 sep 2014 <rel224.html>`__
`A.11. Version 2.2.3-beta, 13 may 2014 <rel223.html>`__
`A.12. Version 2.2.2-beta, 11 feb 2014 <rel222.html>`__
`A.13. Version 2.2.1-beta, 13 nov 2013 <rel221.html>`__
`A.14. Version 2.1.9-release, 03 jul 2014 <rel219.html>`__
`A.15. Version 2.1.8-release, 28 apr 2014 <rel218.html>`__
`A.16. Version 2.1.7-release, 30 mar 2014 <rel217.html>`__
`A.17. Version 2.1.6-release, 24 feb 2014 <rel216.html>`__
`A.18. Version 2.1.5-release, 22 jan 2014 <rel215.html>`__
`A.19. Version 2.1.4-release, 18 dec 2013 <rel214.html>`__
`A.20. Version 2.1.3-release, 12 nov 2013 <rel213.html>`__
`A.21. Version 2.1.2-release, 10 oct 2013 <rel212.html>`__
`A.22. Version 2.1.1-beta, 20 feb 2013 <rel211.html>`__
`A.23. Version 2.0.11-dev, xx xxx xxxx <rel2011.html>`__
`A.24. Version 2.0.10-release, 22 jan 2014 <rel2010.html>`__
`A.25. Version 2.0.9-release, 26 aug 2013 <rel209.html>`__
`A.26. Version 2.0.8-release, 26 apr 2013 <rel208.html>`__
`A.27. Version 2.0.7-release, 26 mar 2013 <rel207.html>`__
`A.28. Version 2.0.6-release, 22 oct 2012 <rel206.html>`__
`A.29. Version 2.0.5-release, 28 jul 2012 <rel205.html>`__
`A.30. Version 2.0.4-release, 02 mar 2012 <rel204.html>`__
`A.31. Version 2.0.3-release, 23 dec 2011 <rel203.html>`__
`A.32. Version 2.0.2-beta, 15 nov 2011 <rel202.html>`__
`A.33. Version 2.0.1-beta, 22 apr 2011 <rel201.html>`__
`A.34. Version 1.10-beta, 19 jul 2010 <rel110.html>`__
`A.35. Version 0.9.9-release, 02 dec 2009 <rel099.html>`__
`A.36. Version 0.9.9-rc2, 08 apr 2009 <rel099rc2.html>`__
`A.37. Version 0.9.9-rc1, 17 nov 2008 <rel099rc1.html>`__
`A.38. Version 0.9.8.1, 30 oct 2008 <rel0981.html>`__
`A.39. Version 0.9.8, 14 jul 2008 <rel098.html>`__
`A.40. Version 0.9.7, 02 apr 2007 <rel097.html>`__
`A.41. Version 0.9.7-rc2, 15 dec 2006 <rel097rc2.html>`__
`A.42. Version 0.9.7-rc1, 26 oct 2006 <rel097rc.html>`__
`A.43. Version 0.9.6, 24 jul 2006 <rel096.html>`__
`A.44. Version 0.9.6-rc1, 26 jun 2006 <rel096rc1.html>`__

.. raw:: html

   </div>

.. raw:: html

   <div class="list-of-tables">

**List of Tables**

5.1. ` <ranking-factors.html#ranking-factors-table>`__

.. raw:: html

   </div>

.. raw:: html

   <div class="list-of-examples">

**List of Examples**

3.1. `Ranged query usage example <sql.html#ex-ranged-queries>`__
3.2. `xmlpipe2 document stream <xmlpipe2.html#ex-xmlpipe2-document>`__
3.3. `Fully automated live
updates <delta-updates.html#ex-live-updates>`__
4.1. `RT index declaration <rt-overview.html#ex-rt-updates>`__
5.1. `Boolean query example <boolean-syntax.html#ex-boolean-query>`__
5.2. `Extended matching mode: query
example <extended-syntax.html#ex-extended-query>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----+-----+----------------------------+
|     |     |  `Next <intro.html>`__     |
+-----+-----+----------------------------+
|     |     |  Chapter 1. Introduction   |
+-----+-----+----------------------------+

.. raw:: html

   </div>
