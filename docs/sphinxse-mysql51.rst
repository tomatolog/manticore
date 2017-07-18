.. raw:: html

   <div class="navheader">

10.2.2. Compiling MySQL 5.1.x with SphinxSE
`Prev <sphinxse-mysql50.html>`__ 
10.2. Installing SphinxSE
 `Next <sphinxse-checking.html>`__

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

.. rubric:: 10.2.2. Compiling MySQL 5.1.x with SphinxSE
   :name: compiling-mysql-5.1.x-with-sphinxse
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="orderedlist">

1. in MySQL sources directory, create ``storage/sphinx`` directory in
   and copy all files in ``mysqlse`` directory from Sphinx sources
   there. Example:

   .. code:: programlisting

       cp -R /root/builds/sphinx-0.9.7/mysqlse /root/builds/mysql-5.1.14/storage/sphinx

2. in MySQL sources directory, run

   .. code:: programlisting

       sh BUILD/autorun.sh

3. configure MySQL and enable Sphinx engine:

   .. code:: programlisting

       ./configure --with-plugins=sphinx

4. build and install MySQL:

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

+------------------------------------------------+-------------------------------------+-------------------------------------------+
| `Prev <sphinxse-mysql50.html>`__               | `Up <sphinxse-installing.html>`__   |  `Next <sphinxse-checking.html>`__        |
+------------------------------------------------+-------------------------------------+-------------------------------------------+
| 10.2.1. Compiling MySQL 5.0.x with SphinxSE    | `Home <index.html>`__               |  10.2.3. Checking SphinxSE installation   |
+------------------------------------------------+-------------------------------------+-------------------------------------------+

.. raw:: html

   </div>
