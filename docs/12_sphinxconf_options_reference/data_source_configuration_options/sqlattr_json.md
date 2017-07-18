### sql_attr_json {#sql-attr-json}

JSON attribute declaration. Multi-value (ie. there may be more than one such attribute declared), optional. Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only. Introduced in version 2.1.1-beta.

When indexing JSON attributes, Sphinx expects a text field with JSON formatted data. As of 2.2.1-beta JSON attributes supports arbitrary JSON data with no limitation in nested levels or types.

```

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

```

These attributes allow Sphinx to work with documents without a fixed set of attribute columns. When you filter on a key of a JSON attribute, documents that don&#039;t include the key will simply be ignored.

You can read more on JSON attributes in [http://sphinxsearch.com/blog/2013/08/08/full-json-support-in-trunk/](http://sphinxsearch.com/blog/2013/08/08/full-json-support-in-trunk/).

#### Example: {#example}

```

sql_attr_json = properties

```