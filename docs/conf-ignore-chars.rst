.. raw:: html

   <div class="navheader">

12.2.17. ignore\_chars
`Prev <conf-charset-table.html>`__ 
12.2. Index configuration options
 `Next <conf-min-prefix-len.html>`__

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

.. rubric:: 12.2.17. ignore\_chars
   :name: ignore_chars
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Ignored characters list. Optional, default is empty.

Useful in the cases when some characters, such as soft hyphenation mark
(U+00AD), should be not just treated as separators but rather fully
ignored. For example, if ‘-’ is simply not in the charset\_table,
“abc-def” text will be indexed as “abc” and “def” keywords. On the
contrary, if ‘-’ is added to ignore\_chars list, the same text will be
indexed as a single “abcdef” keyword.

The syntax is the same as for
`charset\_table <conf-charset-table.html>`__, but it’s only allowed to
declare characters, and not allowed to map them. Also, the ignored
characters must not be present in charset\_table.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    ignore_chars = U+AD

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------+----------------------------------------+
| `Prev <conf-charset-table.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-min-prefix-len.html>`__   |
+---------------------------------------+---------------------------------+----------------------------------------+
| 12.2.16. charset\_table               | `Home <index.html>`__           |  12.2.18. min\_prefix\_len             |
+---------------------------------------+---------------------------------+----------------------------------------+

.. raw:: html

   </div>
