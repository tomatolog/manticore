.. raw:: html

   <div class="navheader">

12.4.33. collation\_libc\_locale
`Prev <conf-collation-server.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-mysql-version-string.html>`__

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

.. rubric:: 12.4.33. collation\_libc\_locale
   :name: collation_libc_locale
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Server libc locale. Optional, default is C. Introduced in version
2.0.1-beta.

Specifies the libc locale, affecting the libc-based collations. Refer to
`Section 5.13, “Collations” <collations.html>`__ section for the
details.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    collation_libc_locale = fr_FR

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+-----------------------------------+----------------------------------------------+
| `Prev <conf-collation-server.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-mysql-version-string.html>`__   |
+------------------------------------------+-----------------------------------+----------------------------------------------+
| 12.4.32. collation\_server               | `Home <index.html>`__             |  12.4.34. mysql\_version\_string             |
+------------------------------------------+-----------------------------------+----------------------------------------------+

.. raw:: html

   </div>
