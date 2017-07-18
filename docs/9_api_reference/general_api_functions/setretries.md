### SetRetries {#setretries}

&lt;b&gt;Prototype:&lt;/b&gt; function SetRetries ( $count, $delay=0 )

Sets distributed retry count and delay.

On temporary failures `searchd` will attempt up to `$count` retries per agent. `$delay` is the delay between the retries, in milliseconds. Retries are disabled by default. Note that this call will &lt;b&gt;not&lt;/b&gt; make the API itself retry on temporary failure; it only tells `searchd` to do so. Currently, the list of temporary failures includes all kinds of connect() failures and maxed out (too busy) remote agents.