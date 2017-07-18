### stopwords {#stopwords}

Stopword files list (space separated). Optional, default is empty.

Stopwords are the words that will not be indexed. Typically you&#039;d put most frequent words in the stopwords list because they do not add much value to search results but consume a lot of resources to process.

You can specify several file names, separated by spaces. All the files will be loaded. Stopwords file format is simple plain text. The encoding must be UTF-8. File data will be tokenized with respect to [charset_table](../../index_configuration_options/charsettable.md) settings, so you can use the same separators as in the indexed data.

The [stemmers](../../index_configuration_options/morphology.md) will normally be applied when parsing stopwords file. That might however lead to undesired results. Starting with 2.1.1-beta, you can turn that off with [stopwords_unstemmed](../../index_configuration_options/stopwordsunstemmed.md).

Starting with version 2.1.1-beta small enough files are stored in the index header, see [the section called “embedded_limit”](../../index_configuration_options/embeddedlimit.md) for details.

While stopwords are not indexed, they still do affect the keyword positions. For instance, assume that &quot;the&quot; is a stopword, that document 1 contains the line &quot;in office&quot;, and that document 2 contains &quot;in the office&quot;. Searching for &quot;in office&quot; as for exact phrase will only return the first document, as expected, even though &quot;the&quot; in the second one is stopped. That behavior can be tweaked through the [stopword_step](../../index_configuration_options/stopwordstep.md) directive.

Stopwords files can either be created manually, or semi-automatically. `indexer` provides a mode that creates a frequency dictionary of the index, sorted by the keyword frequency, see `--buildstops` and `--buildfreqs` switch in [the section called “`indexer` command reference”](../../indexer_command_reference.md). Top keywords from that dictionary can usually be used as stopwords.

#### Example: {#example}

```

stopwords = /usr/local/sphinx/data/stopwords.txt
stopwords = stopwords-ru.txt stopwords-en.txt

```