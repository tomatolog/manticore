.. raw:: html

   <div class="navheader">

12.3.6. max\_file\_field\_buffer
`Prev <conf-write-buffer.html>`__ 
12.3. \ ``indexer`` program configuration options
 `Next <conf-on-file-field-error.html>`__

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

.. rubric:: 12.3.6. max\_file\_field\_buffer
   :name: max_file_field_buffer
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum file field adaptive buffer size, bytes. Optional, default is 8
MB, minimum is 1 MB.

File field buffer is used to load files referred to from
`sql\_file\_field <conf-sql-file-field.html>`__ columns. This buffer is
adaptive, starting at 1 MB at first allocation, and growing in 2x steps
until either file contents can be loaded, or maximum buffer size,
specified by ``max_file_field_buffer`` directive, is reached.

Thus, if there are no file fields are specified, no buffer is allocated
at all. If all files loaded during indexing are under (for example) 2 MB
in size, but ``max_file_field_buffer`` value is 128 MB, peak buffer
usage would still be only 2 MB. However, files over 128 MB would be
entirely skipped.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_file_field_buffer = 128M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+-----------------------------------+---------------------------------------------+
| `Prev <conf-write-buffer.html>`__    | `Up <confgroup-indexer.html>`__   |  `Next <conf-on-file-field-error.html>`__   |
+--------------------------------------+-----------------------------------+---------------------------------------------+
| 12.3.5. write\_buffer                | `Home <index.html>`__             |  12.3.7. on\_file\_field\_error             |
+--------------------------------------+-----------------------------------+---------------------------------------------+

.. raw:: html

   </div>
