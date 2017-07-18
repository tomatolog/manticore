xmlpipe\_attr\_multi
~~~~~~~~~~~~~~~~~~~~

xmlpipe MVA attribute declaration. Multi-value, optional. Applies to
``xmlpipe2`` source type only.

This setting declares an MVA attribute tag in xmlpipe2 stream. The
contents of the specified tag will be parsed and a list of integers that
will constitute the MVA will be extracted, similar to how
`sql\_attr\_multi <../../data_source_configuration_options/sqlattr_multi.rst>`__
parses SQL column contents when ‘field’ MVA source type is specified.

Example:
^^^^^^^^

::


    xmlpipe_attr_multi = taglist

