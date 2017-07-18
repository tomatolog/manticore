.. raw:: html

   <div class="navheader">

12.3.5. write\_buffer
`Prev <conf-max-xmlpipe2-field.html>`__ 
12.3. \ ``indexer`` program configuration options
 `Next <conf-max-file-field-buffer.html>`__

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

.. rubric:: 12.3.5. write\_buffer
   :name: write_buffer
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Write buffer size, bytes. Optional, default is 1 MB.

Write buffers are used to write both temporary and final index files
when indexing. Larger buffers reduce the number of required disk writes.
Memory for the buffers is allocated in addition to
`mem\_limit <conf-mem-limit.html>`__. Note that several (currently up to
4) buffers for different files will be allocated, proportionally
increasing the RAM usage.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    write_buffer = 4M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+-----------------------------------+-----------------------------------------------+
| `Prev <conf-max-xmlpipe2-field.html>`__    | `Up <confgroup-indexer.html>`__   |  `Next <conf-max-file-field-buffer.html>`__   |
+--------------------------------------------+-----------------------------------+-----------------------------------------------+
| 12.3.4. max\_xmlpipe2\_field               | `Home <index.html>`__             |  12.3.6. max\_file\_field\_buffer             |
+--------------------------------------------+-----------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
