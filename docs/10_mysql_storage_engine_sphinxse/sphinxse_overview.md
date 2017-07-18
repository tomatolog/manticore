## SphinxSE overview {#sphinxse-overview}

SphinxSE is MySQL storage engine which can be compiled into MySQL server 5.x using its pluggable architecture. It is not available for MySQL 4.x series. It also requires MySQL 5.0.22 or higher in 5.0.x series, or MySQL 5.1.12 or higher in 5.1.x series.

Despite the name, SphinxSE does _not_ actually store any data itself. It is actually a built-in client which allows MySQL server to talk to `searchd`, run search queries, and obtain search results. All indexing and searching happen outside MySQL.

Obvious SphinxSE applications include:

*   easier porting of MySQL FTS applications to Sphinx;

*   allowing Sphinx use with programming languages for which native APIs are not available yet;

*   optimizations when additional Sphinx result set processing on MySQL side is required (eg. JOINs with original document tables, additional MySQL-side filtering, etc).