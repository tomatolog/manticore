.. raw:: html

   <div class="navheader">

10.1. SphinxSE overview
`Prev <sphinxse.html>`__ 
Chapter 10. MySQL storage engine (SphinxSE)
 `Next <sphinxse-installing.html>`__

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

.. rubric:: 10.1. SphinxSE overview
   :name: sphinxse-overview
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

SphinxSE is MySQL storage engine which can be compiled into MySQL server
5.x using its pluggable architecture. It is not available for MySQL 4.x
series. It also requires MySQL 5.0.22 or higher in 5.0.x series, or
MySQL 5.1.12 or higher in 5.1.x series.

Despite the name, SphinxSE does *not* actually store any data itself. It
is actually a built-in client which allows MySQL server to talk to
``searchd``, run search queries, and obtain search results. All indexing
and searching happen outside MySQL.

Obvious SphinxSE applications include:

.. raw:: html

   <div class="itemizedlist">

-  easier porting of MySQL FTS applications to Sphinx;

-  allowing Sphinx use with programming languages for which native APIs
   are not available yet;

-  optimizations when additional Sphinx result set processing on MySQL
   side is required (eg. JOINs with original document tables, additional
   MySQL-side filtering, etc).

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------+--------------------------+----------------------------------------+
| `Prev <sphinxse.html>`__                       | `Up <sphinxse.html>`__   |  `Next <sphinxse-installing.html>`__   |
+------------------------------------------------+--------------------------+----------------------------------------+
| Chapter 10. MySQL storage engine (SphinxSE)    | `Home <index.html>`__    |  10.2. Installing SphinxSE             |
+------------------------------------------------+--------------------------+----------------------------------------+

.. raw:: html

   </div>
