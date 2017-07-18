.. raw:: html

   <div class="navheader">

Chapter 4. Real-time indexes
`Prev <index-merging.html>`__ 
 
 `Next <rt-overview.html>`__

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

`4.1. RT indexes overview <rt-overview.html>`__
`4.2. Known caveats with RT indexes <rt-caveats.html>`__
`4.3. RT index internals <rt-internals.html>`__
`4.4. Binary logging <rt-binlog.html>`__

.. raw:: html

   </div>

Real-time indexes (or RT indexes for brevity) are a new backend that
lets you insert, update, or delete documents (rows) on the fly. RT
indexes were added in version 1.10-beta. While querying of RT indexes is
possible using any of the SphinxAPI, SphinxQL, or SphinxSE, updating
them is only possible via SphinxQL at the moment. Full SphinxQL
reference is available in `Chapter 8, *SphinxQL
reference* <sphinxql-reference.html>`__.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------+-------------------------+--------------------------------+
| `Prev <index-merging.html>`__    |                         |  `Next <rt-overview.html>`__   |
+----------------------------------+-------------------------+--------------------------------+
| 3.13. Index merging              | `Home <index.html>`__   |  4.1. RT indexes overview      |
+----------------------------------+-------------------------+--------------------------------+

.. raw:: html

   </div>
