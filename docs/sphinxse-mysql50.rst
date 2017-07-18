.. raw:: html

   <div class="navheader">

10.2.1. Compiling MySQL 5.0.x with SphinxSE
`Prev <sphinxse-installing.html>`__ 
10.2. Installing SphinxSE
 `Next <sphinxse-mysql51.html>`__

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

.. rubric:: 10.2.1. Compiling MySQL 5.0.x with SphinxSE
   :name: compiling-mysql-5.0.x-with-sphinxse
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="orderedlist">

1. copy ``sphinx.5.0.yy.diff`` patch file into MySQL sources directory
   and run

   .. code:: programlisting

       patch -p1 < sphinx.5.0.yy.diff

   If there’s no .diff file exactly for the specific version you need to
   build, try applying .diff with closest version numbers. It is
   important that the patch should apply with no rejects.

2. in MySQL sources directory, run

   .. code:: programlisting

       sh BUILD/autorun.sh

3. in MySQL sources directory, create ``sql/sphinx`` directory in and
   copy all files in ``mysqlse`` directory from Sphinx sources there.
   Example:

   .. code:: programlisting

       cp -R /root/builds/sphinx-0.9.7/mysqlse /root/builds/mysql-5.0.24/sql/sphinx

4. configure MySQL and enable Sphinx engine:

   .. code:: programlisting

       ./configure --with-sphinx-storage-engine

5. build and install MySQL:

   .. code:: programlisting

       make
       make install

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+-------------------------------------+------------------------------------------------+
| `Prev <sphinxse-installing.html>`__    | `Up <sphinxse-installing.html>`__   |  `Next <sphinxse-mysql51.html>`__              |
+----------------------------------------+-------------------------------------+------------------------------------------------+
| 10.2. Installing SphinxSE              | `Home <index.html>`__               |  10.2.2. Compiling MySQL 5.1.x with SphinxSE   |
+----------------------------------------+-------------------------------------+------------------------------------------------+

.. raw:: html

   </div>
