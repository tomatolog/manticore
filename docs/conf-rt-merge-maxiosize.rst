.. raw:: html

   <div class="navheader">

12.4.44. rt\_merge\_maxiosize
`Prev <conf-rt-merge-iops.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-predicted-time-costs.html>`__

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

.. rubric:: 12.4.44. rt\_merge\_maxiosize
   :name: rt_merge_maxiosize
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A maximum size of an I/O operation that the RT chunks merge thread is
allowed to start. Optional, default is 0 (no limit). Added in
2.1.1-beta.

This directive lets you throttle down the I/O impact arising from the
``OPTIMIZE`` statements. I/Os bigger than this limit will be broken down
into 2 or more I/Os, which will then be accounted as separate I/Os with
regards to the `rt\_merge\_iops <conf-rt-merge-iops.html>`__ limit.
Thus, it is guaranteed that all the optimization activity will not
generate more than (rt\_merge\_iops \* rt\_merge\_maxiosize) bytes of
disk I/O per second.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    rt_merge_maxiosize = 1M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+-----------------------------------+----------------------------------------------+
| `Prev <conf-rt-merge-iops.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-predicted-time-costs.html>`__   |
+---------------------------------------+-----------------------------------+----------------------------------------------+
| 12.4.43. rt\_merge\_iops              | `Home <index.html>`__             |  12.4.45. predicted\_time\_costs             |
+---------------------------------------+-----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
