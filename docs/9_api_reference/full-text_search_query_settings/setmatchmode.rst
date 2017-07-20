SetMatchMode
~~~~~~~~~~~~

<b>DEPRECATED</b>

<b>Prototype:</b> function SetMatchMode ( $mode )

Sets full-text query matching mode, as described in `the section called
“Matching modes” <../../matching_modes.md>`__. Parameter must be a
constant specifying one of the known modes.

<b>WARNING:</b> (PHP specific) you <b>must not</b> take the matching
mode constant name in quotes, that syntax specifies a string and is
incorrect:

::


    $cl->SetMatchMode ( "SPH_MATCH_ANY" ); // INCORRECT! will not work as expected
    $cl->SetMatchMode ( SPH_MATCH_ANY ); // correct, works OK

