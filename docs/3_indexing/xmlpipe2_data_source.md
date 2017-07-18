## xmlpipe2 data source {#xmlpipe2-data-source}

xmlpipe2 lets you pass arbitrary full-text and attribute data to Sphinx in yet another custom XML format. It also allows to specify the schema (ie. the set of fields and attributes) either in the XML stream itself, or in the source settings.

When indexing xmlpipe2 source, indexer runs the given command, opens a pipe to its stdout, and expects well-formed XML stream. Here&#039;s sample stream data:

###### Example 3.2. xmlpipe2 document stream {#example-3-2-xmlpipe2-document-stream}

```

<?xml version="1.0" encoding="utf-8"?>
<sphinx:docset>

<sphinx:schema>
<sphinx:field name="subject"/>
<sphinx:field name="content"/>
<sphinx:attr name="published" type="timestamp"/>
<sphinx:attr name="author_id" type="int" bits="16" default="1"/>
</sphinx:schema>

<sphinx:document id="1234">
<content>this is the main content <![CDATA[[and this <cdata> entry
must be handled properly by xml parser lib]]></content>
<published>1012325463</published>
<subject>note how field/attr tags can be
in <b class="red">randomized</b> order</subject>
<misc>some undeclared element</misc>
</sphinx:document>

<sphinx:document id="1235">
<subject>another subject</subject>
<content>here comes another document, and i am given to understand,
that in-document field order must not matter, sir</content>
<published>1012325467</published>
</sphinx:document>

<!-- ... even more sphinx:document entries here ... -->

<sphinx:killlist>
<id>1234</id>
<id>4567</id>
</sphinx:killlist>

</sphinx:docset>

```

Arbitrary fields and attributes are allowed. They also can occur in the stream in arbitrary order within each document; the order is ignored. There is a restriction on maximum field length; fields longer than 2 MB will be truncated to 2 MB (this limit can be changed in the source).

The schema, ie. complete fields and attributes list, must be declared before any document could be parsed. This can be done either in the configuration file using `xmlpipe_field` and `xmlpipe_attr_XXX` settings, or right in the stream using &lt;sphinx:schema&gt; element. &lt;sphinx:schema&gt; is optional. It is only allowed to occur as the very first sub-element in &lt;sphinx:docset&gt;. If there is no in-stream schema definition, settings from the configuration file will be used. Otherwise, stream settings take precedence.

Unknown tags (which were not declared neither as fields nor as attributes) will be ignored with a warning. In the example above, &lt;misc&gt; will be ignored. All embedded tags and their attributes (such as &lt;b&gt; in &lt;subject&gt; in the example above) will be silently ignored.

Support for incoming stream encodings depends on whether `iconv` is installed on the system. xmlpipe2 is parsed using `libexpat` parser that understands US-ASCII, ISO-8859-1, UTF-8 and a few UTF-16 variants natively. Sphinx `configure` script will also check for `libiconv` presence, and utilize it to handle other encodings. `libexpat` also enforces the requirement to use UTF-8 charset on Sphinx side, because the parsed data it returns is always in UTF-8.

XML elements (tags) recognized by xmlpipe2 (and their attributes where applicable) are:

*   sphinx:docset
*   Mandatory top-level element, denotes and contains xmlpipe2 document set.

*   sphinx:schema
*   Optional element, must either occur as the very first child of sphinx:docset, or never occur at all. Declares the document schema. Contains field and attribute declarations. If present, overrides per-source settings from the configuration file.

*   sphinx:field
*   Optional element, child of sphinx:schema. Declares a full-text field. Known attributes are:

    *   &quot;name&quot;, specifies the XML element name that will be treated as a full-text field in the subsequent documents.

    *   &quot;attr&quot;, specifies whether to also index this field as a string. Possible value is &quot;string&quot;. Introduced in version 1.10-beta.

*   sphinx:attr
*   Optional element, child of sphinx:schema. Declares an attribute. Known attributes are:

    *   &quot;name&quot;, specifies the element name that should be treated as an attribute in the subsequent documents.

    *   &quot;type&quot;, specifies the attribute type. Possible values are &quot;int&quot;, &quot;bigint&quot;, &quot;timestamp&quot;, &quot;bool&quot;, &quot;float&quot;, &quot;multi&quot; and &quot;json&quot;.

    *   &quot;bits&quot;, specifies the bit size for &quot;int&quot; attribute type. Valid values are 1 to 32.

    *   &quot;default&quot;, specifies the default value for this attribute that should be used if the attribute&#039;s element is not present in the document.

*   sphinx:document
*   Mandatory element, must be a child of sphinx:docset. Contains arbitrary other elements with field and attribute values to be indexed, as declared either using sphinx:field and sphinx:attr elements or in the configuration file. The only known attribute is &quot;id&quot; that must contain the unique integer document ID.

*   sphinx:killlist
*   Optional element, child of sphinx:docset. Contains a number of &quot;id&quot; elements whose contents are document IDs to be put into a [kill-list](../data_source_configuration_options/sqlquery_killlist.md) for this index.