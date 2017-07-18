.. raw:: html

   <div class="navheader">

12.2.30. local
`Prev <conf-html-remove-elements.html>`__ 
12.2. Index configuration options
 `Next <conf-agent.html>`__

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

.. rubric:: 12.2.30. local
   :name: local
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Local index declaration in the `distributed index <distributed.html>`__.
Multi-value, optional, default is empty.

This setting is used to declare local indexes that will be searched when
given distributed index is searched. Many local indexes can be declared
per each distributed index. Any local index can also be mentioned
several times in different distributed indexes.

Note that by default all local indexes will be searched
**sequentially**, utilizing only 1 CPU or core. To parallelize
processing of the local parts in the distributed index, you should use
``dist_threads`` directive, see `Section 12.4.27,
“dist\_threads” <conf-dist-threads.html>`__.

Before ``dist_threads``, there also was a legacy solution to configure
``searchd`` to query itself instead of using local indexes (refer to
`Section 12.2.31, “agent” <conf-agent.html>`__ for the details).
However, that creates redundant CPU and network load, and
``dist_threads`` is now strongly suggested instead.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    local = chunk1
    local = chunk2

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+---------------------------------+-------------------------------+
| `Prev <conf-html-remove-elements.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-agent.html>`__   |
+----------------------------------------------+---------------------------------+-------------------------------+
| 12.2.29. html\_remove\_elements              | `Home <index.html>`__           |  12.2.31. agent               |
+----------------------------------------------+---------------------------------+-------------------------------+

.. raw:: html

   </div>
