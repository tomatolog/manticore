### write_buffer {#write-buffer}

Write buffer size, bytes. Optional, default is 1 MB.

Write buffers are used to write both temporary and final index files when indexing. Larger buffers reduce the number of required disk writes. Memory for the buffers is allocated in addition to [mem_limit](../../indexer_program_configuration_options/memlimit.md). Note that several (currently up to 4) buffers for different files will be allocated, proportionally increasing the RAM usage.

#### Example: {#example}

```

write_buffer = 4M

```