.. raw:: html

   <div class="navheader">

9.5.1. SetGroupBy
`Prev <api-funcgroup-groupby.html>`__ 
9.5. GROUP BY settings
 `Next <api-func-setgroupdistinct.html>`__

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

.. rubric:: 9.5.1. SetGroupBy
   :name: setgroupby
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetGroupBy ( $attribute, $func,
$groupsort=“@group desc” )

Sets grouping attribute, function, and groups sorting mode; and enables
grouping (as described in `Section 5.7, “Grouping (clustering) search
results ” <clustering.html>`__).

``$attribute`` is a string that contains group-by attribute name.
``$func`` is a constant that chooses a function applied to the attribute
value in order to compute group-by key. ``$groupsort`` is a clause that
controls how the groups will be sorted. Its syntax is similar to that
described in `the section called “SPH\_SORT\_EXTENDED
mode” <sorting-modes.html#sort-extended>`__.

Grouping feature is very similar in nature to GROUP BY clause from SQL.
Results produces by this function call are going to be the same as
produced by the following pseudo code:

.. code:: programlisting

    SELECT ... GROUP BY $func($attribute) ORDER BY $groupsort

Note that it’s ``$groupsort`` that affects the order of matches in the
final result set. Sorting mode (see `Section 9.3.3,
“SetSortMode” <api-func-setsortmode.html>`__) affect the ordering of
matches *within* group, ie. what match will be selected as the best one
from the group. So you can for instance order the groups by matches
count and select the most relevant match within each group at the same
time.

Starting with version 0.9.9-rc2, aggregate functions (AVG(), MIN(),
MAX(), SUM()) are supported through
`SetSelect() <api-func-setselect.html>`__ API call when using GROUP BY.

Starting with version 2.0.1-beta, grouping on string attributes is
supported, with respect to current collation.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------------------+----------------------------------------------+
| `Prev <api-funcgroup-groupby.html>`__    | `Up <api-funcgroup-groupby.html>`__   |  `Next <api-func-setgroupdistinct.html>`__   |
+------------------------------------------+---------------------------------------+----------------------------------------------+
| 9.5. GROUP BY settings                   | `Home <index.html>`__                 |  9.5.2. SetGroupDistinct                     |
+------------------------------------------+---------------------------------------+----------------------------------------------+

.. raw:: html

   </div>
