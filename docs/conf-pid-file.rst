.. raw:: html

   <div class="navheader">

12.4.11. pid\_file
`Prev <conf-queue-max-length.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-seamless-rotate.html>`__

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

.. rubric:: 12.4.11. pid\_file
   :name: pid_file
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

``searchd`` process ID file name. Mandatory.

PID file will be re-created (and locked) on startup. It will contain
head daemon process ID while the daemon is running, and it will be
unlinked on daemon shutdown. It’s mandatory because Sphinx uses it
internally for a number of things: to check whether there already is a
running instance of ``searchd``; to stop ``searchd``; to notify it that
it should rotate the indexes. Can also be used for different external
automation scripts.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    pid_file = /var/run/searchd.pid

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------+-----------------------------------------+
| `Prev <conf-queue-max-length.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-seamless-rotate.html>`__   |
+------------------------------------------+-----------------------------------+-----------------------------------------+
| 12.4.10. queue\_max\_length              | `Home <index.html>`__             |  12.4.12. seamless\_rotate              |
+------------------------------------------+-----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
