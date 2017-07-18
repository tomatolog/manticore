.. raw:: html

   <div class="navheader">

12.4.34. mysql\_version\_string
`Prev <conf-collation-libc-locale.html>`__ 
12.4. \ ``searchd`` program configuration options
 `Next <conf-rt-flush-period.html>`__

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

.. rubric:: 12.4.34. mysql\_version\_string
   :name: mysql_version_string
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A server version string to return via MySQL protocol. Optional, default
is empty (return Sphinx version). Introduced in version 2.0.1-beta.

Several picky MySQL client libraries depend on a particular version
number format used by MySQL, and moreover, sometimes choose a different
execution path based on the reported version number (rather than the
indicated capabilities flags). For instance, Python MySQLdb 1.2.2 throws
an exception when the version number is not in X.Y.ZZ format; MySQL .NET
connector 6.3.x fails internally on version numbers 1.x along with a
certain combination of flags, etc. To workaround that, you can use
``mysql_version_string`` directive and have ``searchd`` report a
different version to clients connecting over MySQL protocol. (By
default, it reports its own version.)

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mysql_version_string = 5.0.37

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+-----------------------------------+-----------------------------------------+
| `Prev <conf-collation-libc-locale.html>`__    | `Up <confgroup-searchd.html>`__   |  `Next <conf-rt-flush-period.html>`__   |
+-----------------------------------------------+-----------------------------------+-----------------------------------------+
| 12.4.33. collation\_libc\_locale              | `Home <index.html>`__             |  12.4.35. rt\_flush\_period             |
+-----------------------------------------------+-----------------------------------+-----------------------------------------+

.. raw:: html

   </div>
