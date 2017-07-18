.. raw:: html

   <div class="navheader">

12.4.13. preopen\_indexes
`Prev <conf-seamless-rotate.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-unlink-old.html>`__

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

.. rubric:: 12.4.13. preopen\_indexes
   :name: preopen_indexes
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Whether to forcibly preopen all indexes on startup. Optional, default is
1 (preopen everything).

Starting with 2.0.1-beta, the default value for this option is now 1
(foribly preopen all indexes). In prior versions, it used to be 0 (use
per-index settings).

When set to 1, this directive overrides and enforces
`preopen <conf-preopen.html>`__ on all indexes. They will be preopened,
no matter what is the per-index ``preopen`` setting. When set to 0,
per-index settings can take effect. (And they default to 0.)

Pre-opened indexes avoid races between search queries and rotations that
can cause queries to fail occasionally. They also make ``searchd`` use
more file handles. In most scenarios it’s therefore preferred and
recommended to preopen indexes.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    preopen_indexes = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+-----------------------------------+------------------------------------+
| `Prev <conf-seamless-rotate.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-unlink-old.html>`__   |
+-----------------------------------------+-----------------------------------+------------------------------------+
| 12.4.12. seamless\_rotate               | `Home <index.html>`__             |  12.4.14. unlink\_old              |
+-----------------------------------------+-----------------------------------+------------------------------------+

.. raw:: html

   </div>
