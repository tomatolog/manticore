.. raw:: html

   <div class="navheader">

2.2.2. Compiling on Linux
`Prev <required-tools.html>`__ 
2.2. Compiling Sphinx from source
 `Next <compiling-source-problems.html>`__

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

.. rubric:: 2.2.2. Compiling on Linux
   :name: compiling-on-linux
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="orderedlist">

1. Extract everything from the distribution tarball (haven’t you
   already?) and go to the ``sphinx`` subdirectory. (We are using
   version 2.3.2-beta here for the sake of example only; be sure to
   change this to a specific version you’re using.)

   .. raw:: html

      <div class="literallayout">

   **``$ tar xzvf sphinx-2.3.2-beta.tar.gz $ cd sphinx``**

   .. raw:: html

      </div>

2. Run the configuration program:

   .. raw:: html

      <div class="literallayout">

   **``$ ./configure``**

   .. raw:: html

      </div>

   There’s a number of options to configure. The complete listing may be
   obtained by using ``--help`` switch. The most important ones are:

   .. raw:: html

      <div class="itemizedlist">

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

   .. raw:: html

      </div>

3. Build the binaries:

   .. raw:: html

      <div class="literallayout">

   **``$ make``**

   .. raw:: html

      </div>

4. Install the binaries in the directory of your choice: (defaults to
   ``/usr/local/bin/`` on \*nix systems, but is overridden with
   ``configure --prefix``)

   .. raw:: html

      <div class="literallayout">

   **``$ make install``**

   .. raw:: html

      </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+---------------------------------------+----------------------------------------------+
| `Prev <required-tools.html>`__    | `Up <compiling-from-source.html>`__   |  `Next <compiling-source-problems.html>`__   |
+-----------------------------------+---------------------------------------+----------------------------------------------+
| 2.2.1. Required tools             | `Home <index.html>`__                 |  2.2.3. Known compilation issues             |
+-----------------------------------+---------------------------------------+----------------------------------------------+

.. raw:: html

   </div>
