.. raw:: html

   <div class="navheader">

12.3.2. max\_iops
`Prev <conf-mem-limit.html>`__ 
12.3. \ ``indexer`` program configuration options
 `Next <conf-max-iosize.html>`__

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

.. rubric:: 12.3.2. max\_iops
   :name: max_iops
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum I/O operations per second, for I/O throttling. Optional, default
is 0 (unlimited).

I/O throttling related option. It limits maximum count of I/O operations
(reads or writes) per any given second. A value of 0 means that no limit
is imposed.

``indexer`` can cause bursts of intensive disk I/O during indexing, and
it might desired to limit its disk activity (and keep something for
other programs running on the same machine, such as ``searchd``). I/O
throttling helps to do that. It works by enforcing a minimum guaranteed
delay between subsequent disk I/O operations performed by ``indexer``.
Modern SATA HDDs are able to perform up to 70-100+ I/O operations per
second (that’s mostly limited by disk heads seek time). Limiting
indexing I/O to a fraction of that can help reduce search performance
degradation caused by indexing.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_iops = 40

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+-----------------------------------+------------------------------------+
| `Prev <conf-mem-limit.html>`__    | `Up <confgroup-indexer.html>`__   |  `Next <conf-max-iosize.html>`__   |
+-----------------------------------+-----------------------------------+------------------------------------+
| 12.3.1. mem\_limit                | `Home <index.html>`__             |  12.3.3. max\_iosize               |
+-----------------------------------+-----------------------------------+------------------------------------+

.. raw:: html

   </div>
