SetSortMode
~~~~~~~~~~~

<b>Prototype:</b> function SetSortMode ( $mode, $sortby=“” )

Set matches sorting mode, as described in `the section called “Sorting
modes” <../../sorting_modes.md>`__. Parameter must be a constant
specifying one of the known modes.

<b>WARNING:</b> (PHP specific) you <b>must not</b> take the matching
mode constant name in quotes, that syntax specifies a string and is
incorrect:

::


    $cl->SetSortMode ( "SPH_SORT_ATTR_DESC" ); // INCORRECT! will not work as expected
    $cl->SetSortMode ( SPH_SORT_ATTR_ASC ); // correct, works OK

