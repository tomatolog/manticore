Manticore features
---------------

Key Manticore features are:

-  high indexing and searching performance;

-  advanced indexing and querying tools (flexible and feature-rich text
   tokenizer, querying language, several different ranking modes, etc);

-  advanced result set post-processing (SELECT with expressions, WHERE,
   ORDER BY, GROUP BY, HAVING etc over text search results);

-  proven scalability up to billions of documents, terabytes of data,
   and thousands of queries per second;

-  easy integration with SQL and XML data sources, and SphinxQL,
   SphinxAPI, or ManticoreSE search interfaces;

-  easy scaling with distributed searches.

To expand a bit, Manticore:

-  has high indexing speed (upto 10-15 MB/sec per core on an internal
   benchmark);

-  has high search speed (upto 150-250 queries/sec per core against
   1,000,000 documents, 1.2 GB of data on an internal benchmark);

-  has high scalability (biggest known cluster indexes over
   3,000,000,000 documents, and busiest one peaks over 50,000,000
   queries/day);

-  provides good relevance ranking through combination of phrase
   proximity ranking and statistical (BM25) ranking;

-  provides distributed searching capabilities;

-  provides document excerpts (snippets) generation;

-  provides searching from within application with SphinxQL or SphinxAPI
   interfaces, and from within MySQL with pluggable ManticoreSE storage
   engine;

-  supports boolean, phrase, word proximity and other types of queries;

-  supports multiple full-text fields per document (upto 32 by default);

-  supports multiple additional attributes per document (ie. groups,
   timestamps, etc);

-  supports stopwords;

-  supports morphological word forms dictionaries;

-  supports tokenizing exceptions;

-  supports UTF-8 encoding;

-  supports stemming (stemmers for English, Russian, Czech and Arabic
   are built-in; and stemmers for French, Spanish, Portuguese, Italian,
   Romanian, German, Dutch, Swedish, Norwegian, Danish, Finnish,
   Hungarian, are available by building third party `libstemmer
   library <http://snowball.tartarus.org/>`__);

-  supports MySQL natively (all types of tables, including MyISAM,
   InnoDB, NDB, Archive, etc are supported);

-  supports PostgreSQL natively;

-  supports ODBC compliant databases (MS SQL, Oracle, etc) natively;

-  …has 50+ other features not listed here, refer configuration manual!
