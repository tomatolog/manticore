.. raw:: html

   <div class="navheader">

12.5.7. rlp\_max\_batch\_size
`Prev <conf-rlp-environment.html>`__ 
12.5. Common section configuration options
 `Next <conf-rlp-max-batch-docs.html>`__

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

.. rubric:: 12.5.7. rlp\_max\_batch\_size
   :name: rlp_max_batch_size
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum total size of documents batched before processing them by the
RLP. Optional, default is 51200. Do not set this value to more than 10Mb
because sphinx splits large documents to 10Mb chunks before processing
them by the RLP. This option has effect only if
``morphology = rlp_chinese_batched`` is specified. Added in 2.2.1-beta.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    rlp_max_batch_size = 100k

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+----------------------------------+--------------------------------------------+
| `Prev <conf-rlp-environment.html>`__    | `Up <confgroup-common.html>`__   |  `Next <conf-rlp-max-batch-docs.html>`__   |
+-----------------------------------------+----------------------------------+--------------------------------------------+
| 12.5.6. rlp\_environment                | `Home <index.html>`__            |  12.5.8. rlp\_max\_batch\_docs             |
+-----------------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
