.. raw:: html

   <div class="navheader">

12.1.44. mssql\_winauth
`Prev <conf-xmlpipe-fixup-utf8.html>`__ 
12.1. Data source configuration options
 `Next <conf-unpack-zlib.html>`__

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

.. rubric:: 12.1.44. mssql\_winauth
   :name: mssql_winauth
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

MS SQL Windows authentication flag. Boolean, optional, default value is
0 (false). Applies to ``mssql`` source type only. Introduced in version
0.9.9-rc1.

Whether to use currently logged in Windows account credentials for
authentication when connecting to MS SQL Server. Note that when running
``searchd`` as a service, account user can differ from the account you
used to install the service.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    mssql_winauth = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+-------------------------------------+
| `Prev <conf-xmlpipe-fixup-utf8.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-unpack-zlib.html>`__   |
+--------------------------------------------+----------------------------------+-------------------------------------+
| 12.1.43. xmlpipe\_fixup\_utf8              | `Home <index.html>`__            |  12.1.45. unpack\_zlib              |
+--------------------------------------------+----------------------------------+-------------------------------------+

.. raw:: html

   </div>
