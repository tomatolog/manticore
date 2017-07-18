SetFilterRange
~~~~~~~~~~~~~~

<b>Prototype:</b> function SetFilterRange ( $attribute, $min, $max,
$exclude=false )

Adds new integer range filter.

On this call, additional new filter is added to the existing list of
filters. ``$attribute`` must be a string with attribute name. ``$min``
and ``$max`` must be integers that define the acceptable attribute
values range (including the boundaries). ``$exclude`` must be a boolean
value; it controls whether to accept the matching documents (default
mode, when ``$exclude`` is false) or reject them.

Only those documents where ``$attribute`` column value stored in the
index is between ``$min`` and ``$max`` (including values that are
exactly equal to ``$min`` or ``$max``) will be matched (or rejected, if
``$exclude`` is true).
