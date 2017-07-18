### html_index_attrs {#html-index-attrs}

A list of markup attributes to index when stripping HTML. Optional, default is empty (do not index markup attributes).

Specifies HTML markup attributes whose contents should be retained and indexed even though other HTML markup is stripped. The format is per-tag enumeration of indexable attributes, as shown in the example below.

#### Example: {#example}

```

html_index_attrs = img=alt,title; a=title;

```