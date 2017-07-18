.. raw:: html

   <div class="navheader">

3.2. Full-text fields
`Prev <sources.html>`__ 
Chapter 3. Indexing
 `Next <attributes.html>`__

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

.. rubric:: 3.2. Full-text fields
   :name: full-text-fields
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Full-text fields (or just *fields* for brevity) are the textual document
contents that get indexed by Sphinx, and can be (quickly) searched for
keywords.

Fields are named, and you can limit your searches to a single field (eg.
search through “title” only) or a subset of fields (eg. to “title” and
“abstract” only). Sphinx index format generally supports up to 256
fields. However, up to version 2.0.1-beta indexes were forcibly limited
by 32 fields, because of certain complications in the matching engine.
Full support for up to 256 fields was added in version 2.0.2-beta.

Note that the original contents of the fields are **not** stored in the
Sphinx index. The text that you send to Sphinx gets processed, and a
full-text index (a special data structure that enables quick searches
for a keyword) gets built from that text. But the original text contents
are then simply discarded. Sphinx assumes that you store those contents
elsewhere anyway.

Moreover, it is impossible to *fully* reconstruct the original text,
because the specific whitespace, capitalization, punctuation, etc will
all be lost during indexing. It is theoretically possible to partially
reconstruct a given document from the Sphinx full-text index, but that
would be a slow process (especially if the `CRC
dictionary <conf-dict.html>`__ is used, which does not even store the
original keywords and works with their hashes instead).

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------+--------------------------+-------------------------------+
| `Prev <sources.html>`__    | `Up <indexing.html>`__   |  `Next <attributes.html>`__   |
+----------------------------+--------------------------+-------------------------------+
| 3.1. Data sources          | `Home <index.html>`__    |  3.3. Attributes              |
+----------------------------+--------------------------+-------------------------------+

.. raw:: html

   </div>
