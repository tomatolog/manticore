.. raw:: html

   <div class="navheader">

12.4.31. snippets\_file\_prefix
`Prev <conf-binlog-max-log-size.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-collation-server.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.4.31. snippets\_file\_prefix
   :name: snippets_file_prefix
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A prefix to prepend to the local file names when generating snippets.
Optional, default is empty. Introduced in version 2.1.1-beta.

This prefix can be used in distributed snippets generation along with
``load_files`` or ``load_files_scattered`` options.

Note how this is a prefix, and **not** a path! Meaning that if a prefix
is set to “server1” and the request refers to “file23”, ``searchd`` will
attempt to open “server1file23” (all of that without quotes). So if you
need it to be a path, you have to mention the trailing slash.

Note also that this is a local option, it does not affect the agents
anyhow. So you can safely set a prefix on a master server. The requests
routed to the agents will not be affected by the master’s setting. They
will however be affected by the agent’s own settings.

This might be useful, for instance, when the document storage locations
(be those local storage or NAS mountpoints) are inconsistent across the
servers.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    snippets_file_prefix = /mnt/common/server1/

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-binlog-max-log-size.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-collation-server.html>`__   |
+---------------------------------------------+-----------------------------------+------------------------------------------+
| 12.4.30. binlog\_max\_log\_size             | `Home <index.html>`__             |  12.4.32. collation\_server              |
+---------------------------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
