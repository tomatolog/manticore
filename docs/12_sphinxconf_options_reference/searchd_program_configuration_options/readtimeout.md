### read_timeout {#read-timeout}

Network client request read timeout, in seconds. Optional, default is 5 seconds. `searchd` will forcibly close the client connections which fail to send a query within this timeout.

#### Example: {#example}

```

read_timeout = 1

```