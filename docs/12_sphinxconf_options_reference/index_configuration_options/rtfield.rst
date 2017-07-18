rt\_field
~~~~~~~~~

Full-text field declaration. Multi-value, mandatory Introduced in
version 1.10-beta.

Full-text fields to be indexed are declared using ``rt_field``
directive. The names must be unique. The order is preserved; and so
field values in INSERT statements without an explicit list of inserted
columns will have to be in the same order as configured.

Example:
^^^^^^^^

::


    rt_field = author
    rt_field = title
    rt_field = content

