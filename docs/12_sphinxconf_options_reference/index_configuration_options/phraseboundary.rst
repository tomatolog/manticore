phrase\_boundary
~~~~~~~~~~~~~~~~

Phrase boundary characters list. Optional, default is empty.

This list controls what characters will be treated as phrase boundaries,
in order to adjust word positions and enable phrase-level search
emulation through proximity search. The syntax is similar to
`charset\_table <../../index_configuration_options/charsettable.html>`__.
Mappings are not allowed and the boundary characters must not overlap
with anything else.

On phrase boundary, additional word position increment (specified by
`phrase\_boundary\_step <../../index_configuration_options/phraseboundary_step.html>`__)
will be added to current word position. This enables phrase-level
searching through proximity queries: words in different phrases will be
guaranteed to be more than phrase\_boundary\_step distance away from
each other; so proximity search within that distance will be equivalent
to phrase-level search.

Phrase boundary condition will be raised if and only if such character
is followed by a separator; this is to avoid abbreviations such as
S.T.A.L.K.E.R or URLs being treated as several phrases.

Example:
^^^^^^^^

::


    phrase_boundary = ., ?, !, U+2026 # horizontal ellipsis

