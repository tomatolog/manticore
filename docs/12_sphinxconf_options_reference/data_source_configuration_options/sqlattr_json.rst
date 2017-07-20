sql\_attr\_json
~~~~~~~~~~~~~~~

JSON attribute declaration. Multi-value (ie. there may be more than one
such attribute declared), optional. Applies to SQL source types
(``mysql``, ``pgsql``, ``mssql``) only.

When indexing JSON attributes, Sphinx expects a text field with JSON
formatted data. JSON attributes supports arbitrary JSON data with no
limitation in nested levels or types.

::


    {
        "id": 1,
        "gid": 2,
        "title": "some title",
        "tags": [
            "tag1",
            "tag2",
            "tag3"
            {
                "one": "two",
                "three": [4, 5]
            }
        ]
    }

These attributes allow Sphinx to work with documents without a fixed set
of attribute columns. When you filter on a key of a JSON attribute,
documents that don't include the key will simply be ignored.

You can read more on JSON attributes in
http://sphinxsearch.com/blog/2013/08/08/full-json-support-in-trunk/.

Example:
^^^^^^^^

::


    sql_attr_json = properties

