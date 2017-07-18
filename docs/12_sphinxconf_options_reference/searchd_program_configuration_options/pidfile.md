### pid_file {#pid-file}

`searchd` process ID file name. Mandatory.

PID file will be re-created (and locked) on startup. It will contain head daemon process ID while the daemon is running, and it will be unlinked on daemon shutdown. It&#039;s mandatory because Sphinx uses it internally for a number of things: to check whether there already is a running instance of `searchd`; to stop `searchd`; to notify it that it should rotate the indexes. Can also be used for different external automation scripts.

#### Example: {#example}

```

pid_file = /var/run/searchd.pid

```