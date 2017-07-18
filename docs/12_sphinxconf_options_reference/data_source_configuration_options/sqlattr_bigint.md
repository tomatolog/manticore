### sql_attr_bigint {#sql-attr-bigint}

64-bit signed integer [attribute](../../attributes.md) declaration. Multi-value (there might be multiple attributes declared), optional. Applies to SQL source types (`mysql`, `pgsql`, `mssql`) only. Note that unlike [sql_attr_uint](../../data_source_configuration_options/sqlattr_uint.md), these values are &lt;b&gt;signed&lt;/b&gt;. Introduced in version 0.9.9-rc1.

#### Example: {#example}

```

sql_attr_bigint = my_bigint_id

```