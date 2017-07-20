rt\_mem\_limit
~~~~~~~~~~~~~~

RAM chunk size limit. Optional, default is 128M.

RT index keeps some data in memory (so-called RAM chunk) and also
maintains a number of on-disk indexes (so-called disk chunks). This
directive lets you control the RAM chunk size. Once there's too much
data to keep in RAM, RT index will flush it to disk, activate a newly
created disk chunk, and reset the RAM chunk.

The limit is pretty strict; RT index should never allocate more memory
than it's limited to. The memory is not preallocated either, hence,
specifying 512 MB limit and only inserting 3 MB of data should result in
allocating 3 MB, not 512 MB.

Example:
^^^^^^^^

::


    rt_mem_limit = 512M

