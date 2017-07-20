attr\_flush\_period
~~~~~~~~~~~~~~~~~~~

When calling ``UpdateAttributes()`` to update document attributes in
real-time, changes are first written to the in-memory copy of attributes
(``docinfo`` must be set to ``extern``). Then, once ``searchd`` shuts
down normally (via ``SIGTERM`` being sent), the changes are written to
disk.

It is possible to tell ``searchd`` to periodically write these changes
back to disk, to avoid them being lost. The time between those intervals
is set with ``attr_flush_period``, in seconds.

It defaults to 0, which disables the periodic flushing, but flushing
will still occur at normal shut-down.

Example:
^^^^^^^^

::


    attr_flush_period = 900 # persist updates to disk every 15 minutes

