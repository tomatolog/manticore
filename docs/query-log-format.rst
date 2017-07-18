.. raw:: html

   <div class="navheader">

5.9. \ ``searchd`` query log formats
`Prev <distributed.html>`__ 
Chapter 5. Searching
 `Next <plain-log-format.html>`__

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

.. rubric:: 5.9. \ ``searchd`` query log formats
   :name: searchd-query-log-formats
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="toc">

`5.9.1. Plain log format <plain-log-format.html>`__
`5.9.2. SphinxQL log format <sphinxql-log-format.html>`__

.. raw:: html

   </div>

In version 2.0.1-beta and above two query log formats are supported.
Previous versions only supported a custom plain text format. That format
is still the default one. However, while it might be more convenient for
manual monitoring and review, but hard to replay for benchmarks, it only
logs *search* queries but not the other types of requests, does not
always contain the complete search query data, etc. The default text
format is also harder (and sometimes impossible) to replay for
benchmarking purposes. The new ``sphinxql`` format alleviates that. It
aims to be complete and automatable, even though at the cost of brevity
and readability.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------+---------------------------+-------------------------------------+
| `Prev <distributed.html>`__    | `Up <searching.html>`__   |  `Next <plain-log-format.html>`__   |
+--------------------------------+---------------------------+-------------------------------------+
| 5.8. Distributed searching     | `Home <index.html>`__     |  5.9.1. Plain log format            |
+--------------------------------+---------------------------+-------------------------------------+

.. raw:: html

   </div>
