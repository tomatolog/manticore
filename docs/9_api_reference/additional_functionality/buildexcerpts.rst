BuildExcerpts
~~~~~~~~~~~~~

<b>Prototype:</b> function BuildExcerpts ( $docs, $index, $words,
$opts=array() )

Excerpts (snippets) builder function. Connects to ``searchd``, asks it
to generate excerpts (snippets) from given documents, and returns the
results.

``$docs`` is a plain array of strings that carry the documents'
contents. ``$index`` is an index name string. Different settings (such
as charset, morphology, wordforms) from given index will be used.
``$words`` is a string that contains the keywords to highlight. They
will be processed with respect to index settings. For instance, if
English stemming is enabled in the index, “shoes” will be highlighted
even if keyword is “shoe”. Starting with version 0.9.9-rc1, keywords can
contain wildcards, that work similarly to star-syntax available in
queries. ``$opts`` is a hash which contains additional optional
highlighting parameters:

-  “before\_match”:
-  A string to insert before a keyword match. Starting with version
   1.10-beta, a %PASSAGE\_ID% macro can be used in this string. The
   first match of the macro is replaced with an incrementing passage
   number within a current snippet. Numbering starts at 1 by default but
   can be overridden with “start\_passage\_id” option. In a
   multi-document call, %PASSAGE\_ID% would restart at every given
   document. Default is “<b>”.

-  “after\_match”:
-  A string to insert after a keyword match. Starting with version
   1.10-beta, a %PASSAGE\_ID% macro can be used in this string. Default
   is “</b>”.

-  “chunk\_separator”:
-  A string to insert between snippet chunks (passages). Default is " …
   “.

-  “limit”:
-  Maximum snippet size, in symbols (codepoints). Integer, default is
   256.

-  “around”:
-  How much words to pick around each matching keywords block. Integer,
   default is 5.

-  “exact\_phrase”:
-  Whether to highlight exact query phrase matches only instead of
   individual keywords. Boolean, default is false.

-  “use\_boundaries”:
-  Whether to additionally break passages by phrase boundary characters,
   as configured in index settings with
   `phrase\_boundary <../../index_configuration_options/phraseboundary.rst>`__
   directive. Boolean, default is false.

-  “weight\_order”:
-  Whether to sort the extracted passages in order of relevance
   (decreasing weight), or in order of appearance in the document
   (increasing position). Boolean, default is false.

-  “query\_mode”:
-  Added in version 1.10-beta. Whether to handle $words as a query in
   `extended syntax <../../extended_query_syntax.rst>`__, or as a bag of
   words (default behavior). For instance, in query mode (“one two” \|
   “three four”) will only highlight and include those occurrences “one
   two” or “three four” when the two words from each pair are adjacent
   to each other. In default mode, any single occurrence of “one”,
   “two”, “three”, or “four” would be highlighted. Boolean, default is
   false.

-  “force\_all\_words”:
-  Added in version 1.10-beta. Ignores the snippet length limit until it
   includes all the keywords. Boolean, default is false.

-  “limit\_passages”:
-  Added in version 1.10-beta. Limits the maximum number of passages
   that can be included into the snippet. Integer, default is 0 (no
   limit).

-  “limit\_words”:
-  Added in version 1.10-beta. Limits the maximum number of words that
   can be included into the snippet. Note the limit applies to any
   words, and not just the matched keywords to highlight. For example,
   if we are highlighting “Mary” and a passage “Mary had a little lamb”
   is selected, then it contributes 5 words to this limit, not just 1.
   Integer, default is 0 (no limit).

-  “start\_passage\_id”:
-  Added in version 1.10-beta. Specifies the starting value of
   %PASSAGE\_ID% macro (that gets detected and expanded in
   ``before_match``, ``after_match`` strings). Integer, default is 1.

-  “load\_files”:
-  Added in version 1.10-beta. Whether to handle $docs as data to
   extract snippets from (default behavior), or to treat it as file
   names, and load data from specified files on the server side.
   Starting with version 2.0.1-beta, up to
   `dist\_threads <../../searchd_program_configuration_options/distthreads.rst>`__
   worker threads per request will be created to parallelize the work
   when this flag is enabled. Boolean, default is false. Starting with
   version 2.0.2-beta, building of the snippets could be parallelized
   between remote agents. Just set the
   `‘dist\_threads’ <../../searchd_program_configuration_options/distthreads.rst>`__
   param in the config to the value greater than 1, and then invoke the
   snippets generation over the distributed index, which contain only
   one(!) `local <../../index_configuration_options/local.rst>`__ agent
   and several remotes. Starting with version 2.1.1-beta, the
   `snippets\_file\_prefix <../../searchd_program_configuration_options/snippetsfile_prefix.rst>`__
   option is also in the game and the final filename is calculated by
   concatenation of the prefix with given name. Otherwords, when
   snippets\_file\_prefix is ‘/var/data’ and filename is ‘text.txt’ the
   sphinx will try to generate the snippets from the file
   ‘/var/datatext.txt’, which is exactly ‘/var/data’ + ‘text.txt’.

-  “load\_files\_scattered”:
-  Added in version 2.0.2-beta. It works only with distributed snippets
   generation with remote agents. The source files for snippets could be
   distributed among different agents, and the main daemon will merge
   together all non-erroneous results. So, if one agent of the
   distributed index has ‘file1.txt’, another has ‘file2.txt’ and you
   call for the snippets with both these files, the sphinx will merge
   results from the agents together, so you will get the snippets from
   both ‘file1.txt’ and ‘file2.txt’. Boolean, default is false.

   If the “load\_files” is also set, the request will return the error
   in case if any of the files is not available anywhere. Otherwise (if
   “load\_files” is not set) it will just return the empty strings for
   all absent files. The master instance reset this flag when
   distributes the snippets among agents. So, for agents the absence of
   a file is not critical error, but for the master it might be so. If
   you want to be sure that all snippets are actually created, set both
   “load\_files\_scattered” and “load\_files”. If the absence of some
   snippets caused by some agents is not critical for you - set just
   “load\_files\_scattered”, leaving “load\_files” not set.

-  “html\_strip\_mode”:
-  Added in version 1.10-beta. HTML stripping mode setting. Defaults to
   “index”, which means that index settings will be used. The other
   values are “none” and “strip”, that forcibly skip or apply stripping
   irregardless of index settings; and “retain”, that retains HTML
   markup and protects it from highlighting. The “retain” mode can only
   be used when highlighting full documents and thus requires that no
   snippet size limits are set. String, allowed values are “none”,
   “strip”, “index”, and “retain”.

-  “allow\_empty”:
-  Added in version 1.10-beta. Allows empty string to be returned as
   highlighting result when a snippet could not be generated (no
   keywords match, or no passages fit the limit). By default, the
   beginning of original text would be returned instead of an empty
   string. Boolean, default is false.

-  “passage\_boundary”:
-  Added in version 2.0.1-beta. Ensures that passages do not cross a
   sentence, paragraph, or zone boundary (when used with an index that
   has the respective indexing settings enabled). String, allowed values
   are “sentence”, “paragraph”, and “zone”.

-  “emit\_zones”:
-  Added in version 2.0.1-beta. Emits an HTML tag with an enclosing zone
   name before each passage. Boolean, default is false.

Snippets extraction algorithm currently favors better passages (with
closer phrase matches), and then passages with keywords not yet in
snippet. Generally, it will try to highlight the best match with the
query, and it will also to highlight all the query keywords, as made
possible by the limits. In case the document does not match the query,
beginning of the document trimmed down according to the limits will be
return by default. Starting with 1.10-beta, you can also return an empty
snippet instead case by setting “allow\_empty” option to true.

Returns false on failure. Returns a plain array of strings with excerpts
(snippets) on success.
