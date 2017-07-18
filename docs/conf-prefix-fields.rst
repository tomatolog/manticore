.. raw:: html

   <div class="navheader">

12.2.21. prefix\_fields
`Prev <conf-max-substring-len.html>`__ 
12.2. Index configuration options
 `Next <conf-infix-fields.html>`__

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

.. rubric:: 12.2.21. prefix\_fields
   :name: prefix_fields
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The list of full-text fields to limit prefix indexing to. Applies to
dict=crc only. Optional, default is empty (index all fields in prefix
mode).

Because prefix indexing impacts both indexing and searching performance,
it might be desired to limit it to specific full-text fields only: for
instance, to provide prefix searching through URLs, but not through page
contents. prefix\_fields specifies what fields will be prefix-indexed;
all other fields will be indexed in normal mode. The value format is a
comma-separated list of field names.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    prefix_fields = url, domain

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+---------------------------------+--------------------------------------+
| `Prev <conf-max-substring-len.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-infix-fields.html>`__   |
+-------------------------------------------+---------------------------------+--------------------------------------+
| 12.2.20. max\_substring\_len              | `Home <index.html>`__           |  12.2.22. infix\_fields              |
+-------------------------------------------+---------------------------------+--------------------------------------+

.. raw:: html

   </div>
