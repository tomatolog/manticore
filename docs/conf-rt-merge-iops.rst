.. raw:: html

   <div class="navheader">

12.4.43. rt\_merge\_iops
`Prev <conf-persistent-connections-limit.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-rt-merge-maxiosize.html>`__

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

.. rubric:: 12.4.43. rt\_merge\_iops
   :name: rt_merge_iops
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A maximum number of I/O operations (per second) that the RT chunks merge
thread is allowed to start. Optional, default is 0 (no limit). Added in
2.1.1-beta.

This directive lets you throttle down the I/O impact arising from the
``OPTIMIZE`` statements. It is guaranteed that all the RT optimization
activity will not generate more disk iops (I/Os per second) than the
configured limit. Modern SATA drives can perform up to around 100 I/O
operations per second, and limiting rt\_merge\_iops can reduce search
performance degradation caused by merging.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    rt_merge_iops = 40

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------------+-----------------------------------+--------------------------------------------+
| `Prev <conf-persistent-connections-limit.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-rt-merge-maxiosize.html>`__   |
+------------------------------------------------------+-----------------------------------+--------------------------------------------+
| 12.4.42. persistent\_connections\_limit              | `Home <index.html>`__             |  12.4.44. rt\_merge\_maxiosize             |
+------------------------------------------------------+-----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
