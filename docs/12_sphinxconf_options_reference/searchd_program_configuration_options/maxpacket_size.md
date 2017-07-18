### max_packet_size {#max-packet-size}

Maximum allowed network packet size. Limits both query packets from clients, and response packets from remote agents in distributed environment. Only used for internal sanity checks, does not directly affect RAM use or performance. Optional, default is 8M. Introduced in version 0.9.9-rc1.

#### Example: {#example}

```

max_packet_size = 32M

```