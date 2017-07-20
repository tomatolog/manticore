type
~~~~

Index type. Known values are ‘plain’, ‘distributed’, ‘rt’ and
‘template’. Optional, default is ‘plain’ (plain local index).

Sphinx supports several different types of indexes. Plain local indexes
are stored and processed on the local machine. Distributed indexes
involve not only local searching but querying remote ``searchd``
instances over the network as well (see `the section called “Distributed
searching” <../../distributed_searching.md>`__). Real-time indexes (or
RT indexes for short) are also stored and processed locally, but
additionally allow for on-the-fly updates of the full-text index (see
`Chapter 4, *Real-time
indexes* <../../4_real-time_indexes/README.md>`__). Note that
*attributes* can be updated on-the-fly using either plain local indexes
or RT ones. Template indexes are actually a pseudo-indexes because they
do not store any data. That means they do not create any files on your
hard drive. But you can use them for keywords and snippets generation,
which may be useful in some cases, and also as templates to inherit real
indexes from them.

Index type setting lets you choose the needed type. By default, plain
local index type will be assumed.

Example:
^^^^^^^^

::


    type = distributed

