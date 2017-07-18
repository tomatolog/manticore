SetMaxQueryTime
~~~~~~~~~~~~~~~

<b>Prototype:</b> function SetMaxQueryTime ( $max\_query\_time )

Sets maximum search query time, in milliseconds. Parameter must be a
non-negative integer. Default value is 0 which means “do not limit”.

Similar to ``$cutoff`` setting from
`SetLimits() <../../general_query_settings/setlimits.html>`__, but limits
elapsed query time instead of processed matches count. Local search
queries will be stopped once that much time has elapsed. Note that if
you're performing a search which queries several local indexes, this
limit applies to each index separately.
