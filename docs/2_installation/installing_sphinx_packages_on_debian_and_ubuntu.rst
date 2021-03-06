Installing Manticore packages on Debian and Ubuntu
-----------------------------------------------

There are two ways of getting Manticore for Ubuntu: regular deb packages
and the Launchpad PPA repository.

Deb packages:

1. Manticore requires a few libraries to be installed on Debian/Ubuntu. Use
   apt-get to download and install these dependencies:

   **``$ sudo apt-get install mysql-client unixodbc libpq5``**
2. Now you can install Manticore:

   **``$ sudo dpkg -i sphinxsearch_2.3.2-beta-1~trusty_amd64.deb``**

PPA repository (Ubuntu only).

Installing Manticore is much easier from Manticoresearch PPA repository,
because you will get all dependencies and can also update Manticore to the
latest version with the same command.

1. First, add Manticoresearch repository and update the list of packages:

   **``$ sudo add-apt-repository ppa:builds/sphinxsearch-rel23``**

   **``$ sudo apt-get update``**

2. Install/update sphinxsearch package:

   **``$ sudo apt-get install sphinxsearch``**

Manticore ``searchd`` daemon can be started/stopped using service command:

**``$ sudo service sphinxsearch start``**
