EscapeString
~~~~~~~~~~~~

<b>Prototype:</b> function EscapeString ( $string )

Escapes characters that are treated as special operators by the query
language parser. Returns an escaped string.

``$string`` is a string to escape.

This function might seem redundant because it's trivial to implement in
any calling application. However, as the set of special characters might
change over time, it makes sense to have an API call that is guaranteed
to escape all such characters at all times.

Usage example:

::


    $escaped = $cl->EscapeString ( "escaping-sample@query/string" );

