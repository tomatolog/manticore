.. raw:: html

   <div class="navheader">

12.4.4. query\_log\_format
`Prev <conf-query-log.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-read-timeout.html>`__

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

.. rubric:: 12.4.4. query\_log\_format
   :name: query_log_format
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Query log format. Optional, allowed values are ‘plain’ and ‘sphinxql’,
default is ‘plain’. Introduced in version 2.0.1-beta.

Starting with version 2.0.1-beta, two different log formats are
supported. The default one logs queries in a custom text format. The new
one logs valid SphinxQL statements. This directive allows to switch
between the two formats on search daemon startup. The log format can
also be altered on the fly, using
``SET GLOBAL query_log_format=sphinxql`` syntax. Refer to `Section 5.9,
“\ ``searchd`` query log formats” <query-log-format.html>`__ for more
discussion and format details.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    query_log_format = sphinxql

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+-----------------------------------+--------------------------------------+
| `Prev <conf-query-log.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-read-timeout.html>`__   |
+-----------------------------------+-----------------------------------+--------------------------------------+
| 12.4.3. query\_log                | `Home <index.html>`__             |  12.4.5. read\_timeout               |
+-----------------------------------+-----------------------------------+--------------------------------------+

.. raw:: html

   </div>
