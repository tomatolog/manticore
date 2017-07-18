### read_buffer {#read-buffer}

Per-keyword read buffer size. Optional, default is 256K.

For every keyword occurrence in every search query, there are two associated read buffers (one for document list and one for hit list). This setting lets you control their sizes, increasing per-query RAM use, but possibly decreasing IO time.

#### Example: {#example}

```

read_buffer = 1M

```