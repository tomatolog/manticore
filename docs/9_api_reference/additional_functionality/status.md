### Status {#status}

&lt;b&gt;Prototype:&lt;/b&gt; function Status ()

Queries searchd status, and returns an array of status variable name and value pairs.

Usage example:

```

$status = $cl->Status ();
foreach ( $status as $row )
    print join ( ": ", $row ) . "\n";

```