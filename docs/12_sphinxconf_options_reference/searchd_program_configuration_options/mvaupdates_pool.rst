mva\_updates\_pool
~~~~~~~~~~~~~~~~~~

Shared pool size for in-memory MVA updates storage. Optional, default
size is 1M.

This setting controls the size of the shared storage pool for updated
MVA values. Specifying 0 for the size disable MVA updates at all. Once
the pool size limit is hit, MVA update attempts will result in an error.
However, updates on regular (scalar) attributes will still work. Due to
internal technical difficulties, currently it is <b>not</b> possible to
store (flush) <b>any</b> updates on indexes where MVA were updated;
though this might be implemented in the future. In the meantime, MVA
updates are intended to be used as a measure to quickly catchup with
latest changes in the database until the next index rebuild; not as a
persistent storage mechanism.

Example:
^^^^^^^^

::


    mva_updates_pool = 16M

