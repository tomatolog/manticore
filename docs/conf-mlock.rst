.. raw:: html

   <div class="navheader">

12.2.5. mlock
`Prev <conf-docinfo.html>`__ 
12.2. Index configuration options
 `Next <conf-morphology.html>`__

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

.. rubric:: 12.2.5. mlock
   :name: mlock
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Memory locking for cached data. Optional, default is 0 (do not call
mlock()).

For search performance, ``searchd`` preloads a copy of ``.spa`` and
``.spi`` files in RAM, and keeps that copy in RAM at all times. But if
there are no searches on the index for some time, there are no accesses
to that cached copy, and OS might decide to swap it out to disk. First
queries to such “cooled down” index will cause swap-in and their latency
will suffer.

Setting mlock option to 1 makes Sphinx lock physical RAM used for that
cached data using mlock(2) system call, and that prevents swapping (see
man 2 mlock for details). mlock(2) is a privileged call, so it will
require ``searchd`` to be either run from root account, or be granted
enough privileges otherwise. If mlock() fails, a warning is emitted, but
index continues working.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mlock = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------+---------------------------------+------------------------------------+
| `Prev <conf-docinfo.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-morphology.html>`__   |
+---------------------------------+---------------------------------+------------------------------------+
| 12.2.4. docinfo                 | `Home <index.html>`__           |  12.2.6. morphology                |
+---------------------------------+---------------------------------+------------------------------------+

.. raw:: html

   </div>
