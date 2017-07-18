.. raw:: html

   <div class="navheader">

12.2.20. max\_substring\_len
`Prev <conf-min-infix-len.html>`__ 
12.2. Index configuration options
 `Next <conf-prefix-fields.html>`__

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

.. rubric:: 12.2.20. max\_substring\_len
   :name: max_substring_len
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Maximum substring (either prefix or infix) length to index. Optional,
default is 0 (do not limit indexed substrings). Applies to dict=crc
only.

By default, substring (either prefix or infix) indexing in the `dict=crc
mode <conf-dict.html>`__ will index **all** the possible substrings as
separate keywords. That might result in an overly large index. So the
``max_substring_len`` directive lets you limit the impact of substring
indexing by skipping too-long substrings (which, chances are, will never
get searched for anyway).

For example, a test index of 10,000 blog posts takes this much disk
space depending on the settings:

.. raw:: html

   <div class="itemizedlist">

-  6.4 MB baseline (no substrings)
-  24.3 MB (3.8x) with min\_prefix\_len = 3
-  22.2 MB (3.5x) with min\_prefix\_len = 3, max\_substring\_len = 8
-  19.3 MB (3.0x) with min\_prefix\_len = 3, max\_substring\_len = 6
-  94.3 MB (14.7x) with min\_infix\_len = 3
-  84.6 MB (13.2x) with min\_infix\_len = 3, max\_substring\_len = 8
-  70.7 MB (11.0x) with min\_infix\_len = 3, max\_substring\_len = 6

.. raw:: html

   </div>

So in this test limiting the max substring length saved us 10-15% on the
index size.

There is no performance impact associated with substring length when
using dict=keywords mode, so this directive is not applicable and
intentionally forbidden in that case. If required, you can still limit
the length of a substring that you search for in the application code.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    max_substring_len = 12

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------+---------------------------------------+
| `Prev <conf-min-infix-len.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-prefix-fields.html>`__   |
+---------------------------------------+---------------------------------+---------------------------------------+
| 12.2.19. min\_infix\_len              | `Home <index.html>`__           |  12.2.21. prefix\_fields              |
+---------------------------------------+---------------------------------+---------------------------------------+

.. raw:: html

   </div>
