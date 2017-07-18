sql\_attr\_float
~~~~~~~~~~~~~~~~

Floating point `attribute <../../attributes.rst>`__ declaration.
Multi-value (there might be multiple attributes declared), optional.
Applies to SQL source types (``mysql``, ``pgsql``, ``mssql``) only.

The values will be stored in single precision, 32-bit IEEE 754 format.
Represented range is approximately from 1e-38 to 1e+38. The amount of
decimal digits that can be stored precisely is approximately 7. One
important usage of the float attributes is storing latitude and
longitude values (in radians), for further usage in query-time geosphere
distance calculations.

Example:
^^^^^^^^

::


    sql_attr_float = lat_radians
    sql_attr_float = long_radians

