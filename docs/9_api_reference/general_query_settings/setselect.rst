SetSelect
~~~~~~~~~

<b>Prototype:</b> function SetSelect ( $clause )

Sets the select clause, listing specific attributes to fetch, and
`expressions <../../5_searching/sorting_modes.rst#sph-sort-expr-mode>`__
to compute and fetch. Clause syntax mimics SQL. Introduced in version
0.9.9-rc1.

SetSelect() is very similar to the part of a typical SQL query between
SELECT and FROM. It lets you choose what attributes (columns) to fetch,
and also what expressions over the columns to compute and fetch. A
certain difference from SQL is that expressions <b>must</b> always be
aliased to a correct identifier (consisting of letters and digits) using
‘AS’ keyword. SQL also lets you do that but does not require to. Sphinx
enforces aliases so that the computation results can always be returned
under a “normal” name in the result set, used in other clauses, etc.

Everything else is basically identical to SQL. Star ('\*') is supported.
Functions are supported. Arbitrary amount of expressions is supported.
Computed expressions can be used for sorting, filtering, and grouping,
just as the regular attributes.

Starting with version 0.9.9-rc2, aggregate functions (AVG(), MIN(),
MAX(), SUM()) are supported when using GROUP BY.

Expression sorting (`the section called “SPH\_SORT\_EXPR
mode” <../../5_searching/sorting_modes.rst#sph-sort-expr-mode>`__) and
geodistance functions (`the section called
“SetGeoAnchor” <../../result_set_filtering_settings/setgeoanchor.rst>`__)
are now internally implemented using this computed expressions
mechanism, using magic names ‘@expr’ and ‘@geodist’ respectively.

Example:
^^^^^^^^

::


    $cl->SetSelect ( "*, @weight+(user_karma+ln(pageviews))*0.1 AS myweight" );
    $cl->SetSelect ( "exp_years, salary_gbp*{$gbp_usd_rate} AS salary_usd,
       IF(age>40,1,0) AS over40" );
    $cl->SetSelect ( "*, AVG(price) AS avgprice" );

