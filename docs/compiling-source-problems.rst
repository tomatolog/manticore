.. raw:: html

   <div class="navheader">

2.2.3. Known compilation issues
`Prev <compiling-source-linux.html>`__ 
2.2. Compiling Sphinx from source
 `Next <installing-debian.html>`__

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

.. rubric:: 2.2.3. Known compilation issues
   :name: known-compilation-issues
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

If ``configure`` fails to locate MySQL headers and/or libraries, try
checking for and installing ``mysql-devel`` package. On some systems, it
is not installed by default.

If ``make`` fails with a message which look like

.. code:: programlisting

    /bin/sh: g++: command not found
    make[1]: *** [libsphinx_a-sphinx.o] Error 127

try checking for and installing ``gcc-c++`` package.

If you are getting compile-time errors which look like

.. code:: programlisting

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
seem to help you, please don’t hesitate to contact me.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+---------------------------------------+---------------------------------------------------------+
| `Prev <compiling-source-linux.html>`__    | `Up <compiling-from-source.html>`__   |  `Next <installing-debian.html>`__                      |
+-------------------------------------------+---------------------------------------+---------------------------------------------------------+
| 2.2.2. Compiling on Linux                 | `Home <index.html>`__                 |  2.3. Installing Sphinx packages on Debian and Ubuntu   |
+-------------------------------------------+---------------------------------------+---------------------------------------------------------+

.. raw:: html

   </div>
