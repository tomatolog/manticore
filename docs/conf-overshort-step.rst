.. raw:: html

   <div class="navheader">

12.2.43. overshort\_step
`Prev <conf-index-exact-words.html>`__ 
12.2. Index configuration options
 `Next <conf-stopword-step.html>`__

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

.. rubric:: 12.2.43. overshort\_step
   :name: overshort_step
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Position increment on overshort (less that
`min\_word\_len <conf-min-word-len.html>`__) keywords. Optional, allowed
values are 0 and 1, default is 1. Introduced in version 0.9.9-rc1.

This directive does not affect ``searchd`` in any way, it only affects
``indexer``.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    overshort_step = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+---------------------------------+---------------------------------------+
| `Prev <conf-index-exact-words.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-stopword-step.html>`__   |
+-------------------------------------------+---------------------------------+---------------------------------------+
| 12.2.42. index\_exact\_words              | `Home <index.html>`__           |  12.2.44. stopword\_step              |
+-------------------------------------------+---------------------------------+---------------------------------------+

.. raw:: html

   </div>
