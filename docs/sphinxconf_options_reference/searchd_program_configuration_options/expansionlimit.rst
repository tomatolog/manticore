expansion\_limit
~~~~~~~~~~~~~~~~

The maximum number of expanded keywords for a single wildcard. Optional,
default is 0 (no limit).

When doing substring searches against indexes built with
``dict = keywords`` enabled, a single wildcard may potentially result in
thousands and even millions of matched keywords (think of matching 'a\*'
against the entire Oxford dictionary). This directive lets you limit the
impact of such expansions. Setting ``expansion_limit = N`` restricts
expansions to no more than N of the most frequent matching keywords (per
each wildcard in the query).

Example:
^^^^^^^^

::


    expansion_limit = 16

