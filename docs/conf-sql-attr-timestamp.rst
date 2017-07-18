.. raw:: html

   <div class="navheader">

12.1.20. sql\_attr\_timestamp
`Prev <conf-sql-attr-bigint.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-attr-float.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.1.20. sql\_attr\_timestamp
   :name: sql_attr_timestamp
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

UNIX timestamp `attribute <attributes.html>`__ declaration. Multi-value
(there might be multiple attributes declared), optional. Applies to SQL
source types (``mysql``, ``pgsql``, ``mssql``) only.

Timestamps can store date and time in the range of Jan 01, 1970 to Jan
19, 2038 with a precision of one second. The expected column value
should be a timestamp in UNIX format, ie. 32-bit unsigned integer number
of seconds elapsed since midnight, January 01, 1970, GMT. Timestamps are
internally stored and handled as integers everywhere. But in addition to
working with timestamps as integers, it’s also legal to use them along
with different date-based functions, such as time segments sorting mode,
or day/week/month/year extraction for GROUP BY.

Note that DATE or DATETIME column types in MySQL can **not** be directly
used as timestamp attributes in Sphinx; you need to explicitly convert
such columns using UNIX\_TIMESTAMP function (if data is in range).

Note timestamps can not represent dates before January 01, 1970, and
UNIX\_TIMESTAMP() in MySQL will not return anything expected. If you
only needs to work with dates, not times, consider TO\_DAYS() function
in MySQL instead.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    # sql_query = ... UNIX_TIMESTAMP(added_datetime) AS added_ts ...
    sql_attr_timestamp = added_ts

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+----------------------------------+----------------------------------------+
| `Prev <conf-sql-attr-bigint.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-attr-float.html>`__   |
+-----------------------------------------+----------------------------------+----------------------------------------+
| 12.1.19. sql\_attr\_bigint              | `Home <index.html>`__            |  12.1.21. sql\_attr\_float             |
+-----------------------------------------+----------------------------------+----------------------------------------+

.. raw:: html

   </div>
