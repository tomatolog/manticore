### mysql_ssl_cert, mysql_ssl_key, mysql_ssl_ca {#mysql-ssl-cert-mysql-ssl-key-mysql-ssl-ca}

SSL certificate settings to use for connecting to MySQL server. Optional, default values are empty strings (do not use SSL). Applies to `mysql` source type only.

These directives let you set up secure SSL connection between `indexer` and MySQL. The details on creating the certificates and setting up MySQL server can be found in MySQL documentation.

#### Example: {#example}

```

mysql_ssl_cert = /etc/ssl/client-cert.pem
mysql_ssl_key = /etc/ssl/client-key.pem
mysql_ssl_ca = /etc/ssl/cacert.pem

```