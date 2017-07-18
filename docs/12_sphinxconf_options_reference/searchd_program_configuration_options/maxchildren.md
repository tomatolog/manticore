### max_children {#max-children}

Maximum amount of worker threads (or in other words, concurrent queries to run in parallel). Optional, default is 0 (unlimited) in workers=threads, or 1.5 times the CPU cores count in workers=thread_pool mode.

max_children imposes a hard limit on the number of threads working on user queries. There might still be additional internal threads doing maintenance tasks, but when it comes to user queries, it is no more than max_children concurrent threads (and queries) at all times.

Note that in workers=threads mode a thread is allocated for every connection rather than an active query. So when there are 100 idle connections but only 2 active connections with currently running queries, that still accounts for 102 threads, all of them subject to max_children limit. So with a max_children set way too low, and pooled connections not reused well enough on the application side, you can effectively DOS your own server. When the limit is reached, any additional incoming connections will be dismissed with a temporary &quot;maxed out&quot; error immediately as they attempt to connect. Thus, in threads mode you should choose the max_children limit rather carefully, with not just the concurrent queries but also with potentially idle _network connections_ in mind.

Now, in workers=thread_pool mode the network connections are separated from query processing, so in the example above, 100 idle connections will all be handled by an internal network thread, and only the 2 actually active queries will be subject to max_children limit. When the limit is reached, any additional incoming _connections_ will still be accepted, and any additional _queries_ will [get enqueued](../../searchd_program_configuration_options/queuemax_length.md) until there are free worker threads. The queries will only start failing with a temporary Thus, in thread_pool mode it makes little sense to raise max_children much higher than the amount of CPU cores. Usually that will only hurt CPU contention and _decrease_ the general throughput.

#### Example: {#example}

```

max_children = 10

```