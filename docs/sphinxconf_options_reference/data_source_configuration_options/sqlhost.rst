sql\_host
~~~~~~~~~

SQL server host to connect to. Mandatory, no default value. Applies to
SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

In the simplest case when Manticore resides on the same host with your
MySQL or PostgreSQL installation, you would simply specify “localhost”.
Note that MySQL client library chooses whether to connect over TCP/IP or
over UNIX socket based on the host name. Specifically “localhost” will
force it to use UNIX socket (this is the default and generally
recommended mode) and “127.0.0.1” will force TCP/IP usage. Refer to
`MySQL
manual <http://dev.mysql.com/doc/refman/5.0/en/mysql-real-connect.html>`__
for more details.

Example:
^^^^^^^^

::


    sql_host = localhost

