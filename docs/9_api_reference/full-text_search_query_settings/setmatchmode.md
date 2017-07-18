### SetMatchMode {#setmatchmode}

&lt;b&gt;DEPRECATED&lt;/b&gt;

&lt;b&gt;Prototype:&lt;/b&gt; function SetMatchMode ( $mode )

Sets full-text query matching mode, as described in [the section called “Matching modes”](../../matching_modes.md). Parameter must be a constant specifying one of the known modes.

&lt;b&gt;WARNING:&lt;/b&gt; (PHP specific) you &lt;b&gt;must not&lt;/b&gt; take the matching mode constant name in quotes, that syntax specifies a string and is incorrect:

```

$cl->SetMatchMode ( "SPH_MATCH_ANY" ); // INCORRECT! will not work as expected
$cl->SetMatchMode ( SPH_MATCH_ANY ); // correct, works OK

```