.. raw:: html

   <div class="navheader">

3.10. tsvpipe\\csvpipe (Tab\\Comma Separated Values) data source
`Prev <xmlpipe2.html>`__ 
Chapter 3. Indexing
 `Next <live-updates.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 3.10. tsvpipe\\csvpipe (Tab\\Comma Separated Values) data
   source
   :name: tsvpipecsvpipe-tabcomma-separated-values-data-source
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

This is the simplest way to pass data to the indexer. It was created due
to xmlpipe2 limitations. Namely, indexer must map each attribute and
field tag in XML file to corresponding schema element. This mapping
requires some time. And time increases with increasing the number of
fields and attributes in schema. There is no such issue in tsvpipe
because each field and attribute is a particular column in TSV file. So,
in some cases tsvpipe could work slightly faster than xmlpipe2. Added in
2.2.1-beta.

The first column in TSV\\CSV file must be a document ID. The rest ones
must mirror the declaration of fields and attributes in schema
definition.

The difference between tsvpipe and csvpipe is delimiter and quoting
rules. tsvpipe has tab character as hardcoded delimiter and has no
quoting rules. csvpipe has option
`csvpipe\_delimiter <conf-csvpipe-delimiter.html>`__ for delimiter with
default value ‘,’ and also has quoting rules, such as:

.. raw:: html

   <div class="itemizedlist">

-  any field may be quoted

-  fields containing a line-break, double-quote or commas should be
   quoted

-  a double quote character in a field must be represented by two double
   quote characters

.. raw:: html

   </div>

tsvpipe and csvpipe have same field and attrribute declaration
derectives as xmlpipe.

tsvpipe declarations:

`tsvpipe\_command <conf-xmlpipe-command.html>`__,
`tsvpipe\_field <conf-xmlpipe-field.html>`__,
`tsvpipe\_field\_string <conf-xmlpipe-field-string.html>`__,
`tsvpipe\_attr\_uint <conf-xmlpipe-attr-uint.html>`__,
`tsvpipe\_attr\_timestamp <conf-xmlpipe-attr-timestamp.html>`__,
`tsvpipe\_attr\_bool <conf-xmlpipe-attr-bool.html>`__,
`tsvpipe\_attr\_float <conf-xmlpipe-attr-float.html>`__,
`tsvpipe\_attr\_bigint <conf-xmlpipe-attr-bigint.html>`__,
`tsvpipe\_attr\_multi <conf-xmlpipe-attr-multi.html>`__,
`tsvpipe\_attr\_multi\_64 <conf-xmlpipe-attr-multi-64.html>`__,
`tsvpipe\_attr\_string <conf-xmlpipe-attr-string.html>`__,
`tsvpipe\_attr\_json <conf-xmlpipe-attr-json.html>`__

csvpipe declarations:

`csvpipe\_command <conf-xmlpipe-command.html>`__,
`csvpipe\_field <conf-xmlpipe-field.html>`__,
`csvpipe\_field\_string <conf-xmlpipe-field-string.html>`__,
`csvpipe\_attr\_uint <conf-xmlpipe-attr-uint.html>`__,
`csvpipe\_attr\_timestamp <conf-xmlpipe-attr-timestamp.html>`__,
`csvpipe\_attr\_bool <conf-xmlpipe-attr-bool.html>`__,
`csvpipe\_attr\_float <conf-xmlpipe-attr-float.html>`__,
`csvpipe\_attr\_bigint <conf-xmlpipe-attr-bigint.html>`__,
`csvpipe\_attr\_multi <conf-xmlpipe-attr-multi.html>`__,
`csvpipe\_attr\_multi\_64 <conf-xmlpipe-attr-multi-64.html>`__,
`csvpipe\_attr\_string <conf-xmlpipe-attr-string.html>`__,
`csvpipe\_attr\_json <conf-xmlpipe-attr-json.html>`__

.. code:: programlisting

    source tsv_test
    {
        type = tsvpipe
        tsvpipe_command = cat /tmp/rock_bands.tsv
        tsvpipe_field = name
        tsvpipe_attr_multi = genre_tags
    }

.. code:: programlisting

    1   Led Zeppelin    35,23,16
    2   Deep Purple 35,92
    3   Frank Zappa 35,23,16,92,33,24

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------+--------------------------+---------------------------------+
| `Prev <xmlpipe2.html>`__     | `Up <indexing.html>`__   |  `Next <live-updates.html>`__   |
+------------------------------+--------------------------+---------------------------------+
| 3.9. xmlpipe2 data source    | `Home <index.html>`__    |  3.11. Live index updates       |
+------------------------------+--------------------------+---------------------------------+

.. raw:: html

   </div>
