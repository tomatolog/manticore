UpdateAttributes
~~~~~~~~~~~~~~~~

<b>Prototype:</b> function UpdateAttributes ( $index, $attrs, $values,
$mva=false, $ignorenonexistent=false )

Instantly updates given attribute values in given documents. Returns
number of actually updated documents (0 or more) on success, or -1 on
failure.

``$index`` is a name of the index (or indexes) to be updated. ``$attrs``
is a plain array with string attribute names, listing attributes that
are updated. ``$values`` is a hash where key is document ID, and value
is a plain array of new attribute values. Optional boolean parameter
``mva`` points that there is update of MVA attributes. In this case the
:math:`values must be a dict with int key (document ID) and list of lists of int values (new MVA attribute values). Optional boolean parameter ``\ ignorenonexistent\`
(added in version 2.1.1-beta) points that the update will silently
ignore any warnings about trying to update a column which is not exists
in current index schema.

``$index`` can be either a single index name or a list, like in
``Query()``. Unlike ``Query()``, wildcard is not allowed and all the
indexes to update must be specified explicitly. The list of indexes can
include distributed index names. Updates on distributed indexes will be
pushed to all agents.

The updates only work with ``docinfo=extern`` storage strategy. They are
very fast because they're working fully in RAM, but they can also be
made persistent: updates are saved on disk on clean ``searchd`` shutdown
initiated by SIGTERM signal. With additional restrictions, updates are
also possible on MVA attributes; refer to
`mva\_updates\_pool <../../searchd_program_configuration_options/mvaupdates_pool.md>`__
directive for details.

Usage example:

::


    $cl->UpdateAttributes ( "test1", array("group_id"), array(1=>array(456)) );
    $cl->UpdateAttributes ( "products", array ( "price", "amount_in_stock" ),
        array ( 1001=>array(123,5), 1002=>array(37,11), 1003=>(25,129) ) );

The first sample statement will update document 1 in index “test1”,
setting “group\_id” to 456. The second one will update documents 1001,
1002 and 1003 in index “products”. For document 1001, the new price will
be set to 123 and the new amount in stock to 5; for document 1002, the
new price will be 37 and the new amount will be 11; etc.
