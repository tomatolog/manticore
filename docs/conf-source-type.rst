.. raw:: html

   <div class="navheader">

12.1.1. type
`Prev <confgroup-source.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-host.html>`__

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

.. rubric:: 12.1.1. type
   :name: type
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Data source type. Mandatory, no default value. Known types are
``mysql``, ``pgsql``, ``mssql``, ``xmlpipe2``, ``tsvpipe``, ``csvpipe``
and ``odbc``.

All other per-source options depend on source type selected by this
option. Names of the options used for SQL sources (ie. MySQL,
PostgreSQL, MS SQL) start with “sql\_”; names of the ones used for
xmlpipe2 or tsvpipe, csvpipe start with “xmlpipe\_” and “tsvpipe\_”,
“csvpipe\_” correspondingly. All source types are conditional; they
might or might not be supported depending on your build settings,
installed client libraries, etc. ``mssql`` type is currently only
available on Windows. ``odbc`` type is available both on Windows
natively and on Linux through `UnixODBC
library <http://www.unixodbc.org/>`__.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    type = mysql

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+----------------------------------+
| `Prev <confgroup-source.html>`__           | `Up <confgroup-source.html>`__   |  `Next <conf-sql-host.html>`__   |
+--------------------------------------------+----------------------------------+----------------------------------+
| 12.1. Data source configuration options    | `Home <index.html>`__            |  12.1.2. sql\_host               |
+--------------------------------------------+----------------------------------+----------------------------------+

.. raw:: html

   </div>
