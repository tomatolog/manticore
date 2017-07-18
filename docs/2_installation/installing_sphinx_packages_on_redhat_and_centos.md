## Installing Sphinx packages on RedHat and CentOS {#installing-sphinx-packages-on-redhat-and-centos}

Currently we distribute Sphinx RPMS and SRPMS on our website for both 5.x and 6.x versions of Red Hat Enterprise Linux, but they can be installed on CentOS as well.

1.  Before installation make sure you have these packages installed:

    **`$ yum install postgresql-libs unixODBC`**

2.  Download RedHat RPM from Sphinx website and install it:

    **`$ rpm -Uhv sphinx-2.2.1-1.rhel6.x86_64.rpm`**

3.  After preparing configuration file (see [Quick tour](../quick_sphinx_usage_tour.md)), you can start searchd daemon:

    **`$ service searchd start`**