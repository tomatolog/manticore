.. raw:: html

   <div class="navheader">

12.4. \ ``searchd`` program configuration options
`Prev <conf-lemmatizer-cache.html>`__ 
Chapter 12. \ ``sphinx.conf`` options reference
 `Next <conf-listen.html>`__

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

.. rubric:: 12.4. \ ``searchd`` program configuration options
   :name: searchd-program-configuration-options
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="toc">

`12.4.1. listen <conf-listen.html>`__
`12.4.2. log <conf-log.html>`__
`12.4.3. query\_log <conf-query-log.html>`__
`12.4.4. query\_log\_format <conf-query-log-format.html>`__
`12.4.5. read\_timeout <conf-read-timeout.html>`__
`12.4.6. client\_timeout <conf-client-timeout.html>`__
`12.4.7. sphinxql\_timeout <conf-sphinxql-timeout.html>`__
`12.4.8. max\_children <conf-max-children.html>`__
`12.4.9. net\_workers <conf-net-workers.html>`__
`12.4.10. queue\_max\_length <conf-queue-max-length.html>`__
`12.4.11. pid\_file <conf-pid-file.html>`__
`12.4.12. seamless\_rotate <conf-seamless-rotate.html>`__
`12.4.13. preopen\_indexes <conf-preopen-indexes.html>`__
`12.4.14. unlink\_old <conf-unlink-old.html>`__
`12.4.15. attr\_flush\_period <conf-attr-flush-period.html>`__
`12.4.16. max\_packet\_size <conf-max-packet-size.html>`__
`12.4.17. mva\_updates\_pool <conf-mva-updates-pool.html>`__
`12.4.18. max\_filters <conf-max-filters.html>`__
`12.4.19. max\_filter\_values <conf-max-filter-values.html>`__
`12.4.20. listen\_backlog <conf-listen-backlog.html>`__
`12.4.21. read\_buffer <conf-read-buffer.html>`__
`12.4.22. read\_unhinted <conf-read-unhinted.html>`__
`12.4.23. max\_batch\_queries <conf-max-batch-queries.html>`__
`12.4.24. subtree\_docs\_cache <conf-subtree-docs-cache.html>`__
`12.4.25. subtree\_hits\_cache <conf-subtree-hits-cache.html>`__
`12.4.26. workers <conf-workers.html>`__
`12.4.27. dist\_threads <conf-dist-threads.html>`__
`12.4.28. binlog\_path <conf-binlog-path.html>`__
`12.4.29. binlog\_flush <conf-binlog-flush.html>`__
`12.4.30. binlog\_max\_log\_size <conf-binlog-max-log-size.html>`__
`12.4.31. snippets\_file\_prefix <conf-snippets-file-prefix.html>`__
`12.4.32. collation\_server <conf-collation-server.html>`__
`12.4.33. collation\_libc\_locale <conf-collation-libc-locale.html>`__
`12.4.34. mysql\_version\_string <conf-mysql-version-string.html>`__
`12.4.35. rt\_flush\_period <conf-rt-flush-period.html>`__
`12.4.36. thread\_stack <conf-thread-stack.html>`__
`12.4.37. expansion\_limit <conf-expansion-limit.html>`__
`12.4.38. watchdog <conf-watchdog.html>`__
`12.4.39. sphinxql\_state <conf-sphinxql-state.html>`__
`12.4.40. ha\_ping\_interval <conf-ha-ping-interval.html>`__
`12.4.41. ha\_period\_karma <conf-ha-period-karma.html>`__
`12.4.42.
persistent\_connections\_limit <conf-persistent-connections-limit.html>`__
`12.4.43. rt\_merge\_iops <conf-rt-merge-iops.html>`__
`12.4.44. rt\_merge\_maxiosize <conf-rt-merge-maxiosize.html>`__
`12.4.45. predicted\_time\_costs <conf-predicted-time-costs.html>`__
`12.4.46. shutdown\_timeout <conf-shutdown-timeout.html>`__
`12.4.47. ondisk\_attrs\_default <conf-ondisk-attrs-default.html>`__
`12.4.48. query\_log\_min\_msec <conf-query-log-min-msec.html>`__
`12.4.49.
agent\_connect\_timeout <conf-agent-connect-timeout-default.html>`__
`12.4.50.
agent\_query\_timeout <conf-agent-query-timeout-default.html>`__
`12.4.51. agent\_retry\_count <conf-agent-retry-count.html>`__
`12.4.52. agent\_retry\_delay <conf-agent-retry-delay.html>`__
`12.4.53. hostname\_lookup <conf-hostname-lookup.html>`__
`12.4.54. qcache\_max\_bytes <conf-qcache-max-bytes.html>`__
`12.4.55. qcache\_thresh\_msec <conf-qcache-thresh-msec.html>`__
`12.4.56. qcache\_ttl\_sec <conf-qcache-ttl-sec.html>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+--------------------------------+--------------------------------+
| `Prev <conf-lemmatizer-cache.html>`__    | `Up <conf-reference.html>`__   |  `Next <conf-listen.html>`__   |
+------------------------------------------+--------------------------------+--------------------------------+
| 12.3.8. lemmatizer\_cache                | `Home <index.html>`__          |  12.4.1. listen                |
+------------------------------------------+--------------------------------+--------------------------------+

.. raw:: html

   </div>
