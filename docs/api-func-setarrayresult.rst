.. raw:: html

   <div class="navheader">

9.1.6. SetArrayResult
`Prev <api-func-setconnecttimeout.html>`__ 
9.1. General API functions
 `Next <api-func-isconnecterror.html>`__

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

.. rubric:: 9.1.6. SetArrayResult
   :name: setarrayresult
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetArrayResult ( $arrayresult )

PHP specific. Controls matches format in the search results set (whether
matches should be returned as an array or a hash).

``$arrayresult`` argument must be boolean. If ``$arrayresult`` is
``false`` (the default mode), matches will returned in PHP hash format
with document IDs as keys, and other information (weight, attributes) as
values. If ``$arrayresult`` is true, matches will be returned as a plain
array with complete per-match information including document ID.

Introduced along with GROUP BY support on MVA attributes. Group-by-MVA
result sets may contain duplicate document IDs. Thus they need to be
returned as plain arrays, because hashes will only keep one entry per
document ID.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+---------------------------------------+--------------------------------------------+
| `Prev <api-func-setconnecttimeout.html>`__    | `Up <api-funcgroup-general.html>`__   |  `Next <api-func-isconnecterror.html>`__   |
+-----------------------------------------------+---------------------------------------+--------------------------------------------+
| 9.1.5. SetConnectTimeout                      | `Home <index.html>`__                 |  9.1.7. IsConnectError                     |
+-----------------------------------------------+---------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
