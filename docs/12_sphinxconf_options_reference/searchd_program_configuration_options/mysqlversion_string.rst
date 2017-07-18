mysql\_version\_string
~~~~~~~~~~~~~~~~~~~~~~

A server version string to return via MySQL protocol. Optional, default
is empty (return Sphinx version). Introduced in version 2.0.1-beta.

Several picky MySQL client libraries depend on a particular version
number format used by MySQL, and moreover, sometimes choose a different
execution path based on the reported version number (rather than the
indicated capabilities flags). For instance, Python MySQLdb 1.2.2 throws
an exception when the version number is not in X.Y.ZZ format; MySQL .NET
connector 6.3.x fails internally on version numbers 1.x along with a
certain combination of flags, etc. To workaround that, you can use
``mysql_version_string`` directive and have ``searchd`` report a
different version to clients connecting over MySQL protocol. (By
default, it reports its own version.)

Example:
^^^^^^^^

::


    mysql_version_string = 5.0.37

