.. raw:: html

   <div class="navheader">

2.3. Installing Sphinx packages on Debian and Ubuntu
`Prev <compiling-source-problems.html>`__ 
Chapter 2. Installation
 `Next <installing-redhat.html>`__

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

.. rubric:: 2.3. Installing Sphinx packages on Debian and Ubuntu
   :name: installing-sphinx-packages-on-debian-and-ubuntu
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

There are two ways of getting Sphinx for Ubuntu: regular deb packages
and the Launchpad PPA repository.

Deb packages:

.. raw:: html

   <div class="orderedlist">

1. Sphinx requires a few libraries to be installed on Debian/Ubuntu. Use
   apt-get to download and install these dependencies:

   **``$ sudo apt-get install mysql-client unixodbc libpq5``**

2. Now you can install Sphinx:

   **``$ sudo dpkg -i sphinxsearch_2.3.2-beta-1~trusty_amd64.deb``**

.. raw:: html

   </div>

PPA repository (Ubuntu only).

Installing Sphinx is much easier from Sphinxsearch PPA repository,
because you will get all dependencies and can also update Sphinx to the
latest version with the same command.

.. raw:: html

   <div class="orderedlist">

1. First, add Sphinxsearch repository and update the list of packages:

   **``$ sudo add-apt-repository ppa:builds/sphinxsearch-rel23``**

   **``$ sudo apt-get update``**

2. Install/update sphinxsearch package:

   **``$ sudo apt-get install sphinxsearch``**

.. raw:: html

   </div>

Sphinx ``searchd`` daemon can be started/stopped using service command:

**``$ sudo service sphinxsearch start``**

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+------------------------------+---------------------------------------------------------+
| `Prev <compiling-source-problems.html>`__    | `Up <installation.html>`__   |  `Next <installing-redhat.html>`__                      |
+----------------------------------------------+------------------------------+---------------------------------------------------------+
| 2.2.3. Known compilation issues              | `Home <index.html>`__        |  2.4. Installing Sphinx packages on RedHat and CentOS   |
+----------------------------------------------+------------------------------+---------------------------------------------------------+

.. raw:: html

   </div>
