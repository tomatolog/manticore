.. raw:: html

   <div class="navheader">

12.3.1. mem\_limit
`Prev <confgroup-indexer.html>`__ 
12.3. \ ``indexer`` program configuration options
 `Next <conf-max-iops.html>`__

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

.. rubric:: 12.3.1. mem\_limit
   :name: mem_limit
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Indexing RAM usage limit. Optional, default is 128M.

Enforced memory usage limit that the ``indexer`` will not go above. Can
be specified in bytes, or kilobytes (using K postfix), or megabytes
(using M postfix); see the example. This limit will be automatically
raised if set to extremely low value causing I/O buffers to be less than
8 KB; the exact lower bound for that depends on the indexed data size.
If the buffers are less than 256 KB, a warning will be produced.

Maximum possible limit is 2047M. Too low values can hurt indexing speed,
but 256M to 1024M should be enough for most if not all datasets. Setting
this value too high can cause SQL server timeouts. During the document
collection phase, there will be periods when the memory buffer is
partially sorted and no communication with the database is performed;
and the database server can timeout. You can resolve that either by
raising timeouts on SQL server side or by lowering ``mem_limit``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mem_limit = 256M
    # mem_limit = 262144K # same, but in KB
    # mem_limit = 268435456 # same, but in bytes

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------------+-----------------------------------+----------------------------------+
| `Prev <confgroup-indexer.html>`__                    | `Up <confgroup-indexer.html>`__   |  `Next <conf-max-iops.html>`__   |
+------------------------------------------------------+-----------------------------------+----------------------------------+
| 12.3. \ ``indexer`` program configuration options    | `Home <index.html>`__             |  12.3.2. max\_iops               |
+------------------------------------------------------+-----------------------------------+----------------------------------+

.. raw:: html

   </div>
