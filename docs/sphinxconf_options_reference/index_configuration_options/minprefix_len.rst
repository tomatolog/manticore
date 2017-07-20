min\_prefix\_len
~~~~~~~~~~~~~~~~

Minimum word prefix length to index. Optional, default is 0 (do not
index prefixes).

Prefix indexing allows to implement wildcard searching by 'wordstart\*'
wildcards. When mininum prefix length is set to a positive number,
indexer will index all the possible keyword prefixes (ie. word
beginnings) in addition to the keywords themselves. Too short prefixes
(below the minimum allowed length) will not be indexed.

For instance, indexing a keyword “example” with min\_prefix\_len=3 will
result in indexing “exa”, “exam”, “examp”, “exampl” prefixes along with
the word itself. Searches against such index for “exam” will match
documents that contain “example” word, even if they do not contain
“exam” on itself. However, indexing prefixes will make the index grow
significantly (because of many more indexed keywords), and will degrade
both indexing and searching times.

Perfect word matches can be differentiated from prefix matches, and
ranked higher, by utilizing all of the following options: a)
dict=keywords (on by default), b) index\_exact\_words=1 (off by
default), and c) expand\_keywords=1 (also off by default). Note that
either with the legacy dict=crc mode (which you should ditch anyway!),
or with any of the above options disable, there is no data to
differentiate between the prefixes and full words, and thus perfect word
matches can't be ranked higher.

Example:
^^^^^^^^

::


    min_prefix_len = 3

