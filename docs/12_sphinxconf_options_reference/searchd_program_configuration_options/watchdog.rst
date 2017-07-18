watchdog
~~~~~~~~

Threaded server watchdog. Optional, default is 1 (watchdog enabled).
Introduced in version 2.0.1-beta.

A crashed query in ``threads`` multi-processing mode
(``[workers](../../searchd_program_configuration_options/workers.rst) = threads``)
can take down the entire server. With watchdog feature enabled,
``searchd`` additionally keeps a separate lightweight process that
monitors the main server process, and automatically restarts the latter
in case of abnormal termination. Watchdog is enabled by default.

Example:
^^^^^^^^

::


    watchdog = 0 # disable watchdog

