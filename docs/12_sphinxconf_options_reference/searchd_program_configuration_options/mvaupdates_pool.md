### mva_updates_pool {#mva-updates-pool}

Shared pool size for in-memory MVA updates storage. Optional, default size is 1M. Introduced in version 0.9.9-rc1.

This setting controls the size of the shared storage pool for updated MVA values. Specifying 0 for the size disable MVA updates at all. Once the pool size limit is hit, MVA update attempts will result in an error. However, updates on regular (scalar) attributes will still work. Due to internal technical difficulties, currently it is &lt;b&gt;not&lt;/b&gt; possible to store (flush) &lt;b&gt;any&lt;/b&gt; updates on indexes where MVA were updated; though this might be implemented in the future. In the meantime, MVA updates are intended to be used as a measure to quickly catchup with latest changes in the database until the next index rebuild; not as a persistent storage mechanism.

#### Example: {#example}

```

mva_updates_pool = 16M

```