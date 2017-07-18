max\_substring\_len
~~~~~~~~~~~~~~~~~~~

Maximum substring (either prefix or infix) length to index. Optional,
default is 0 (do not limit indexed substrings). Applies to dict=crc
only.

By default, substring (either prefix or infix) indexing in the `dict=crc
mode <../../index_configuration_options/dict.md>`__ will index
<b>all</b> the possible substrings as separate keywords. That might
result in an overly large index. So the ``max_substring_len`` directive
lets you limit the impact of substring indexing by skipping too-long
substrings (which, chances are, will never get searched for anyway).

For example, a test index of 10,000 blog posts takes this much disk
space depending on the settings:

-  6.4 MB baseline (no substrings)
-  24.3 MB (3.8x) with min\_prefix\_len = 3
-  22.2 MB (3.5x) with min\_prefix\_len = 3, max\_substring\_len = 8
-  19.3 MB (3.0x) with min\_prefix\_len = 3, max\_substring\_len = 6
-  94.3 MB (14.7x) with min\_infix\_len = 3
-  84.6 MB (13.2x) with min\_infix\_len = 3, max\_substring\_len = 8
-  70.7 MB (11.0x) with min\_infix\_len = 3, max\_substring\_len = 6

So in this test limiting the max substring length saved us 10-15% on the
index size.

There is no performance impact associated with substring length when
using dict=keywords mode, so this directive is not applicable and
intentionally forbidden in that case. If required, you can still limit
the length of a substring that you search for in the application code.

Example:
^^^^^^^^

::


    max_substring_len = 12

