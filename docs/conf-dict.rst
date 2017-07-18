.. raw:: html

   <div class="navheader">

12.2.7. dict
`Prev <conf-morphology.html>`__ 
12.2. Index configuration options
 `Next <conf-index-sp.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 12.2.7. dict
   :name: dict
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The keywords dictionary type. Known values are ‘crc’ and ‘keywords’.
‘crc’ is DEPRECATED. Use ‘keywords’ instead. Optional, default is
‘keywords’. Introduced in version 2.0.1-beta.

CRC dictionary mode (dict=crc) is the default dictionary type in Sphinx,
and the only one available until version 2.0.1-beta. Keywords dictionary
mode (dict=keywords) was added in 2.0.1-beta, primarily to (greatly)
reduce indexing impact and enable substring searches on huge
collections. They also eliminate the chance of CRC32 collisions. In
2.0.1-beta, that mode was only supported for disk indexes. Starting with
2.0.2-beta, RT indexes are also supported.

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
(see `Section 12.2.18, “min\_prefix\_len” <conf-min-prefix-len.html>`__,
`Section 12.2.19, “min\_infix\_len” <conf-min-infix-len.html>`__
directives). That actually has an added benefit of matching substrings
in the quickest way possible. But at the same time pre-indexing all
substrings grows the index size a lot (factors of 3-10x and even more
would not be unusual) and impacts the indexing time respectively,
rendering substring searches on big indexes rather impractical.

Keywords dictionary, introduced in 2.0.1-beta, fixes both these
drawbacks. It stores the keywords in the index and performs search-time
wildcard expansion. For example, a search for a ‘test\*’ prefix could
internally expand to ‘test\|tests\|testing’ query based on the
dictionary contents. That expansion is fully transparent to the
application, except that the separate per-keyword statistics for all the
actually matched keywords would now also be reported.

Version 2.1.1-beta introduced extended wildcards support, now special
symbols like ‘?’ and ‘%’ are supported along with substring (infix)
search (e.g. “t?st\*”, “run%”, “\*abc\*”). Note, however, these
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
`expansion\_limit <conf-expansion-limit.html>`__ directive.

Essentially, keywords and CRC dictionaries represent the two different
trade-off substring searching decisions. You can choose to either
sacrifice indexing time and index size in favor of top-speed worst-case
searches (CRC dictionary), or only slightly impact indexing time but
sacrifice worst-case searching time when the prefix expands into very
many keywords (keywords dictionary).

.. rubric:: Example:
   :name: example

.. code:: programlisting

    dict = keywords

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------+---------------------------------+----------------------------------+
| `Prev <conf-morphology.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-index-sp.html>`__   |
+------------------------------------+---------------------------------+----------------------------------+
| 12.2.6. morphology                 | `Home <index.html>`__           |  12.2.8. index\_sp               |
+------------------------------------+---------------------------------+----------------------------------+

.. raw:: html

   </div>
