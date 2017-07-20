min\_infix\_len
~~~~~~~~~~~~~~~

Minimum infix prefix length to index and search. Optional, default is 0
(do not index infixes), and minimum allowed non-zero value is 2.

Infix length setting enables wildcard searches with term patterns like
‘start\ *', '*\ end’, ‘*middle*’, and so on. It also lets you disable
too short wildcards if those are too expensive to search for.

Perfect word matches can be differentiated from infix matches, and
ranked higher, by utilizing all of the following options: a)
dict=keywords (on by default), b) index\_exact\_words=1 (off by
default), and c) expand\_keywords=1 (also off by default). Note that
either with the legacy dict=crc mode (which you should ditch anyway!),
or with any of the above options disable, there is no data to
differentiate between the infixes and full words, and thus perfect word
matches can't be ranked higher.

However, query time might vary greatly, depending on how many keywords
the substring will actually expand to. Short and frequent syllables like
‘*in*’ or ‘*ti*’ just might expand to way too many keywords, all of
which would need to be matched and processed. Therefore, to generally
enable substring searches you would set min\_infix\_len to 2; and to
limit the impact from wildcard searches with too short wildcards, you
might set it higher.

Infixes must be at least 2 characters long, wildcards like ‘*a*’ are not
allowed for performance reasons. (While in theory it is possible to scan
the entire dictionary, identify keywords matching on just a single
character, expand ‘*a*’ to an OR operator over 100,000+ keywords, and
evaluate that expanded query, in practice this will very definitely kill
your server.)

Example:
^^^^^^^^

::


    min_infix_len = 3

