xmlpipe\_field\_string
~~~~~~~~~~~~~~~~~~~~~~

xmlpipe field and string attribute declaration. Multi-value, optional.
Applies to ``xmlpipe2`` source type only. Refer to `the section called
“xmlpipe2 data source” <../../xmlpipe2_data_source.html>`__. Introduced in
version 1.10-beta.

Makes the specified XML element indexed as both a full-text field and a
string attribute. Equivalent to <sphinx:field name=“field”
attr=“string”/> declaration within the XML file.

Example:
^^^^^^^^

::


    xmlpipe_field_string = subject

