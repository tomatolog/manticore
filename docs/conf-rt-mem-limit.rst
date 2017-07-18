.. raw:: html

   <div class="navheader">

12.2.49. rt\_mem\_limit
`Prev <conf-blend-mode.html>`__ 
12.2. Index configuration options
 `Next <conf-rt-field.html>`__

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

.. rubric:: 12.2.49. rt\_mem\_limit
   :name: rt_mem_limit
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

RAM chunk size limit. Optional, default is 128M. Introduced in version
1.10-beta.

RT index keeps some data in memory (so-called RAM chunk) and also
maintains a number of on-disk indexes (so-called disk chunks). This
directive lets you control the RAM chunk size. Once there’s too much
data to keep in RAM, RT index will flush it to disk, activate a newly
created disk chunk, and reset the RAM chunk.

The limit is pretty strict; RT index should never allocate more memory
than it’s limited to. The memory is not preallocated either, hence,
specifying 512 MB limit and only inserting 3 MB of data should result in
allocating 3 MB, not 512 MB.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    rt_mem_limit = 512M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------+---------------------------------+----------------------------------+
| `Prev <conf-blend-mode.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-rt-field.html>`__   |
+------------------------------------+---------------------------------+----------------------------------+
| 12.2.48. blend\_mode               | `Home <index.html>`__           |  12.2.50. rt\_field              |
+------------------------------------+---------------------------------+----------------------------------+

.. raw:: html

   </div>
