.. raw:: html

   <div class="navheader">

12.4.19. max\_filter\_values
`Prev <conf-max-filters.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-listen-backlog.html>`__

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

.. rubric:: 12.4.19. max\_filter\_values
   :name: max_filter_values
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum allowed per-filter values count. Only used for internal sanity
checks, does not directly affect RAM use or performance. Optional,
default is 4096. Introduced in version 0.9.9-rc1.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_filter_values = 16384

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+-----------------------------------+----------------------------------------+
| `Prev <conf-max-filters.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-listen-backlog.html>`__   |
+-------------------------------------+-----------------------------------+----------------------------------------+
| 12.4.18. max\_filters               | `Home <index.html>`__             |  12.4.20. listen\_backlog              |
+-------------------------------------+-----------------------------------+----------------------------------------+

.. raw:: html

   </div>
