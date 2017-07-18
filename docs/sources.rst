.. raw:: html

   <div class="navheader">

3.1. Data sources
`Prev <indexing.html>`__ 
Chapter 3. Indexing
 `Next <fields.html>`__

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

.. rubric:: 3.1. Data sources
   :name: data-sources
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The data to be indexed can generally come from very different sources:
SQL databases, plain text files, HTML files, mailboxes, and so on. From
Sphinx point of view, the data it indexes is a set of structured
*documents*, each of which has the same set of *fields* and
*attributes*. This is similar to SQL, where each row would correspond to
a document, and each column to either a field or an attribute.

Depending on what source Sphinx should get the data from, different code
is required to fetch the data and prepare it for indexing. This code is
called *data source driver* (or simply *driver* or *data source* for
brevity).

At the time of this writing, there are built-in drivers for MySQL,
PostgreSQL, MS SQL (on Windows), and ODBC. There is also a generic
driver called xmlpipe2, which runs a specified command and reads the
data from its ``stdout``. See `Section 3.9, “xmlpipe2 data
source” <xmlpipe2.html>`__ section for the format description. In
2.2.1-beta a tsvpipe (Tab Separated Values) and csvpipe (Comma Separated
Values) data source was added. You can get more information here
`Section 3.10, “tsvpipe\\csvpipe (Tab\\Comma Separated Values) data
source” <xsvpipe.html>`__.

There can be as many sources per index as necessary. They will be
sequentially processed in the very same order which was specified in
index definition. All the documents coming from those sources will be
merged as if they were coming from a single source.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------+--------------------------+---------------------------+
| `Prev <indexing.html>`__    | `Up <indexing.html>`__   |  `Next <fields.html>`__   |
+-----------------------------+--------------------------+---------------------------+
| Chapter 3. Indexing         | `Home <index.html>`__    |  3.2. Full-text fields    |
+-----------------------------+--------------------------+---------------------------+

.. raw:: html

   </div>
