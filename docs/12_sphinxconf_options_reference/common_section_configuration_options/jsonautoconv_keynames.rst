json\_autoconv\_keynames
~~~~~~~~~~~~~~~~~~~~~~~~

Whether and how to auto-convert key names within JSON attributes. Known
value is ‘lowercase’. Optional, default value is unspecified (do not
convert anything).

When this directive is set to ‘lowercase’, key names within JSON
attributes will be automatically brought to lower case when indexing.
This conversion applies to any data source, that is, JSON attributes
originating from either SQL or XMLpipe2 sources will all be affected.

Example:
^^^^^^^^

::


    json_autoconv_keynames = lowercase

