xmlpipe\_attr\_json
~~~~~~~~~~~~~~~~~~~

JSON attribute declaration. Multi-value (ie. there may be more than one
such attribute declared), optional.

This directive is used to declare that the contents of a given XML tag
are to be treated as a JSON document and stored into a Manticore index for
later use. Refer to `the section called
“sql\_attr\_json” <../../data_source_configuration_options/sqlattr_json.md>`__
for more details on the JSON attributes.

Example:
^^^^^^^^

::


    xmlpipe_attr_json = properties

