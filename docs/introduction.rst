Introduction
=============================

About
-----

Manticore is a full-text search engine, publicly distributed under GPL
version 2. Commercial licensing (eg. for embedded use) is available upon
request.

Technically, Manticore is a standalone software package provides fast and
relevant full-text search functionality to client applications. It was
specially designed to integrate well with SQL databases storing the
data, and to be easily accessed by scripting languages. However, Manticore
does not depend on nor require any specific database to function.

Applications can access Manticore search daemon (searchd) using any of the
three different access methods: a) via Manticore own implementation of
MySQL network protocol (using a small SQL subset called SphinxQL, this
is recommended way), b) via native search API (SphinxAPI) or c) via
MySQL server with a pluggable storage engine (ManticoreSE).

Official native SphinxAPI implementations for PHP, Perl, Python, Ruby
and Java are included within the distribution package. API is very
lightweight so porting it to a new language is known to take a few hours
or days. Third party API ports and plugins exist for Perl, C#, Haskell,
Ruby-on-Rails, and possibly other languages and frameworks.

Manticore supports two different indexing backends: “disk” index backend,
and “realtime” (RT) index backend. Disk indexes support online full-text
index rebuilds, but online updates can only be done on non-text
(attribute) data. RT indexes additionally allow for online full-text
index updates. Previous versions only supported disk indexes.

Data can be loaded into disk indexes using a so-called data source.
Built-in sources can fetch data directly from MySQL, PostgreSQL, MSSQL,
ODBC compliant database (Oracle, etc) or a pipe in TSV or a custom XML
format. Adding new data sources drivers (eg. to natively support other
DBMSes) is designed to be as easy as possible. RT indexes can only be
populated using SphinxQL.

As for the name, Manticore is an acronym which is officially decoded as SQL
Phrase Index. Yes, I know about CMU's Manticore project.


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


Where to get Manticore
-------------------

Manticore is available through its official Web site at
http://sphinxsearch.com/.

Currently, Manticore distribution tarball includes the following software:

-  ``indexer``: an utility which creates fulltext indexes;

-  ``searchd``: a daemon which enables external software (eg. Web
   applications) to search through fulltext indexes;

-  ``sphinxapi``: a set of searchd client API libraries for popular Web
   scripting languages (PHP, Python, Perl, Ruby).

-  ``spelldump``: a simple command-line tool to extract the items from
   an ``ispell`` or ``MySpell`` (as bundled with OpenOffice) format
   dictionary to help customize your index, for use with
   `wordforms <../index_configuration_options/wordforms.md>`__.

-  ``indextool``: an utility to dump miscellaneous debug information
   about the index

-  ``wordbreaker``: an utility to break down compound words into
   separate words

   
License
-------

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version. See COPYING file for details.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

Non-GPL licensing (for OEM/ISV embedded use) can also be arranged,
please `contact us <http://sphinxsearch.com/contacts.html>`__ to discuss
commercial licensing possibilities.

Credits
-------

Author
~~~~~~

Manticore initial author (and a benevolent dictator ever since):

-  Andrew Aksyonoff, http://shodan.ru

Team
~~~~

Past and present employees of Manticore Technologies Inc who should be
noted on their work on Manticore (in alphabetical order):

-  Adam Rice

-  Adrian Nuta

-  Alexander Klimenko

-  Alexey Dvoichenkov

-  Alexey Vinogradov

-  Anton Tsitlionok

-  Eugene Kosov

-  Gloria Vinogradova

-  Ilya Kuznetsov

-  Kirill Shmatov

-  Rich Kelm

-  Stanislav Klinov

-  Steven Barker

-  Vladimir Fedorkov

-  Yuri Schapov

Contributors
~~~~~~~~~~~~

People who contributed to Manticore and their contributions (in no
particular order):

-  Robert “coredev” Bengtsson (Sweden), initial version of PostgreSQL
   data source

-  Len Kranendonk, Perl API

-  Dmytro Shteflyuk, Ruby API

Many other people have contributed ideas, bug reports, fixes, etc. Thank
you!

History
-------

Manticore development was started back in 2001, because I didn't manage to
find an acceptable search solution (for a database driven Web site)
which would meet my requirements. Actually, each and every important
aspect was a problem:

-  search quality (ie. good relevance)

   -  statistical ranking methods performed rather bad, especially on
      large collections of small documents (forums, blogs, etc)

-  search speed

   -  especially if searching for phrases which contain stopwords, as in
      “to be or not to be”

-  moderate disk and CPU requirements when indexing

   -  important in shared hosting environment, not to mention the
      indexing speed.

Despite the amount of time passed and numerous improvements made in the
other solutions, there's still no solution which I personally would be
eager to migrate to.

Considering that and a lot of positive feedback received from Manticore
users during last years, the obvious decision is to continue developing
Manticore (and, eventually, to take over the world).

