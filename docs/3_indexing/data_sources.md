## Data sources {#data-sources}

The data to be indexed can generally come from very different sources: SQL databases, plain text files, HTML files, mailboxes, and so on. From Sphinx point of view, the data it indexes is a set of structured _documents_, each of which has the same set of _fields_ and _attributes_. This is similar to SQL, where each row would correspond to a document, and each column to either a field or an attribute.

Depending on what source Sphinx should get the data from, different code is required to fetch the data and prepare it for indexing. This code is called _data source driver_ (or simply _driver_ or _data source_ for brevity).

At the time of this writing, there are built-in drivers for MySQL, PostgreSQL, MS SQL (on Windows), and ODBC. There is also a generic driver called xmlpipe2, which runs a specified command and reads the data from its `stdout`. See [the section called “xmlpipe2 data source”](../xmlpipe2_data_source.md) section for the format description. In 2.2.1-beta a tsvpipe (Tab Separated Values) and csvpipe (Comma Separated Values) data source was added. You can get more information here [the section called “tsvpipe\csvpipe (Tab\Comma Separated Values) data source”](../tsvpipecsvpipe_tabcomma_separated_values_data_sour.md).

There can be as many sources per index as necessary. They will be sequentially processed in the very same order which was specified in index definition. All the documents coming from those sources will be merged as if they were coming from a single source.