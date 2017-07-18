.. raw:: html

   <div class="navheader">

Chapter 8. SphinxQL reference
`Prev <ref-wordbreaker.html>`__ 
 
 `Next <sphinxql-select.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="chapter">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="toc">

**Table of Contents**

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

.. raw:: html

   </div>

SphinxQL is our SQL dialect that exposes all of the search daemon
functionality using a standard SQL syntax with a few Sphinx-specific
extensions. Everything available via the SphinxAPI is also available via
SphinxQL but not vice versa; for instance, writes into RT indexes are
only available via SphinxQL. This chapter documents supported SphinxQL
statements syntax.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+-------------------------+------------------------------------+
| `Prev <ref-wordbreaker.html>`__             |                         |  `Next <sphinxql-select.html>`__   |
+---------------------------------------------+-------------------------+------------------------------------+
| 7.5. \ ``wordbreaker`` command reference    | `Home <index.html>`__   |  8.1. SELECT syntax                |
+---------------------------------------------+-------------------------+------------------------------------+

.. raw:: html

   </div>
