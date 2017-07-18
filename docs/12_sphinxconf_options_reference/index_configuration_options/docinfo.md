### docinfo {#docinfo}

Document attribute values (docinfo) storage mode. Optional, default is &#039;extern&#039;. Known values are &#039;none&#039;, &#039;extern&#039; and &#039;inline&#039;.

Docinfo storage mode defines how exactly docinfo will be physically stored on disk and RAM. &quot;none&quot; means that there will be no docinfo at all (ie. no attributes). Normally you need not to set &quot;none&quot; explicitly because Sphinx will automatically select &quot;none&quot; when there are no attributes configured. &quot;inline&quot; means that the docinfo will be stored in the `.spd` file, along with the document ID lists. &quot;extern&quot; means that the docinfo will be stored separately (externally) from document ID lists, in a special `.spa` file.

Basically, externally stored docinfo must be kept in RAM when querying. for performance reasons. So in some cases &quot;inline&quot; might be the only option. However, such cases are infrequent, and docinfo defaults to &quot;extern&quot;. Refer to [the section called “Attributes”](../../attributes.md) for in-depth discussion and RAM usage estimates.

#### Example: {#example}

```

docinfo = inline

```