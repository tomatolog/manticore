.. raw:: html

   <div class="navheader">

12.4.39. sphinxql\_state
`Prev <conf-watchdog.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-ha-ping-interval.html>`__

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

.. rubric:: 12.4.39. sphinxql\_state
   :name: sphinxql_state
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Path to a file where current SphinxQL state will be serialized.
Available since version 2.1.1-beta.

On daemon startup, this file gets replayed. On eligible state changes
(eg. SET GLOBAL), this file gets rewritten automatically. This can
prevent a hard-to-diagnose problem: If you load UDF functions, but
Sphinx crashes, when it gets (automatically) restarted, your UDF and
global variables will no longer be available; using persistent state
helps a graceful recovery with no such surprises.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sphinxql_state = uservars.sql

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-watchdog.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-ha-ping-interval.html>`__   |
+----------------------------------+-----------------------------------+------------------------------------------+
| 12.4.38. watchdog                | `Home <index.html>`__             |  12.4.40. ha\_ping\_interval             |
+----------------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
