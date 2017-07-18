SetIndexWeights
~~~~~~~~~~~~~~~

<b>Prototype:</b> function SetIndexWeights ( $weights )

Sets per-index weights, and enables weighted summing of match weights
across different indexes. Parameter must be a hash (associative array)
mapping string index names to integer weights. Default is empty array
that means to disable weighting summing.

When a match with the same document ID is found in several different
local indexes, by default Sphinx simply chooses the match from the index
specified last in the query. This is to support searching through
partially overlapping index partitions.

However in some cases the indexes are not just partitions, and you might
want to sum the weights across the indexes instead of picking one.
``SetIndexWeights()`` lets you do that. With summing enabled, final
match weight in result set will be computed as a sum of match weight
coming from the given index multiplied by respective per-index weight
specified in this call. Ie. if the document 123 is found in index A with
the weight of 2, and also in index B with the weight of 3, and you
called
``SetIndexWeights ( array ( &quot;A&quot;=&gt;100, &quot;B&quot;=&gt;10 ) )``,
the final weight return to the client will be 2\ *100+3*\ 10 = 230.
