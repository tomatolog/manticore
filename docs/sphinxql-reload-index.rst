.. raw:: html

   <div class="navheader">

8.45. RELOAD INDEX syntax
`Prev <sphinxql-threads.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-multi-queries.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 8.45. RELOAD INDEX syntax
   :name: reload-index-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    RELOAD INDEX idx [ FROM '/path/to/index_files' ]

RELOAD INDEX, added in 2.3.1-beta, allows you to rotate indexes using
SphinxQL.

It has two modes of operation. First one (without specifying a path)
makes Sphinx daemon check for new index files in directory specified in
`Section 12.2.3, “path” <conf-path.html>`__. New index files must have a
idx.new.sp? names.

And if you additionally specify a path, daemon will look for index files
in specified directory, move them to index `Section 12.2.3,
“path” <conf-path.html>`__, rename from index\_files.sp? to idx.new.sp?
and rotate them.

.. code:: programlisting

    mysql> RELOAD INDEX plain_index;
    mysql> RELOAD INDEX plain_index FROM '/home/mighty/new_index_files';

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+------------------------------------+-------------------------------------------+
| `Prev <sphinxql-threads.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-multi-queries.html>`__   |
+-------------------------------------+------------------------------------+-------------------------------------------+
| 8.44. SHOW THREADS syntax           | `Home <index.html>`__              |  8.46. Multi-statement queries            |
+-------------------------------------+------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
