plugin\_dir
~~~~~~~~~~~

Trusted location for the dynamic libraries (UDFs). Optional, default is
empty (no location).

Specifies the trusted directory from which the `UDF
libraries <../../sphinx_udfs_user_defined_functions.md>`__ can be
loaded. Requires `workers =
thread <../../searchd_program_configuration_options/workers.md>`__ to
take effect.

Example:
^^^^^^^^

::


    plugin_dir = /usr/local/sphinx/lib

