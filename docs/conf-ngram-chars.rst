.. raw:: html

   <div class="navheader">

12.2.24. ngram\_chars
`Prev <conf-ngram-len.html>`__ 
12.2. Index configuration options
 `Next <conf-phrase-boundary.html>`__

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

.. rubric:: 12.2.24. ngram\_chars
   :name: ngram_chars
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

N-gram characters list. Optional, default is empty.

To be used in conjunction with in `ngram\_len <conf-ngram-len.html>`__,
this list defines characters, sequences of which are subject to N-gram
extraction. Words comprised of other characters will not be affected by
N-gram indexing feature. The value format is identical to
`charset\_table <conf-charset-table.html>`__.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    ngram_chars = U+3000..U+2FA1F

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+---------------------------------+-----------------------------------------+
| `Prev <conf-ngram-len.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-phrase-boundary.html>`__   |
+-----------------------------------+---------------------------------+-----------------------------------------+
| 12.2.23. ngram\_len               | `Home <index.html>`__           |  12.2.25. phrase\_boundary              |
+-----------------------------------+---------------------------------+-----------------------------------------+

.. raw:: html

   </div>
