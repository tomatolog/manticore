workers
~~~~~~~

Multi-processing mode (MPM). Optional; allowed values are thread\_pool,
and threads. Default is thread\_pool.

Lets you choose how ``searchd`` processes multiple concurrent requests.
The possible values are:

-  threads
-  A new dedicated thread is created on every incoming network
   connection. Subsequent queries on that connection are handled by that
   thread. When a client disconnected, the thread gets killed.

-  thread\_pool
-  A worker threads pool is created on daemon startup. An internal
   network thread handles all the incoming network connections.
   Subsequent queries on any connection are then put into a queue, and
   processed in order by the first avaialble worker thread from the
   pool. No threads are normally created or killed, neither for new
   connections, nor for new queries. Network thread uses epoll() and
   poll() on Linux, kqueue() on Mac OS/BSD, and WSAPoll on Windows
   (Vista and later). This is the default mode.

Thread pool is a newer, better, faster implementation of threads mode
which does not suffer from overheads of creating a new thread per every
new connection and managing a lot of parallel threads. We still retain
workers=threads for the transition period, but thread pool is scheduled
to become the only MPM mode.

Example:
^^^^^^^^

::


    workers = thread_pool

