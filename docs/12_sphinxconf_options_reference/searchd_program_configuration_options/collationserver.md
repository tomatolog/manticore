### collation_server {#collation-server}

Default server collation. Optional, default is libc_ci. Introduced in version 2.0.1-beta.

Specifies the default collation used for incoming requests. The collation can be overridden on a per-query basis. Refer to [the section called “Collations”](../../collations.md) section for the list of available collations and other details.

#### Example: {#example}

```

collation_server = utf8_ci

```