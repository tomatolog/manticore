.. raw:: html

   <div class="navheader">

12.4.47. ondisk\_attrs\_default
`Prev <conf-shutdown-timeout.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-query-log-min-msec.html>`__

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

.. rubric:: 12.4.47. ondisk\_attrs\_default
   :name: ondisk_attrs_default
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Instance-wide defaults for `ondisk\_attrs <conf-ondisk-attrs.html>`__
directive. Optional, default is 0 (all attributes are loaded in memory).
This directive lets you specify the default value of ondisk\_attrs for
all indexes served by this copy of searchd. Per-index directives take
precedence, and will overwrite this instance-wide default value,
allowing for fine-grain control.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------+--------------------------------------------+
| `Prev <conf-shutdown-timeout.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-query-log-min-msec.html>`__   |
+------------------------------------------+-----------------------------------+--------------------------------------------+
| 12.4.46. shutdown\_timeout               | `Home <index.html>`__             |  12.4.48. query\_log\_min\_msec            |
+------------------------------------------+-----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
