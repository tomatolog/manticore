.. raw:: html

   <div class="navheader">

9.5.2. SetGroupDistinct
`Prev <api-func-setgroupby.html>`__ 
9.5. GROUP BY settings
 `Next <api-funcgroup-querying.html>`__

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

.. rubric:: 9.5.2. SetGroupDistinct
   :name: setgroupdistinct
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetGroupDistinct ( $attribute )

Sets attribute name for per-group distinct values count calculations.
Only available for grouping queries.

``$attribute`` is a string that contains the attribute name. For each
group, all values of this attribute will be stored (as RAM limits
permit), then the amount of distinct values will be calculated and
returned to the client. This feature is similar to ``COUNT(DISTINCT)``
clause in standard SQL; so these Sphinx calls:

.. code:: programlisting

    $cl->SetGroupBy ( "category", SPH_GROUPBY_ATTR, "@count desc" );
    $cl->SetGroupDistinct ( "vendor" );

can be expressed using the following SQL clauses:

.. code:: programlisting

    SELECT id, weight, all-attributes,
        COUNT(DISTINCT vendor) AS @distinct,
        COUNT(*) AS @count
    FROM products
    GROUP BY category
    ORDER BY @count DESC

In the sample pseudo code shown just above, ``SetGroupDistinct()`` call
corresponds to ``COUNT(DISINCT vendor)`` clause only. ``GROUP BY``,
``ORDER BY``, and ``COUNT(*)`` clauses are all an equivalent of
``SetGroupBy()`` settings. Both queries will return one matching row for
each category. In addition to indexed attributes, matches will also
contain total per-category matches count, and the count of distinct
vendor IDs within each category.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+---------------------------------------+-------------------------------------------+
| `Prev <api-func-setgroupby.html>`__    | `Up <api-funcgroup-groupby.html>`__   |  `Next <api-funcgroup-querying.html>`__   |
+----------------------------------------+---------------------------------------+-------------------------------------------+
| 9.5.1. SetGroupBy                      | `Home <index.html>`__                 |  9.6. Querying                            |
+----------------------------------------+---------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
