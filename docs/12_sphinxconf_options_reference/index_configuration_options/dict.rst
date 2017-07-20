dict
~~~~

The keywords dictionary type. Known values are ‘crc’ and ‘keywords’.
‘crc’ is DEPRECATED. Use ‘keywords’ instead. Optional, default is
‘keywords’.

Keywords dictionary mode (dict=keywords), (greatly) reduces indexing
impact and enable substring searches on huge collections. They also
eliminate the chance of CRC32 collisions. That mode supported both for
disk and RT indexes.

CRC dictionaries never store the original keyword text in the index.
Instead, keywords are replaced with their control sum value (either
CRC32 or FNV64, depending whether Sphinx was built with
``--enable-id64``) both when searching and indexing, and that value is
used internally in the index.

That approach has two drawbacks. First, in CRC32 case there is a chance
of control sum collision between several pairs of different keywords,
growing quadratically with the number of unique keywords in the index.
(FNV64 case is unaffected in practice, as a chance of a single FNV64
collision in a dictionary of 1 billion entries is approximately 1:16, or
6.25 percent. And most dictionaries will be much more compact that a
billion keywords, as a typical spoken human language has in the region
of 1 to 10 million word forms.) Second, and more importantly, substring
searches are not directly possible with control sums. Sphinx alleviated
that by pre-indexing all the possible substrings as separate keywords
(see `the section called
“min\_prefix\_len” <../../index_configuration_options/minprefix_len.md>`__,
`the section called
“min\_infix\_len” <../../index_configuration_options/mininfix_len.md>`__
directives). That actually has an added benefit of matching substrings
in the quickest way possible. But at the same time pre-indexing all
substrings grows the index size a lot (factors of 3-10x and even more
would not be unusual) and impacts the indexing time respectively,
rendering substring searches on big indexes rather impractical.

Keywords dictionary fixes both these drawbacks. It stores the keywords
in the index and performs search-time wildcard expansion. For example, a
search for a 'test\*‘prefix could internally expand to
'test\|tests\|testing’ query based on the dictionary contents. That
expansion is fully transparent to the application, except that the
separate per-keyword statistics for all the actually matched keywords
would now also be reported.

For substring (infix) search extended wildcards may be used. Special
symbols like ‘?’ and ‘%’ are supported along with substring (infix)
search (e.g. “t?st\ *“,”run%“,”*\ abc\*“). Note, however, these
wildcards work only with dict=keywords, and not elsewhere.

Indexing with keywords dictionary should be 1.1x to 1.3x slower compared
to regular, non-substring indexing - but times faster compared to
substring indexing (either prefix or infix). Index size should only be
slightly bigger that than of the regular non-substring index, with a
1..10% percent total difference. Regular keyword searching time must be
very close or identical across all three discussed index kinds (CRC
non-substring, CRC substring, keywords). Substring searching time can
vary greatly depending on how many actual keywords match the given
substring (in other words, into how many keywords does the search term
expand). The maximum number of keywords matched is restricted by the
`expansion\_limit <../../searchd_program_configuration_options/expansionlimit.md>`__
directive.

Essentially, keywords and CRC dictionaries represent the two different
trade-off substring searching decisions. You can choose to either
sacrifice indexing time and index size in favor of top-speed worst-case
searches (CRC dictionary), or only slightly impact indexing time but
sacrifice worst-case searching time when the prefix expands into very
many keywords (keywords dictionary).

Example:
^^^^^^^^

::


    dict = keywords

