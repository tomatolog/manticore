.. raw:: html

   <div class="navheader">

12.2.15. min\_word\_len
`Prev <conf-exceptions.html>`__ 
12.2. Index configuration options
 `Next <conf-charset-table.html>`__

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

.. rubric:: 12.2.15. min\_word\_len
   :name: min_word_len
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Minimum indexed word length. Optional, default is 1 (index everything).

Only those words that are not shorter than this minimum will be indexed.
For instance, if min\_word\_len is 4, then ‘the’ won’t be indexed, but
‘they’ will be.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    min_word_len = 4

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------+---------------------------------+---------------------------------------+
| `Prev <conf-exceptions.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-charset-table.html>`__   |
+------------------------------------+---------------------------------+---------------------------------------+
| 12.2.14. exceptions                | `Home <index.html>`__           |  12.2.16. charset\_table              |
+------------------------------------+---------------------------------+---------------------------------------+

.. raw:: html

   </div>
