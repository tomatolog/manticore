listen
~~~~~~

This setting lets you specify IP address and port, or Unix-domain socket
path, that ``searchd`` will listen on.

The informal grammar for ``listen`` setting is:

::


    listen = ( address ":" port | port | path ) [ ":" protocol ] [ "_vip" ]

I.e. you can specify either an IP address (or hostname) and port number,
or just a port number, or Unix socket path. If you specify port number
but not the address, ``searchd`` will listen on all network interfaces.
Unix path is identified by a leading slash.

You can also specify a protocol handler (listener) to be used for
connections on this socket. Supported protocol values are ‘sphinx’
(Manticore 0.9.x API protocol) and ‘mysql41’ (MySQL protocol used since 4.1
upto at least 5.1). More details on MySQL protocol support can be found
in `the section called “MySQL protocol support and
SphinxQL” <../../mysql_protocol_support_and_sphinxql.md>`__ section.

Adding a “\_vip" suffix to a protocol (for instance “sphinx\_vip” or
“mysql41\_vip”) makes all connections to that port bypass the thread
pool and always forcibly create a new dedicated thread. That's useful
for managing in case of a severe overload when the daemon would either
stall or not let you connect via a regular port.

Examples:
^^^^^^^^^

::


    listen = localhost
    listen = localhost:5000
    listen = 192.168.0.1:5000
    listen = /var/run/sphinx.s
    listen = 9312
    listen = localhost:9306:mysql41

There can be multiple listen directives, ``searchd`` will listen for
client connections on all specified ports and sockets. If no ``listen``
directives are found then the server will listen on all available
interfaces using the default ManticoreAPI port 9312, and also on default
SphinxQL port 9306. Both port numbers are assigned by IANA (see
http://www.iana.org/assignments/port-numbers for details) and should
therefore be available.

Unix-domain sockets are not supported on Windows.
