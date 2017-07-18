tsvpipe:raw-latex:`\csvpipe `(Tab:raw-latex:`\Comma `Separated Values) data source
----------------------------------------------------------------------------------

This is the simplest way to pass data to the indexer. It was created due
to xmlpipe2 limitations. Namely, indexer must map each attribute and
field tag in XML file to corresponding schema element. This mapping
requires some time. And time increases with increasing the number of
fields and attributes in schema. There is no such issue in tsvpipe
because each field and attribute is a particular column in TSV file. So,
in some cases tsvpipe could work slightly faster than xmlpipe2. Added in
2.2.1-beta.

The first column in TSV:raw-latex:`\CSV `file must be a document ID. The
rest ones must mirror the declaration of fields and attributes in schema
definition.

The difference between tsvpipe and csvpipe is delimiter and quoting
rules. tsvpipe has tab character as hardcoded delimiter and has no
quoting rules. csvpipe has option
`csvpipe\_delimiter <../data_source_configuration_options/csvpipedelimiter.rst>`__
for delimiter with default value ‘,’ and also has quoting rules, such
as:

-  any field may be quoted

-  fields containing a line-break, double-quote or commas should be
   quoted

-  a double quote character in a field must be represented by two double
   quote characters

tsvpipe and csvpipe have same field and attrribute declaration
derectives as xmlpipe.

tsvpipe declarations:

`tsvpipe\_command <../data_source_configuration_options/xmlpipecommand.rst>`__,
`tsvpipe\_field <../data_source_configuration_options/xmlpipefield.rst>`__,
`tsvpipe\_field\_string <../data_source_configuration_options/xmlpipefield_string.rst>`__,
`tsvpipe\_attr\_uint <../data_source_configuration_options/xmlpipeattr_uint.rst>`__,
`tsvpipe\_attr\_timestamp <../data_source_configuration_options/xmlpipeattr_timestamp.rst>`__,
`tsvpipe\_attr\_bool <../data_source_configuration_options/xmlpipeattr_bool.rst>`__,
`tsvpipe\_attr\_float <../data_source_configuration_options/xmlpipeattr_float.rst>`__,
`tsvpipe\_attr\_bigint <../data_source_configuration_options/xmlpipeattr_bigint.rst>`__,
`tsvpipe\_attr\_multi <../data_source_configuration_options/xmlpipeattr_multi.rst>`__,
`tsvpipe\_attr\_multi\_64 <../data_source_configuration_options/xmlpipeattr_multi_64.rst>`__,
`tsvpipe\_attr\_string <../data_source_configuration_options/xmlpipeattr_string.rst>`__,
`tsvpipe\_attr\_json <../data_source_configuration_options/xmlpipeattr_json.rst>`__

csvpipe declarations:

`csvpipe\_command <../data_source_configuration_options/xmlpipecommand.rst>`__,
`csvpipe\_field <../data_source_configuration_options/xmlpipefield.rst>`__,
`csvpipe\_field\_string <../data_source_configuration_options/xmlpipefield_string.rst>`__,
`csvpipe\_attr\_uint <../data_source_configuration_options/xmlpipeattr_uint.rst>`__,
`csvpipe\_attr\_timestamp <../data_source_configuration_options/xmlpipeattr_timestamp.rst>`__,
`csvpipe\_attr\_bool <../data_source_configuration_options/xmlpipeattr_bool.rst>`__,
`csvpipe\_attr\_float <../data_source_configuration_options/xmlpipeattr_float.rst>`__,
`csvpipe\_attr\_bigint <../data_source_configuration_options/xmlpipeattr_bigint.rst>`__,
`csvpipe\_attr\_multi <../data_source_configuration_options/xmlpipeattr_multi.rst>`__,
`csvpipe\_attr\_multi\_64 <../data_source_configuration_options/xmlpipeattr_multi_64.rst>`__,
`csvpipe\_attr\_string <../data_source_configuration_options/xmlpipeattr_string.rst>`__,
`csvpipe\_attr\_json <../data_source_configuration_options/xmlpipeattr_json.rst>`__

::


    source tsv_test
    {
        type = tsvpipe
        tsvpipe_command = cat /tmp/rock_bands.tsv
        tsvpipe_field = name
        tsvpipe_attr_multi = genre_tags
    }

::


    1   Led Zeppelin    35,23,16
    2   Deep Purple 35,92
    3   Frank Zappa 35,23,16,92,33,24

