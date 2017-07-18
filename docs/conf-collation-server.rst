.. raw:: html

   <div class="navheader">

12.4.32. collation\_server
`Prev <conf-snippets-file-prefix.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-collation-libc-locale.html>`__

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

.. rubric:: 12.4.32. collation\_server
   :name: collation_server
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Default server collation. Optional, default is libc\_ci. Introduced in
version 2.0.1-beta.

Specifies the default collation used for incoming requests. The
collation can be overridden on a per-query basis. Refer to
`Section 5.13, “Collations” <collations.html>`__ section for the list of
available collations and other details.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    collation_server = utf8_ci

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+-----------------------------------+-----------------------------------------------+
| `Prev <conf-snippets-file-prefix.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-collation-libc-locale.html>`__   |
+----------------------------------------------+-----------------------------------+-----------------------------------------------+
| 12.4.31. snippets\_file\_prefix              | `Home <index.html>`__             |  12.4.33. collation\_libc\_locale             |
+----------------------------------------------+-----------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
