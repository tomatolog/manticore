max\_packet\_size
~~~~~~~~~~~~~~~~~

Maximum allowed network packet size. Limits both query packets from
clients, and response packets from remote agents in distributed
environment. Only used for internal sanity checks, does not directly
affect RAM use or performance. Optional, default is 8M.

Example:
^^^^^^^^

::


    max_packet_size = 32M

