### json_autoconv_keynames {#json-autoconv-keynames}

Whether and how to auto-convert key names within JSON attributes. Known value is &#039;lowercase&#039;. Optional, default value is unspecified (do not convert anything). Added in 2.1.1-beta.

When this directive is set to &#039;lowercase&#039;, key names within JSON attributes will be automatically brought to lower case when indexing. This conversion applies to any data source, that is, JSON attributes originating from either SQL or XMLpipe2 sources will all be affected.

#### Example: {#example}

```

json_autoconv_keynames = lowercase

```