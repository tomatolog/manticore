odbc\_dsn
~~~~~~~~~

ODBC DSN to connect to. Mandatory, no default value. Applies to ``odbc``
source type only.

ODBC DSN (Data Source Name) specifies the credentials (host, user,
password, etc) to use when connecting to ODBC data source. The format
depends on specific ODBC driver used.

Example:
^^^^^^^^

::


    odbc_dsn = Driver={Oracle ODBC Driver};Dbq=myDBName;Uid=myUsername;Pwd=myPassword

