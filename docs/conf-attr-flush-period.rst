.. raw:: html

   <div class="navheader">

12.4.15. attr\_flush\_period
`Prev <conf-unlink-old.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-max-packet-size.html>`__

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

.. rubric:: 12.4.15. attr\_flush\_period
   :name: attr_flush_period
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

When calling ``UpdateAttributes()`` to update document attributes in
real-time, changes are first written to the in-memory copy of attributes
(``docinfo`` must be set to ``extern``). Then, once ``searchd`` shuts
down normally (via ``SIGTERM`` being sent), the changes are written to
disk. Introduced in version 0.9.9-rc1.

Starting with 0.9.9-rc1, it is possible to tell ``searchd`` to
periodically write these changes back to disk, to avoid them being lost.
The time between those intervals is set with ``attr_flush_period``, in
seconds.

It defaults to 0, which disables the periodic flushing, but flushing
will still occur at normal shut-down.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    attr_flush_period = 900 # persist updates to disk every 15 minutes

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------+-----------------------------------+-----------------------------------------+
| `Prev <conf-unlink-old.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-max-packet-size.html>`__   |
+------------------------------------+-----------------------------------+-----------------------------------------+
| 12.4.14. unlink\_old               | `Home <index.html>`__             |  12.4.16. max\_packet\_size             |
+------------------------------------+-----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
