.. raw:: html

   <div class="navheader">

12.2.22. infix\_fields
`Prev <conf-prefix-fields.html>`__ 
12.2. Index configuration options
 `Next <conf-ngram-len.html>`__

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

.. rubric:: 12.2.22. infix\_fields
   :name: infix_fields
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The list of full-text fields to limit infix indexing to. Applies to
dict=crc only. Optional, default is empty (index all fields in infix
mode).

Similar to `prefix\_fields <conf-prefix-fields.html>`__, but lets you
limit infix-indexing to given fields.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    infix_fields = url, domain

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+---------------------------------+-----------------------------------+
| `Prev <conf-prefix-fields.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-ngram-len.html>`__   |
+---------------------------------------+---------------------------------+-----------------------------------+
| 12.2.21. prefix\_fields               | `Home <index.html>`__           |  12.2.23. ngram\_len              |
+---------------------------------------+---------------------------------+-----------------------------------+

.. raw:: html

   </div>
