min\_stemming\_len
~~~~~~~~~~~~~~~~~~

Minimum word length at which to enable stemming. Optional, default is 1
(stem everything). Introduced in version 0.9.9-rc1.

Stemmers are not perfect, and might sometimes produce undesired results.
For instance, running “gps” keyword through Porter stemmer for English
results in “gp”, which is not really the intent. ``min_stemming_len``
feature lets you suppress stemming based on the source word length, ie.
to avoid stemming too short words. Keywords that are shorter than the
given threshold will not be stemmed. Note that keywords that are exactly
as long as specified <b>will</b> be stemmed. So in order to avoid
stemming 3-character keywords, you should specify 4 for the value. For
more finely grained control, refer to
`wordforms <../../index_configuration_options/wordforms.html>`__ feature.

Example:
^^^^^^^^

::


    min_stemming_len = 4

