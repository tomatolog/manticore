### SetSortMode {#setsortmode}

&lt;b&gt;Prototype:&lt;/b&gt; function SetSortMode ( $mode, $sortby=&quot;&quot; )

Set matches sorting mode, as described in [the section called “Sorting modes”](../../sorting_modes.md). Parameter must be a constant specifying one of the known modes.

&lt;b&gt;WARNING:&lt;/b&gt; (PHP specific) you &lt;b&gt;must not&lt;/b&gt; take the matching mode constant name in quotes, that syntax specifies a string and is incorrect:

```

$cl->SetSortMode ( "SPH_SORT_ATTR_DESC" ); // INCORRECT! will not work as expected
$cl->SetSortMode ( SPH_SORT_ATTR_ASC ); // correct, works OK

```