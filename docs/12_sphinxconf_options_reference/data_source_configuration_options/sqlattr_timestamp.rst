sql\_attr\_timestamp
~~~~~~~~~~~~~~~~~~~~

UNIX timestamp `attribute <../../attributes.html>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

Timestamps can store date and time in the range of Jan 01, 1970 to Jan
19, 2038 with a precision of one second. The expected column value
should be a timestamp in UNIX format, ie. 32-bit unsigned integer number
of seconds elapsed since midnight, January 01, 1970, GMT. Timestamps are
internally stored and handled as integers everywhere. But in addition to
working with timestamps as integers, it's also legal to use them along
with different date-based functions, such as time segments sorting mode,
or day/week/month/year extraction for GROUP BY.

Note that DATE or DATETIME column types in MySQL can <b>not</b> be
directly used as timestamp attributes in Sphinx; you need to explicitly
convert such columns using UNIX\_TIMESTAMP function (if data is in
range).

Note timestamps can not represent dates before January 01, 1970, and
UNIX\_TIMESTAMP() in MySQL will not return anything expected. If you
only needs to work with dates, not times, consider TO\_DAYS() function
in MySQL instead.

Example:
^^^^^^^^

::


    # sql_query = ... UNIX_TIMESTAMP(added_datetime) AS added_ts ...
    sql_attr_timestamp = added_ts

