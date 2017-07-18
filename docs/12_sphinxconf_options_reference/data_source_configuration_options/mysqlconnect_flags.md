### mysql_connect_flags {#mysql-connect-flags}

MySQL client connection flags. Optional, default value is 0 (do not set any flags). Applies to `mysql` source type only.

This option must contain an integer value with the sum of the flags. The value will be passed to [mysql_real_connect()](http://dev.mysql.com/doc/refman/5.0/en/mysql-real-connect.html) verbatim. The flags are enumerated in mysql_com.h include file. Flags that are especially interesting in regard to indexing, with their respective values, are as follows:

*   CLIENT_COMPRESS = 32; can use compression protocol

*   CLIENT_SSL = 2048; switch to SSL after handshake

*   CLIENT_SECURE_CONNECTION = 32768; new 4.1 authentication

For instance, you can specify 2080 (2048+32) to use both compression and SSL, or 32768 to use new authentication only. Initially, this option was introduced to be able to use compression when the `indexer` and `mysqld` are on different hosts. Compression on 1 Gbps links is most likely to hurt indexing time though it reduces network traffic, both in theory and in practice. However, enabling compression on 100 Mbps links may improve indexing time significantly (upto 20-30% of the total indexing time improvement was reported). Your mileage may vary.

#### Example: {#example}

```

mysql_connect_flags = 32 # enable compression

```