.. raw:: html

   <div class="navheader">

12.3.3. max\_iosize
`Prev <conf-max-iops.html>`__ 
12.3. \ ``indexer`` program configuration options
 `Next <conf-max-xmlpipe2-field.html>`__

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

.. rubric:: 12.3.3. max\_iosize
   :name: max_iosize
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum allowed I/O operation size, in bytes, for I/O throttling.
Optional, default is 0 (unlimited).

I/O throttling related option. It limits maximum file I/O operation
(read or write) size for all operations performed by ``indexer``. A
value of 0 means that no limit is imposed. Reads or writes that are
bigger than the limit will be split in several smaller operations, and
counted as several operation by `max\_iops <conf-max-iops.html>`__
setting. At the time of this writing, all I/O calls should be under 256
KB (default internal buffer size) anyway, so ``max_iosize`` values
higher than 256 KB must not affect anything.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_iosize = 1048576

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------+-----------------------------------+--------------------------------------------+
| `Prev <conf-max-iops.html>`__    | `Up <confgroup-indexer.html>`__   |  `Next <conf-max-xmlpipe2-field.html>`__   |
+----------------------------------+-----------------------------------+--------------------------------------------+
| 12.3.2. max\_iops                | `Home <index.html>`__             |  12.3.4. max\_xmlpipe2\_field              |
+----------------------------------+-----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
