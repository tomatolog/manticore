.. raw:: html

   <div class="navheader">

12.2.50. rt\_field
`Prev <conf-rt-mem-limit.html>`__ 
12.2. Index configuration options
 `Next <conf-rt-attr-uint.html>`__

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

.. rubric:: 12.2.50. rt\_field
   :name: rt_field
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Full-text field declaration. Multi-value, mandatory Introduced in
version 1.10-beta.

Full-text fields to be indexed are declared using ``rt_field``
directive. The names must be unique. The order is preserved; and so
field values in INSERT statements without an explicit list of inserted
columns will have to be in the same order as configured.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    rt_field = author
    rt_field = title
    rt_field = content

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+---------------------------------+--------------------------------------+
| `Prev <conf-rt-mem-limit.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-rt-attr-uint.html>`__   |
+--------------------------------------+---------------------------------+--------------------------------------+
| 12.2.49. rt\_mem\_limit              | `Home <index.html>`__           |  12.2.51. rt\_attr\_uint             |
+--------------------------------------+---------------------------------+--------------------------------------+

.. raw:: html

   </div>
