mysql\_ssl\_cert, mysql\_ssl\_key, mysql\_ssl\_ca
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SSL certificate settings to use for connecting to MySQL server.
Optional, default values are empty strings (do not use SSL). Applies to
``mysql`` source type only.

These directives let you set up secure SSL connection between
``indexer`` and MySQL. The details on creating the certificates and
setting up MySQL server can be found in MySQL documentation.

Example:
^^^^^^^^

::


    mysql_ssl_cert = /etc/ssl/client-cert.pem
    mysql_ssl_key = /etc/ssl/client-key.pem
    mysql_ssl_ca = /etc/ssl/cacert.pem

