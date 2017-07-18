### Compiling on Linux {#compiling-on-linux}

1.  Extract everything from the distribution tarball (haven&#039;t you already?) and go to the `sphinx` subdirectory. (We are using version 2.3.2-beta here for the sake of example only; be sure to change this to a specific version you&#039;re using.)

    ```
    $ tar xzvf sphinx-2.3.2-beta.tar.gz
    $ cd sphinx

    ```

2.  Run the configuration program:

    ```
    $ ./configure
    ```

    There&#039;s a number of options to configure. The complete listing may be obtained by using `--help` switch. The most important ones are:

    *   `--prefix`, which specifies where to install Sphinx; such as `--prefix=/usr/local/sphinx` (all of the examples use this prefix)

    *   `--with-mysql`, which specifies where to look for MySQL include and library files, if auto-detection fails;

    *   `--with-static-mysql`, which builds Sphinx with statically linked MySQL support;

    *   `--with-pgsql`, which specifies where to look for PostgreSQL include and library files.

    *   `--with-static-pgsql`, which builds Sphinx with statically linked PostgreSQL support;

3.  Build the binaries:

    ```
    $ make
    ```

4.  Install the binaries in the directory of your choice: (defaults to `/usr/local/bin/` on *nix systems, but is overridden with `configure --prefix`)

    ```
    $ make install
    ```