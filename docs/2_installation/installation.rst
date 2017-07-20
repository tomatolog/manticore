Installation
=======================
Supported systems
-----------------

Sphinx can be compiled either from source or installed using prebuilt
packages. Most modern UNIX systems with a C++ compiler should be able to
compile and run Sphinx without any modifications.

Currently known systems Sphinx has been successfully running on are:

-  Linux 2.4.x, 2.6.x, 3.x, 4.x (many various distributions)

-  Windows 7, 8, 10

-  FreeBSD 4.x, 5.x, 6.x, 7.x, 8.x

-  NetBSD 1.6, 3.0

-  Solaris 9, 11

-  Mac OS X

CPU architectures known to work include i386 (aka x86), amd64 (aka
x86\_64), SPARC64, and ARM.

Chances are good that Sphinx should work on other Unix platforms and/or
CPU architectures just as well. Please report any other platforms that
worked for you!

All platforms are production quality. There are no principal functional
limitations on any platform.

Compiling Sphinx from source
----------------------------
Required tools
~~~~~~~~~~~~~~

On UNIX, you will need the following tools to build and install Sphinx:

-  a working C++ compiler. GNU gcc and clang are known to work.

-  a good make program. GNU make is known to work.

On Windows, you will need Microsoft Visual C/C++ Studio 2013 or above.
Other compilers/environments will probably work as well, but for the
time being, you will have to build makefile (or other environment
specific project files) manually.
Compiling on Linux
~~~~~~~~~~~~~~~~~~

1. Extract everything from the distribution tarball (haven't you
   already?) and go to the ``sphinx`` subdirectory. (We are using
   version 2.3.2-beta here for the sake of example only; be sure to
   change this to a specific version you're using.)

   ::

       $ tar xzvf sphinx-2.3.2-beta.tar.gz
       $ cd sphinx

2. Run the configuration program:

   ::

       $ ./configure

   There's a number of options to configure. The complete listing may be
   obtained by using ``--help`` switch. The most important ones are:

   -  ``--prefix``, which specifies where to install Sphinx; such as
      ``--prefix=/usr/local/sphinx`` (all of the examples use this
      prefix)

   -  ``--with-mysql``, which specifies where to look for MySQL include
      and library files, if auto-detection fails;

   -  ``--with-static-mysql``, which builds Sphinx with statically
      linked MySQL support;

   -  ``--with-pgsql``, which specifies where to look for PostgreSQL
      include and library files.

   -  ``--with-static-pgsql``, which builds Sphinx with statically
      linked PostgreSQL support;

3. Build the binaries:

   ::

       $ make

4. Install the binaries in the directory of your choice: (defaults to
   ``/usr/local/bin/`` on \*nix systems, but is overridden with
   ``configure --prefix``)

   ::

       $ make install
	   
Known compilation issues
~~~~~~~~~~~~~~~~~~~~~~~~

If ``configure`` fails to locate MySQL headers and/or libraries, try
checking for and installing ``mysql-devel`` package. On some systems, it
is not installed by default.

If ``make`` fails with a message which look like

::


    /bin/sh: g++: command not found
    make[1]: *** [libsphinx_a-sphinx.o] Error 127

try checking for and installing ``gcc-c++`` package.

If you are getting compile-time errors which look like

::


    sphinx.cpp:67: error: invalid application of `sizeof' to
        incomplete type `Private::SizeError<false>'

this means that some compile-time type size check failed. The most
probable reason is that off\_t type is less than 64-bit on your system.
As a quick hack, you can edit sphinx.h and replace off\_t with DWORD in
a typedef for SphOffset\_t, but note that this will prohibit you from
using full-text indexes larger than 2 GB. Even if the hack helps, please
report such issues, providing the exact error message and compiler/OS
details, so I could properly fix them in next releases.

If you keep getting any other error, or the suggestions above do not
seem to help you, please don't hesitate to contact me.

Installing Sphinx packages on Debian and Ubuntu
-----------------------------------------------

There are two ways of getting Sphinx for Ubuntu: regular deb packages
and the Launchpad PPA repository.

Deb packages:

1. Sphinx requires a few libraries to be installed on Debian/Ubuntu. Use
   apt-get to download and install these dependencies:

   **``$ sudo apt-get install mysql-client unixodbc libpq5``**
2. Now you can install Sphinx:

   **``$ sudo dpkg -i sphinxsearch_2.3.2-beta-1~trusty_amd64.deb``**

PPA repository (Ubuntu only).

Installing Sphinx is much easier from Sphinxsearch PPA repository,
because you will get all dependencies and can also update Sphinx to the
latest version with the same command.

1. First, add Sphinxsearch repository and update the list of packages:

   **``$ sudo add-apt-repository ppa:builds/sphinxsearch-rel23``**

   **``$ sudo apt-get update``**

2. Install/update sphinxsearch package:

   **``$ sudo apt-get install sphinxsearch``**

Sphinx ``searchd`` daemon can be started/stopped using service command:

**``$ sudo service sphinxsearch start``**
Installing Sphinx packages on RedHat and CentOS
-----------------------------------------------

Currently we distribute Sphinx RPMS and SRPMS on our website for both
5.x and 6.x versions of Red Hat Enterprise Linux, but they can be
installed on CentOS as well.

1. Before installation make sure you have these packages installed:

   **``$ yum install postgresql-libs unixODBC``**

2. Download RedHat RPM from Sphinx website and install it:

   **``$ rpm -Uhv sphinx-2.2.1-1.rhel6.x86_64.rpm``**

3. After preparing configuration file (see `Quick
   tour <../quick_sphinx_usage_tour.md>`__), you can start searchd
   daemon:

   **``$ service searchd start``**
Installing Sphinx on Windows
----------------------------

Installing Sphinx on a Windows server is often easier than installing on
a Linux environment; unless you are preparing code patches, you can use
the pre-compiled binary files from the Downloads area on the website.

1. Extract everything from the .zip file you have downloaded -
   ``sphinx-2.3.2-beta-win32.zip``, or
   ``sphinx-2.3.2-beta-win32-pgsql.zip`` if you need PostgresSQL support
   as well. (We are using version 2.3.2-beta here for the sake of
   example only; be sure to change this to a specific version you're
   using.) You can use Windows Explorer in Windows XP and up to extract
   the files, or a freeware package like 7Zip to open the archive.

   For the remainder of this guide, we will assume that the folders are
   unzipped into ``C:\Sphinx``, such that ``searchd.exe`` can be found
   in ``C:\Sphinx\bin\searchd.exe``. If you decide to use any different
   location for the folders or configuration file, please change it
   accordingly.

2. Edit the contents of sphinx.conf.in - specifically entries relating
   to @CONFDIR@ - to paths suitable for your system.

3. Install the ``searchd`` system as a Windows service:

   **``C:\Sphinx\bin&gt; C:\Sphinx\bin\searchd --install --config C:\Sphinx\sphinx.conf.in --servicename SphinxSearch``**

4. The ``searchd`` service will now be listed in the Services panel
   within the Management Console, available from Administrative Tools.
   It will not have been started, as you will need to configure it and
   build your indexes with ``indexer`` before starting the service. A
   guide to do this can be found under `Quick
   tour <../quick_sphinx_usage_tour.md>`__.

   During the next steps of the install (which involve running indexer
   pretty much as you would on Linux) you may find that you get an error
   relating to libmysql.dll not being found. If you have MySQL
   installed, you should find a copy of this library in your Windows
   directory, or sometimes in Windows:raw-latex:`\System`32, or failing
   that in the MySQL core directories. If you do receive an error please
   copy libmysql.dll into the bin directory.
Sphinx deprecations and changes in default configuration
--------------------------------------------------------

Changes are as follows:

-  32-bit document IDs are now deprecated. Our binary releases are now
   all built with 64-bit IDs by default. Note that they can still load
   older indexes with 32-bit IDs, but that support will eventually be
   removed. In fact, that was deprecated awhile ago, but now we just
   want to make it clear: we don't see any sense in trying to save your
   server's RAM this way.

-  dict=crc is now deprecated. It has a bunch of limitations, the most
   important ones being keyword collisions, and no (good) wildcard
   matching support. You can read more about those limitations in our
   documentation.

-  charset\_type=sbcs is now deprecated, we're slowly switching to
   UTF-only. Even if your database is SBCS (likely for legacy reasons
   too, eh?), this should be absolutely trivial to workaround, just add
   a pre-query to fetch your data in UTF-8 and you're all set. Also, in
   fact, our current UTF-8 tokenizer is even faster than the SBCS one.

-  custom sort (@custom) is now removed from Sphinx. This feature was
   introduced long before sort by expression became a reality and it has
   been deprecated for a very long time.

-  hit\_format is deprecated. This is a hidden configuration key - it's
   not mentioned in our documentation. But, it's there and it's possible
   that someone may use it. And now we're urging you: don't use it. The
   default value is ‘inline’ and it's a new standard. ‘plain’
   hit\_format is obsolete and will be removed in the near future.

-  docinfo=inline is deprecated. You can now use
   `ondisk\_attrs <../index_configuration_options/ondiskattrs.md>`__ or
   `ondisk\_attrs\_default <../searchd_program_configuration_options/ondiskattrs_default.md>`__
   instead.

-  workers=threads is a new default for all OS now. We're gonna get rid
   of other modes in future.

-  mem\_limit=128M is a new default.

-  rt\_mem\_limit=128M is a new default.

-  ondisk\_dict is deprecated. No need to save RAM this way.

-  ondisk\_dict\_default is deprecated. No need to save RAM this way.

None of the different querying methods are deprecated, but SphinxQL is
the most advanced method. We plan to remove SphinxAPI and Sphinx SE
someday so it would be a good idea to start using SphinxQL.

-  The SetWeights() API call has been deprecated for a long time and has
   now been removed from official APIs.

-  The default matching mode for the API is now ‘extended’. Actually,
   all other modes are deprecated. We recommend using the `extended
   query syntax <../extended_query_syntax.md>`__ instead.
Quick Sphinx usage tour
-----------------------

All the example commands below assume that you installed Sphinx in
``/usr/local/sphinx``, so ``searchd`` can be found in
``/usr/local/sphinx/bin/searchd``.

To use Sphinx, you will need to:

1. Create a configuration file.

   Default configuration file name is ``sphinx.conf``. All Sphinx
   programs look for this file in current working directory by default.

   Sample configuration file, ``sphinx.conf.dist``, which has all the
   options documented, is created by ``configure``. Copy and edit that
   sample file to make your own configuration: (assuming Sphinx is
   installed into ``/usr/local/sphinx/``)

   ::

       $ cd /usr/local/sphinx/etc
       $ cp sphinx.conf.dist sphinx.conf
       $ vi sphinx.conf

   Sample configuration file is setup to index ``documents`` table from
   MySQL database ``test``; so there's ``example.sql`` sample data file
   to populate that table with a few documents for testing purposes:

   ::

       $ mysql -u test < /usr/local/sphinx/etc/example.sql

2. Run the indexer to create full-text index from your data:

   ::

       $ cd /usr/local/sphinx/etc
       $ /usr/local/sphinx/bin/indexer --all

3. Query your newly created index!

Now query your indexes!

Connect to server:

::

    $ mysql -h0 -P9306

::

    SELECT * FROM test1 WHERE MATCH('my document');

::

    INSERT INTO rt VALUES (1, 'this is', 'a sample text', 11);

::

    INSERT INTO rt VALUES (2, 'some more', 'text here', 22);

::

    SELECT gid/11 FROM rt WHERE MATCH('text') GROUP BY gid;

::

    SELECT * FROM rt ORDER BY gid DESC;

::

    SHOW TABLES;

::

    SELECT *, WEIGHT() FROM test1 WHERE MATCH('"document one"/1');SHOW META;

::

    SET profiling=1;SELECT * FROM test1 WHERE id IN (1,2,4);SHOW PROFILE;

::

    SELECT id, id%3 idd FROM test1 WHERE MATCH('this is | nothing') GROUP BY idd;SHOW PROFILE;

::

    SELECT id FROM test1 WHERE MATCH('is this a good plan?');SHOW PLAN;

::

    SELECT COUNT(*) c, id%3 idd FROM test1 GROUP BY idd HAVING COUNT(*)>1;

::

    SELECT COUNT(*) FROM test1;

::

    CALL KEYWORDS ('one two three', 'test1');

::

    CALL KEYWORDS ('one two three', 'test1', 1);

Happy searching!
