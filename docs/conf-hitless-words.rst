.. raw:: html

   <div class="navheader">

12.2.45. hitless\_words
`Prev <conf-stopword-step.html>`__ 
12.2. Index configuration options
 `Next <conf-expand-keywords.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.2.45. hitless\_words
   :name: hitless_words
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Hitless words list. Optional, allowed values are ‘all’, or a list file
name. Introduced in version 1.10-beta.

By default, Sphinx full-text index stores not only a list of matching
documents for every given keyword, but also a list of its in-document
positions (aka hitlist). Hitlists enables phrase, proximity, strict
order and other advanced types of searching, as well as phrase proximity
ranking. However, hitlists for specific frequent keywords (that can not
be stopped for some reason despite being frequent) can get huge and thus
slow to process while querying. Also, in some cases we might only care
about boolean keyword matching, and never need position-based searching
operators (such as phrase matching) nor phrase ranking.

``hitless_words`` lets you create indexes that either do not have
positional information (hitlists) at all, or skip it for specific
keywords.

Hitless index will generally use less space than the respective regular
index (about 1.5x can be expected). Both indexing and searching should
be faster, at a cost of missing positional query and ranking support.
When searching, positional queries (eg. phrase queries) will be
automatically converted to respective non-positional (document-level) or
combined queries. For instance, if keywords “hello” and “world” are
hitless, “hello world” phrase query will be converted to (hello & world)
bag-of-words query, matching all documents that mention either of the
keywords but not necessarily the exact phrase. And if, in addition,
keywords “simon” and “says” are not hitless, “simon says hello world”
will be converted to (“simon says” & hello & world) query, matching all
documents that contain “hello” and “world” anywhere in the document, and
also “simon says” as an exact phrase.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    hitless_words = all

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------+-----------------------------------------+
| `Prev <conf-stopword-step.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-expand-keywords.html>`__   |
+---------------------------------------+---------------------------------+-----------------------------------------+
| 12.2.44. stopword\_step               | `Home <index.html>`__           |  12.2.46. expand\_keywords              |
+---------------------------------------+---------------------------------+-----------------------------------------+

.. raw:: html

   </div>
