SetArrayResult
~~~~~~~~~~~~~~

<b>Prototype:</b> function SetArrayResult ( $arrayresult )

PHP specific. Controls matches format in the search results set (whether
matches should be returned as an array or a hash).

``$arrayresult`` argument must be boolean. If ``$arrayresult`` is
``false`` (the default mode), matches will returned in PHP hash format
with document IDs as keys, and other information (weight, attributes) as
values. If ``$arrayresult`` is true, matches will be returned as a plain
array with complete per-match information including document ID.

Introduced along with GROUP BY support on MVA attributes. Group-by-MVA
result sets may contain duplicate document IDs. Thus they need to be
returned as plain arrays, because hashes will only keep one entry per
document ID.
