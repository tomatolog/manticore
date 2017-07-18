### SetIDRange {#setidrange}

&lt;b&gt;Prototype:&lt;/b&gt; function SetIDRange ( $min, $max )

Sets an accepted range of document IDs. Parameters must be integers. Defaults are 0 and 0; that combination means to not limit by range.

After this call, only those records that have document ID between `$min` and `$max` (including IDs exactly equal to `$min` or `$max`) will be matched.