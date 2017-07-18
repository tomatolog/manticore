.. raw:: html

   <div class="navheader">

12.4.17. mva\_updates\_pool
`Prev <conf-max-packet-size.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-max-filters.html>`__

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

.. rubric:: 12.4.17. mva\_updates\_pool
   :name: mva_updates_pool
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Shared pool size for in-memory MVA updates storage. Optional, default
size is 1M. Introduced in version 0.9.9-rc1.

This setting controls the size of the shared storage pool for updated
MVA values. Specifying 0 for the size disable MVA updates at all. Once
the pool size limit is hit, MVA update attempts will result in an error.
However, updates on regular (scalar) attributes will still work. Due to
internal technical difficulties, currently it is **not** possible to
store (flush) **any** updates on indexes where MVA were updated; though
this might be implemented in the future. In the meantime, MVA updates
are intended to be used as a measure to quickly catchup with latest
changes in the database until the next index rebuild; not as a
persistent storage mechanism.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mva_updates_pool = 16M

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+-----------------------------------+-------------------------------------+
| `Prev <conf-max-packet-size.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-max-filters.html>`__   |
+-----------------------------------------+-----------------------------------+-------------------------------------+
| 12.4.16. max\_packet\_size              | `Home <index.html>`__             |  12.4.18. max\_filters              |
+-----------------------------------------+-----------------------------------+-------------------------------------+

.. raw:: html

   </div>
