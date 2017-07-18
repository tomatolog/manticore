.. raw:: html

   <div class="navheader">

12.4.53. hostname\_lookup
`Prev <conf-agent-retry-delay.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-qcache-max-bytes.html>`__

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

.. rubric:: 12.4.53. hostname\_lookup
   :name: hostname_lookup
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Hostnames renew strategy. By default, IP addresses of agent host names
are cached at daemon start to avoid extra flood to DNS. In some cases
the IP can change dynamically (e.g. cloud hosting) and it might be
desired to don’t cache the IPs. Setting this option to ‘request’
disabled the caching and queries the DNS at each query. The IP addresses
can also be manually renewed with FLUSH HOSTNAMES command. Added in
2.3.2-beta.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-agent-retry-delay.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-qcache-max-bytes.html>`__   |
+-------------------------------------------+-----------------------------------+------------------------------------------+
| 12.4.52. agent\_retry\_delay              | `Home <index.html>`__             |  12.4.54. qcache\_max\_bytes             |
+-------------------------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
