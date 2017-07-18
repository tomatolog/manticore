### snippets_file_prefix {#snippets-file-prefix}

A prefix to prepend to the local file names when generating snippets. Optional, default is empty. Introduced in version 2.1.1-beta.

This prefix can be used in distributed snippets generation along with `load_files` or `load_files_scattered` options.

Note how this is a prefix, and &lt;b&gt;not&lt;/b&gt; a path! Meaning that if a prefix is set to &quot;server1&quot; and the request refers to &quot;file23&quot;, `searchd` will attempt to open &quot;server1file23&quot; (all of that without quotes). So if you need it to be a path, you have to mention the trailing slash.

Note also that this is a local option, it does not affect the agents anyhow. So you can safely set a prefix on a master server. The requests routed to the agents will not be affected by the master&#039;s setting. They will however be affected by the agent&#039;s own settings.

This might be useful, for instance, when the document storage locations (be those local storage or NAS mountpoints) are inconsistent across the servers.

#### Example: {#example}

```

snippets_file_prefix = /mnt/common/server1/

```