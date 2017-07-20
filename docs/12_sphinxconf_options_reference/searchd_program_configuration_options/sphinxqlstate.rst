sphinxql\_state
~~~~~~~~~~~~~~~

Path to a file where current SphinxQL state will be serialized.

On daemon startup, this file gets replayed. On eligible state changes
(eg. SET GLOBAL), this file gets rewritten automatically. This can
prevent a hard-to-diagnose problem: If you load UDF functions, but
Sphinx crashes, when it gets (automatically) restarted, your UDF and
global variables will no longer be available; using persistent state
helps a graceful recovery with no such surprises.

Example:
^^^^^^^^

::


    sphinxql_state = uservars.sql

