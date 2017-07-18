.. raw:: html

   <div class="navheader">

12.4.22. read\_unhinted
`Prev <conf-read-buffer.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-max-batch-queries.html>`__

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

.. rubric:: 12.4.22. read\_unhinted
   :name: read_unhinted
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Unhinted read size. Optional, default is 32K.

When querying, some reads know in advance exactly how much data is there
to be read, but some currently do not. Most prominently, hit list size
in not currently known in advance. This setting lest you control how
much data to read in such cases. It will impact hit list IO time,
reducing it for lists larger than unhinted read size, but raising it for
smaller lists. It will **not** affect RAM use because read buffer will
be already allocated. So it should be not greater than read\_buffer.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    read_unhinted = 32K

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+-----------------------------------+-------------------------------------------+
| `Prev <conf-read-buffer.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-max-batch-queries.html>`__   |
+-------------------------------------+-----------------------------------+-------------------------------------------+
| 12.4.21. read\_buffer               | `Home <index.html>`__             |  12.4.23. max\_batch\_queries             |
+-------------------------------------+-----------------------------------+-------------------------------------------+

.. raw:: html

   </div>
