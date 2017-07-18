### xmlpipe_attr_multi {#xmlpipe-attr-multi}

xmlpipe MVA attribute declaration. Multi-value, optional. Applies to `xmlpipe2` source type only.

This setting declares an MVA attribute tag in xmlpipe2 stream. The contents of the specified tag will be parsed and a list of integers that will constitute the MVA will be extracted, similar to how [sql_attr_multi](../../data_source_configuration_options/sqlattr_multi.md) parses SQL column contents when &#039;field&#039; MVA source type is specified.

#### Example: {#example}

```

xmlpipe_attr_multi = taglist

```