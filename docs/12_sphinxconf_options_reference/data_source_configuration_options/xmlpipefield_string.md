### xmlpipe_field_string {#xmlpipe-field-string}

xmlpipe field and string attribute declaration. Multi-value, optional. Applies to `xmlpipe2` source type only. Refer to [the section called “xmlpipe2 data source”](../../xmlpipe2_data_source.md). Introduced in version 1.10-beta.

Makes the specified XML element indexed as both a full-text field and a string attribute. Equivalent to &lt;sphinx:field name=&quot;field&quot; attr=&quot;string&quot;/&gt; declaration within the XML file.

#### Example: {#example}

```

xmlpipe_field_string = subject

```