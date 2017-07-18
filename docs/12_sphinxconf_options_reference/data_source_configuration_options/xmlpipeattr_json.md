### xmlpipe_attr_json {#xmlpipe-attr-json}

JSON attribute declaration. Multi-value (ie. there may be more than one such attribute declared), optional. Introduced in version 2.1.1-beta.

This directive is used to declare that the contents of a given XML tag are to be treated as a JSON document and stored into a Sphinx index for later use. Refer to [the section called “sql_attr_json”](../../data_source_configuration_options/sqlattr_json.md) for more details on the JSON attributes.

#### Example: {#example}

```

xmlpipe_attr_json = properties

```