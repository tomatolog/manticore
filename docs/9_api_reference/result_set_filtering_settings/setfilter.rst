SetFilter
~~~~~~~~~

<b>Prototype:</b> function SetFilter ( $attribute, $values,
$exclude=false )

Adds new integer values set filter.

On this call, additional new filter is added to the existing list of
filters. ``$attribute`` must be a string with attribute name.
``$values`` must be a plain array containing integer values.
``$exclude`` must be a boolean value; it controls whether to accept the
matching documents (default mode, when ``$exclude`` is false) or reject
them.

Only those documents where ``$attribute`` column value stored in the
index matches any of the values from ``$values`` array will be matched
(or rejected, if ``$exclude`` is true).
