## tsvpipe\csvpipe (Tab\Comma Separated Values) data source {#tsvpipe-csvpipe-tab-comma-separated-values-data-source}

This is the simplest way to pass data to the indexer. It was created due to xmlpipe2 limitations. Namely, indexer must map each attribute and field tag in XML file to corresponding schema element. This mapping requires some time. And time increases with increasing the number of fields and attributes in schema. There is no such issue in tsvpipe because each field and attribute is a particular column in TSV file. So, in some cases tsvpipe could work slightly faster than xmlpipe2\. Added in 2.2.1-beta.

The first column in TSV\CSV file must be a document ID. The rest ones must mirror the declaration of fields and attributes in schema definition.

The difference between tsvpipe and csvpipe is delimiter and quoting rules. tsvpipe has tab character as hardcoded delimiter and has no quoting rules. csvpipe has option [csvpipe_delimiter](../data_source_configuration_options/csvpipedelimiter.md) for delimiter with default value &#039;,&#039; and also has quoting rules, such as:

*   any field may be quoted

*   fields containing a line-break, double-quote or commas should be quoted

*   a double quote character in a field must be represented by two double quote characters

tsvpipe and csvpipe have same field and attrribute declaration derectives as xmlpipe.

tsvpipe declarations:

[tsvpipe_command](../data_source_configuration_options/xmlpipecommand.md), [tsvpipe_field](../data_source_configuration_options/xmlpipefield.md), [tsvpipe_field_string](../data_source_configuration_options/xmlpipefield_string.md), [tsvpipe_attr_uint](../data_source_configuration_options/xmlpipeattr_uint.md), [tsvpipe_attr_timestamp](../data_source_configuration_options/xmlpipeattr_timestamp.md), [tsvpipe_attr_bool](../data_source_configuration_options/xmlpipeattr_bool.md), [tsvpipe_attr_float](../data_source_configuration_options/xmlpipeattr_float.md), [tsvpipe_attr_bigint](../data_source_configuration_options/xmlpipeattr_bigint.md), [tsvpipe_attr_multi](../data_source_configuration_options/xmlpipeattr_multi.md), [tsvpipe_attr_multi_64](../data_source_configuration_options/xmlpipeattr_multi_64.md), [tsvpipe_attr_string](../data_source_configuration_options/xmlpipeattr_string.md), [tsvpipe_attr_json](../data_source_configuration_options/xmlpipeattr_json.md)

csvpipe declarations:

[csvpipe_command](../data_source_configuration_options/xmlpipecommand.md), [csvpipe_field](../data_source_configuration_options/xmlpipefield.md), [csvpipe_field_string](../data_source_configuration_options/xmlpipefield_string.md), [csvpipe_attr_uint](../data_source_configuration_options/xmlpipeattr_uint.md), [csvpipe_attr_timestamp](../data_source_configuration_options/xmlpipeattr_timestamp.md), [csvpipe_attr_bool](../data_source_configuration_options/xmlpipeattr_bool.md), [csvpipe_attr_float](../data_source_configuration_options/xmlpipeattr_float.md), [csvpipe_attr_bigint](../data_source_configuration_options/xmlpipeattr_bigint.md), [csvpipe_attr_multi](../data_source_configuration_options/xmlpipeattr_multi.md), [csvpipe_attr_multi_64](../data_source_configuration_options/xmlpipeattr_multi_64.md), [csvpipe_attr_string](../data_source_configuration_options/xmlpipeattr_string.md), [csvpipe_attr_json](../data_source_configuration_options/xmlpipeattr_json.md)

```

source tsv_test
{
	type = tsvpipe
	tsvpipe_command = cat /tmp/rock_bands.tsv
	tsvpipe_field = name
	tsvpipe_attr_multi = genre_tags
}

```

```

1	Led Zeppelin	35,23,16
2	Deep Purple	35,92
3	Frank Zappa	35,23,16,92,33,24

```