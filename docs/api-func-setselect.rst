.. raw:: html

   <div class="navheader">

9.2.4. SetSelect
`Prev <api-func-setoverride.html>`__ 
9.2. General query settings
 `Next <api-funcgroup-fulltext-query-settings.html>`__

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

.. rubric:: 9.2.4. SetSelect
   :name: setselect
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function SetSelect ( $clause )

Sets the select clause, listing specific attributes to fetch, and
`expressions <sorting-modes.html#sort-expr>`__ to compute and fetch.
Clause syntax mimics SQL. Introduced in version 0.9.9-rc1.

SetSelect() is very similar to the part of a typical SQL query between
SELECT and FROM. It lets you choose what attributes (columns) to fetch,
and also what expressions over the columns to compute and fetch. A
certain difference from SQL is that expressions **must** always be
aliased to a correct identifier (consisting of letters and digits) using
‘AS’ keyword. SQL also lets you do that but does not require to. Sphinx
enforces aliases so that the computation results can always be returned
under a “normal” name in the result set, used in other clauses, etc.

Everything else is basically identical to SQL. Star (’\*’) is supported.
Functions are supported. Arbitrary amount of expressions is supported.
Computed expressions can be used for sorting, filtering, and grouping,
just as the regular attributes.

Starting with version 0.9.9-rc2, aggregate functions (AVG(), MIN(),
MAX(), SUM()) are supported when using GROUP BY.

Expression sorting (`the section called “SPH\_SORT\_EXPR
mode” <sorting-modes.html#sort-expr>`__) and geodistance functions
(`Section 9.4.5, “SetGeoAnchor” <api-func-setgeoanchor.html>`__) are now
internally implemented using this computed expressions mechanism, using
magic names ‘@expr’ and ‘@geodist’ respectively.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    $cl->SetSelect ( "*, @weight+(user_karma+ln(pageviews))*0.1 AS myweight" );
    $cl->SetSelect ( "exp_years, salary_gbp*{$gbp_usd_rate} AS salary_usd,
       IF(age>40,1,0) AS over40" );
    $cl->SetSelect ( "*, AVG(price) AS avgprice" );

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+------------------------------------------------------+----------------------------------------------------------+
| `Prev <api-func-setoverride.html>`__    | `Up <api-funcgroup-general-query-settings.html>`__   |  `Next <api-funcgroup-fulltext-query-settings.html>`__   |
+-----------------------------------------+------------------------------------------------------+----------------------------------------------------------+
| 9.2.3. SetOverride                      | `Home <index.html>`__                                |  9.3. Full-text search query settings                    |
+-----------------------------------------+------------------------------------------------------+----------------------------------------------------------+

.. raw:: html

   </div>
