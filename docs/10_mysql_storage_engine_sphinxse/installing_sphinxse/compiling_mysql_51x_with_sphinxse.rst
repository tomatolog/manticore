Compiling MySQL 5.1.x with ManticoreSE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. in MySQL sources directory, create ``storage/sphinx`` directory in
   and copy all files in ``mysqlse`` directory from Manticore sources
   there. Example:

   ::


       cp -R /root/builds/sphinx-0.9.7/mysqlse /root/builds/mysql-5.1.14/storage/sphinx

2. in MySQL sources directory, run

   ::


       sh BUILD/autorun.sh

3. configure MySQL and enable Manticore engine:

   ::


       ./configure --with-plugins=sphinx

4. build and install MySQL:

   ::


       make
       make install
