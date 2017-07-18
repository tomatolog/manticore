.. raw:: html

   <div class="navheader">

12.2.9. index\_zones
`Prev <conf-index-sp.html>`__ 
12.2. Index configuration options
 `Next <conf-min-stemming-len.html>`__

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

.. rubric:: 12.2.9. index\_zones
   :name: index_zones
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A list of in-field HTML/XML zones to index. Optional, default is empty
(do not index zones). Introduced in version 2.0.1-beta.

Zones can be formally defined as follows. Everything between an opening
and a matching closing tag is called a span, and the aggregate of all
spans corresponding sharing the same tag name is called a zone. For
instance, everything between the occurrences of <H1> and </H1> in the
document field belongs to H1 zone.

Zone indexing, enabled by ``index_zones`` directive, is an optional
extension of the HTML stripper. So it will also require that the
`stripper <conf-html-strip.html>`__ is enabled (with
``html_strip = 1``). The value of the ``index_zones`` should be a
comma-separated list of those tag names and wildcards (ending with a
star) that should be indexed as zones.

Zones can nest and overlap arbitrarily. The only requirement is that
every opening tag has a matching tag. You can also have an arbitrary
number of both zones (as in unique zone names, such as H1) and spans
(all the occurrences of those H1 tags) in a document. Once indexed,
zones can then be used for matching with the ZONE operator, see
`Section 5.3, “Extended query syntax” <extended-syntax.html>`__.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    index_zones = h*, th, title

Earlier versions than 2.1.1-beta only provided this feature for plain
index files; currently, RT index files also provide it.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------+---------------------------------+------------------------------------------+
| `Prev <conf-index-sp.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-min-stemming-len.html>`__   |
+----------------------------------+---------------------------------+------------------------------------------+
| 12.2.8. index\_sp                | `Home <index.html>`__           |  12.2.10. min\_stemming\_len             |
+----------------------------------+---------------------------------+------------------------------------------+

.. raw:: html

   </div>
