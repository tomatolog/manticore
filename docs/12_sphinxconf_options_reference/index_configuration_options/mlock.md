### mlock {#mlock}

Memory locking for cached data. Optional, default is 0 (do not call mlock()).

For search performance, `searchd` preloads a copy of `.spa` and `.spi` files in RAM, and keeps that copy in RAM at all times. But if there are no searches on the index for some time, there are no accesses to that cached copy, and OS might decide to swap it out to disk. First queries to such &quot;cooled down&quot; index will cause swap-in and their latency will suffer.

Setting mlock option to 1 makes Sphinx lock physical RAM used for that cached data using mlock(2) system call, and that prevents swapping (see man 2 mlock for details). mlock(2) is a privileged call, so it will require `searchd` to be either run from root account, or be granted enough privileges otherwise. If mlock() fails, a warning is emitted, but index continues working.

#### Example: {#example}

```

mlock = 1

```