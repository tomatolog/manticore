.. raw:: html

   <div class="navheader">

12.4.35. rt\_flush\_period
`Prev <conf-mysql-version-string.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-thread-stack.html>`__

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

.. rubric:: 12.4.35. rt\_flush\_period
   :name: rt_flush_period
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

RT indexes RAM chunk flush check period, in seconds. Optional, default
is 10 hours. Introduced in version 2.0.1-beta.

Actively updated RT indexes that however fully fit in RAM chunks can
result in ever-growing binlogs, impacting disk use and crash recovery
time. With this directive the search daemon performs periodic flush
checks, and eligible RAM chunks can get saved, enabling consequential
binlog cleanup. See `Section 4.4, “Binary logging” <rt-binlog.html>`__
for more details.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    rt_flush_period = 3600 # 1 hour

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+-----------------------------------+--------------------------------------+
| `Prev <conf-mysql-version-string.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-thread-stack.html>`__   |
+----------------------------------------------+-----------------------------------+--------------------------------------+
| 12.4.34. mysql\_version\_string              | `Home <index.html>`__             |  12.4.36. thread\_stack              |
+----------------------------------------------+-----------------------------------+--------------------------------------+

.. raw:: html

   </div>
