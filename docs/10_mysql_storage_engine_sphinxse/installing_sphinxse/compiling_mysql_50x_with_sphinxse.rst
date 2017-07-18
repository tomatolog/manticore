Compiling MySQL 5.0.x with SphinxSE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. copy ``sphinx.5.0.yy.diff`` patch file into MySQL sources directory
   and run

   ::


       patch -p1 < sphinx.5.0.yy.diff

   If there's no .diff file exactly for the specific version you need to
   build, try applying .diff with closest version numbers. It is
   important that the patch should apply with no rejects.

2. in MySQL sources directory, run

   ::


       sh BUILD/autorun.sh

3. in MySQL sources directory, create ``sql/sphinx`` directory in and
   copy all files in ``mysqlse`` directory from Sphinx sources there.
   Example:

   ::


       cp -R /root/builds/sphinx-0.9.7/mysqlse /root/builds/mysql-5.0.24/sql/sphinx

4. configure MySQL and enable Sphinx engine:

   ::


       ./configure --with-sphinx-storage-engine

5. build and install MySQL:

   ::


       make
       make install
