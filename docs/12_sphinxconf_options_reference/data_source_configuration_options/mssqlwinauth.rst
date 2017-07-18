mssql\_winauth
~~~~~~~~~~~~~~

MS SQL Windows authentication flag. Boolean, optional, default value is
0 (false). Applies to ``mssql`` source type only. Introduced in version
0.9.9-rc1.

Whether to use currently logged in Windows account credentials for
authentication when connecting to MS SQL Server. Note that when running
``searchd`` as a service, account user can differ from the account you
used to install the service.

Example:
^^^^^^^^

::


    mssql_winauth = 1

