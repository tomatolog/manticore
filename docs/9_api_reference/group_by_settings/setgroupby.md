### SetGroupBy {#setgroupby}

&lt;b&gt;Prototype:&lt;/b&gt; function SetGroupBy ( $attribute, $func, $groupsort=&quot;@group desc&quot; )

Sets grouping attribute, function, and groups sorting mode; and enables grouping (as described in [the section called “Grouping (clustering) search results ”](../../grouping_clustering_search_results.md)).

`$attribute` is a string that contains group-by attribute name. `$func` is a constant that chooses a function applied to the attribute value in order to compute group-by key. `$groupsort` is a clause that controls how the groups will be sorted. Its syntax is similar to that described in [the section called “SPH_SORT_EXTENDED mode”](../../5_searching/sorting_modes.md#sph-sort-extended-mode).

Grouping feature is very similar in nature to GROUP BY clause from SQL. Results produces by this function call are going to be the same as produced by the following pseudo code:

```

SELECT ... GROUP BY $func($attribute) ORDER BY $groupsort

```

Note that it&#039;s `$groupsort` that affects the order of matches in the final result set. Sorting mode (see [the section called “SetSortMode”](../../full-text_search_query_settings/setsortmode.md)) affect the ordering of matches _within_ group, ie. what match will be selected as the best one from the group. So you can for instance order the groups by matches count and select the most relevant match within each group at the same time.

Starting with version 0.9.9-rc2, aggregate functions (AVG(), MIN(), MAX(), SUM()) are supported through [SetSelect()](../../general_query_settings/setselect.md) API call when using GROUP BY.

Starting with version 2.0.1-beta, grouping on string attributes is supported, with respect to current collation.