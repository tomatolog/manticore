.. raw:: html

   <div class="navheader">

2.4. Installing Sphinx packages on RedHat and CentOS
`Prev <installing-debian.html>`__ 
Chapter 2. Installation
 `Next <installing-windows.html>`__

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

.. rubric:: 2.4. Installing Sphinx packages on RedHat and CentOS
   :name: installing-sphinx-packages-on-redhat-and-centos
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Currently we distribute Sphinx RPMS and SRPMS on our website for both
5.x and 6.x versions of Red Hat Enterprise Linux, but they can be
installed on CentOS as well.

.. raw:: html

   <div class="orderedlist">

1. Before installation make sure you have these packages installed:

   **``$ yum install postgresql-libs unixODBC``**

2. Download RedHat RPM from Sphinx website and install it:

   **``$ rpm -Uhv sphinx-2.2.1-1.rhel6.x86_64.rpm``**

3. After preparing configuration file (see `Quick
   tour <quick-tour.html>`__), you can start searchd daemon:

   **``$ service searchd start``**

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------------------+------------------------------+---------------------------------------+
| `Prev <installing-debian.html>`__                       | `Up <installation.html>`__   |  `Next <installing-windows.html>`__   |
+---------------------------------------------------------+------------------------------+---------------------------------------+
| 2.3. Installing Sphinx packages on Debian and Ubuntu    | `Home <index.html>`__        |  2.5. Installing Sphinx on Windows    |
+---------------------------------------------------------+------------------------------+---------------------------------------+

.. raw:: html

   </div>
