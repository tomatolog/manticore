### plugin_dir {#plugin-dir}

Trusted location for the dynamic libraries (UDFs). Optional, default is empty (no location). Introduced in version 2.0.1-beta.

Specifies the trusted directory from which the [UDF libraries](../../sphinx_udfs_user_defined_functions.md) can be loaded. Requires [workers = thread](../../searchd_program_configuration_options/workers.md) to take effect.

#### Example: {#example}

```

plugin_dir = /usr/local/sphinx/lib

```