.. raw:: html

   <div class="navheader">

3.5. Indexes
`Prev <mva.html>`__ 
Chapter 3. Indexing
 `Next <data-restrictions.html>`__

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

.. rubric:: 3.5. Indexes
   :name: indexes
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

To be able to answer full-text search queries fast, Sphinx needs to
build a special data structure optimized for such queries from your text
data. This structure is called *index*; and the process of building
index from text is called *indexing*.

Different index types are well suited for different tasks. For example,
a disk-based tree-based index would be easy to update (ie. insert new
documents to existing index), but rather slow to search. Sphinx
architecture allows internally for different *index types*, or
*backends*, to be implemented comparatively easily.

Starting with 1.10-beta, Sphinx provides 2 different backends: a **disk
index** backend, and a **RT (realtime) index** backend.

**Disk indexes** are designed to provide maximum indexing and searching
speed, while keeping the RAM footprint as low as possible. That comes at
a cost of text index updates. You can not update an existing document or
incrementally add a new document to a disk index. You only can batch
rebuild the entire disk index from scratch. (Note that you still can
update document’s **attributes** on the fly, even with the disk
indexes.)

This “rebuild only” limitation might look as a big constraint at a first
glance. But in reality, it can very frequently be worked around rather
easily by setting up multiple disk indexes, searching through them all,
and only rebuilding the one with a fraction of the most recently changed
data. See `Section 3.11, “Live index updates” <live-updates.html>`__ for
details.

**RT indexes** enable you to implement dynamic updates and incremental
additions to the full text index. RT stands for Real Time and they are
indeed “soft realtime” in terms of writes, meaning that most index
changes become available for searching as quick as 1 millisecond or
less, but could occasionally stall for seconds. (Searches will still
work even during that occasional writing stall.) Refer to `Chapter 4,
*Real-time indexes* <rt-indexes.html>`__ for details.

Last but not least, Sphinx supports so-called **distributed indexes**.
Compared to disk and RT indexes, those are not a real physical backend,
but rather just lists of either local or remote indexes that can be
searched transparently to the application, with Sphinx doing all the
chores of sending search requests to remote machines in the cluster,
aggregating the result sets, retrying the failed requests, and even
doing some load balancing. See `Section 5.8, “Distributed
searching” <distributed.html>`__ for a discussion of distributed
indexes.

There can be as many indexes per configuration file as necessary.
``indexer`` utility can reindex either all of them (if ``--all`` option
is specified), or a certain explicitly specified subset. ``searchd``
utility will serve all the specified indexes, and the clients can
specify what indexes to search in run time.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+--------------------------+-----------------------------------------+
| `Prev <mva.html>`__                   | `Up <indexing.html>`__   |  `Next <data-restrictions.html>`__      |
+---------------------------------------+--------------------------+-----------------------------------------+
| 3.4. MVA (multi-valued attributes)    | `Home <index.html>`__    |  3.6. Restrictions on the source data   |
+---------------------------------------+--------------------------+-----------------------------------------+

.. raw:: html

   </div>
