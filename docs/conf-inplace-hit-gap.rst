.. raw:: html

   <div class="navheader">

12.2.38. inplace\_hit\_gap
`Prev <conf-inplace-enable.html>`__ 
12.2. Index configuration options
 `Next <conf-inplace-docinfo-gap.html>`__

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

.. rubric:: 12.2.38. inplace\_hit\_gap
   :name: inplace_hit_gap
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

`In-place inversion <conf-inplace-enable.html>`__ fine-tuning option.
Controls preallocated hitlist gap size. Optional, default is 0.
Introduced in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    inplace_hit_gap = 1M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+---------------------------------+---------------------------------------------+
| `Prev <conf-inplace-enable.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-inplace-docinfo-gap.html>`__   |
+----------------------------------------+---------------------------------+---------------------------------------------+
| 12.2.37. inplace\_enable               | `Home <index.html>`__           |  12.2.39. inplace\_docinfo\_gap             |
+----------------------------------------+---------------------------------+---------------------------------------------+

.. raw:: html

   </div>
