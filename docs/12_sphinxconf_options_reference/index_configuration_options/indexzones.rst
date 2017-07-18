index\_zones
~~~~~~~~~~~~

A list of in-field HTML/XML zones to index. Optional, default is empty
(do not index zones). Introduced in version 2.0.1-beta.

Zones can be formally defined as follows. Everything between an opening
and a matching closing tag is called a span, and the aggregate of all
spans corresponding sharing the same tag name is called a zone. For
instance, everything between the occurrences of <H1> and </H1> in the
document field belongs to H1 zone.

Zone indexing, enabled by ``index_zones`` directive, is an optional
extension of the HTML stripper. So it will also require that the
`stripper <../../index_configuration_options/htmlstrip.md>`__ is enabled
(with ``html_strip = 1``). The value of the ``index_zones`` should be a
comma-separated list of those tag names and wildcards (ending with a
star) that should be indexed as zones.

Zones can nest and overlap arbitrarily. The only requirement is that
every opening tag has a matching tag. You can also have an arbitrary
number of both zones (as in unique zone names, such as H1) and spans
(all the occurrences of those H1 tags) in a document. Once indexed,
zones can then be used for matching with the ZONE operator, see `the
section called “Extended query
syntax” <../../extended_query_syntax.md>`__.

Example:
^^^^^^^^

::


    index_zones = h*, th, title

Earlier versions than 2.1.1-beta only provided this feature for plain
index files; currently, RT index files also provide it.
