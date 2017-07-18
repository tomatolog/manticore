.. raw:: html

   <div class="navheader">

3.11. Live index updates
`Prev <xsvpipe.html>`__ 
Chapter 3. Indexing
 `Next <delta-updates.html>`__

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

.. rubric:: 3.11. Live index updates
   :name: live-index-updates
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

There are two major approaches to maintaining the full-text index
contents up to date. Note, however, that both these approaches deal with
the task of *full-text data updates*, and not attribute updates. Instant
attribute updates are supported since version 0.9.8. Refer to
`UpdateAttributes() <api-func-updateatttributes.html>`__ API call
description for details.

First, you can use disk-based indexes, partition them manually, and only
rebuild the smaller partitions (so-called “deltas”) frequently. By
minimizing the rebuild size, you can reduce the average indexing lag to
something as low as 30-60 seconds. This approach was the only one
available in versions 0.9.x. On huge collections it actually might be
the most efficient one. Refer to `Section 3.12, “Delta index
updates” <delta-updates.html>`__ for details.

Second, versions 1.x (starting with 1.10-beta) add support for so-called
real-time indexes (RT indexes for short) that on-the-fly updates of the
full-text data. Updates on a RT index can appear in the search results
in 1-2 milliseconds, ie. 0.001-0.002 seconds. However, RT index are less
efficient for bulk indexing huge amounts of data. Refer to `Chapter 4,
*Real-time indexes* <rt-indexes.html>`__ for details.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------------------------------+--------------------------+----------------------------------+
| `Prev <xsvpipe.html>`__                                             | `Up <indexing.html>`__   |  `Next <delta-updates.html>`__   |
+---------------------------------------------------------------------+--------------------------+----------------------------------+
| 3.10. tsvpipe\\csvpipe (Tab\\Comma Separated Values) data source    | `Home <index.html>`__    |  3.12. Delta index updates       |
+---------------------------------------------------------------------+--------------------------+----------------------------------+

.. raw:: html

   </div>
