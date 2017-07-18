Installation
---------------

Supported systems
+++++++++++++
Sphinx can be compiled either from source or installed using prebuilt packages. Most modern UNIX systems with a C++ compiler should be able to compile and run Sphinx without any modifications.

Currently known systems Sphinx has been successfully running on are:

Linux 2.4.x, 2.6.x, 3.x (many various distributions)

Windows 2000, XP, 7, 8

FreeBSD 4.x, 5.x, 6.x, 7.x, 8.x

NetBSD 1.6, 3.0

Solaris 9, 11

Mac OS X

CPU architectures known to work include i386 (aka x86), amd64 (aka x86_64), SPARC64, and ARM.

Chances are good that Sphinx should work on other Unix platforms and/or CPU architectures just as well. Please report any other platforms that worked for you!

All platforms are production quality. There are no principal functional limitations on any platform.

Compiling Sphinx from source
+++++++++++++
Required tools
^^^^^^^^^^^^^
On UNIX, you will need the following tools to build and install Sphinx:

a working C++ compiler. GNU gcc and clang are known to work.

a good make program. GNU make is known to work.

On Windows, you will need Microsoft Visual C/C++ Studio .NET 2005 or above. Other compilers/environments will probably work as well, but for the time being, you will have to build makefile (or other environment specific project files) manually.

Compiling on Linux
^^^^^^^^^^^^^
Extract everything from the distribution tarball (haven't you already?) and go to the sphinx subdirectory. (We are using version 2.3.2-beta here for the sake of example only; be sure to change this to a specific version you're using.)

$ tar xzvf sphinx-2.3.2-beta.tar.gz
$ cd sphinx

Run the configuration program:

$ ./configure

There's a number of options to configure. The complete listing may be obtained by using --help switch. The most important ones are:

--prefix, which specifies where to install Sphinx; such as --prefix=/usr/local/sphinx (all of the examples use this prefix)

--with-mysql, which specifies where to look for MySQL include and library files, if auto-detection fails;

--with-static-mysql, which builds Sphinx with statically linked MySQL support;

--with-pgsql, which specifies where to look for PostgreSQL include and library files.

--with-static-pgsql, which builds Sphinx with statically linked PostgreSQL support;

Build the binaries:

$ make

Install the binaries in the directory of your choice: (defaults to /usr/local/bin/ on *nix systems, but is overridden with configure --prefix)

$ make install

Known compilation issues
^^^^^^^^^^^^^

If configure fails to locate MySQL headers and/or libraries, try checking for and installing mysql-devel package. On some systems, it is not installed by default.

If make fails with a message which look like

/bin/sh: g++: command not found
make[1]: *** [libsphinx_a-sphinx.o] Error 127
try checking for and installing gcc-c++ package.

If you are getting compile-time errors which look like

sphinx.cpp:67: error: invalid application of `sizeof' to
    incomplete type `Private::SizeError<false>'
this means that some compile-time type size check failed. The most probable reason is that off_t type is less than 64-bit on your system. As a quick hack, you can edit sphinx.h and replace off_t with DWORD in a typedef for SphOffset_t, but note that this will prohibit you from using full-text indexes larger than 2 GB. Even if the hack helps, please report such issues, providing the exact error message and compiler/OS details, so I could properly fix them in next releases.

If you keep getting any other error, or the suggestions above do not seem to help you, please don't hesitate to contact me.
