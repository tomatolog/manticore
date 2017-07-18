.. raw:: html

   <div class="navheader">

12.1.47. unpack\_mysqlcompress\_maxsize
`Prev <conf-unpack-mysqlcompress.html>`__ 
12.1. Data source configuration options
 `Next <conf-csvpipe-delimiter.html>`__

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

.. rubric:: 12.1.47. unpack\_mysqlcompress\_maxsize
   :name: unpack_mysqlcompress_maxsize
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Buffer size for UNCOMPRESS()ed data. Optional, default value is 16M.
Introduced in version 0.9.9-rc1.

When using `unpack\_mysqlcompress <conf-unpack-mysqlcompress.html>`__,
due to implementation intricacies it is not possible to deduce the
required buffer size from the compressed data. So the buffer must be
preallocated in advance, and unpacked data can not go over the buffer
size. This option lets you control the buffer size, both to limit
``indexer`` memory use, and to enable unpacking of really long data
fields if necessary.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    unpack_mysqlcompress_maxsize = 1M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+----------------------------------+-------------------------------------------+
| `Prev <conf-unpack-mysqlcompress.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-csvpipe-delimiter.html>`__   |
+----------------------------------------------+----------------------------------+-------------------------------------------+
| 12.1.46. unpack\_mysqlcompress               | `Home <index.html>`__            |  12.1.48. csvpipe\_delimiter              |
+----------------------------------------------+----------------------------------+-------------------------------------------+

.. raw:: html

   </div>
