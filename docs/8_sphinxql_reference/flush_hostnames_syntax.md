## FLUSH HOSTNAMES syntax {#flush-hostnames-syntax}

```

FLUSH HOSTNAMES

```

Added in 2.3.2-beta. Renew IPs associates to agent host names. To always query the DNS for getting the host name IP, see [hostname_lookup](../searchd_program_configuration_options/hostnamelookup.md) directive.

```

mysql> FLUSH HOSTNAMES;
Query OK, 5 rows affected (0.01 sec)

```