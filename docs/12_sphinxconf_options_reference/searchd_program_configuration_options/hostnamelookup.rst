hostname\_lookup
~~~~~~~~~~~~~~~~

Hostnames renew strategy. By default, IP addresses of agent host names
are cached at daemon start to avoid extra flood to DNS. In some cases
the IP can change dynamically (e.g. cloud hosting) and it might be
desired to don't cache the IPs. Setting this option to ‘request’
disabled the caching and queries the DNS at each query. The IP addresses
can also be manually renewed with FLUSH HOSTNAMES command.
