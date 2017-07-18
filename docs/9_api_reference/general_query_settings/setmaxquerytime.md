### SetMaxQueryTime {#setmaxquerytime}

&lt;b&gt;Prototype:&lt;/b&gt; function SetMaxQueryTime ( $max_query_time )

Sets maximum search query time, in milliseconds. Parameter must be a non-negative integer. Default value is 0 which means &quot;do not limit&quot;.

Similar to `$cutoff` setting from [SetLimits()](../../general_query_settings/setlimits.md), but limits elapsed query time instead of processed matches count. Local search queries will be stopped once that much time has elapsed. Note that if you&#039;re performing a search which queries several local indexes, this limit applies to each index separately.