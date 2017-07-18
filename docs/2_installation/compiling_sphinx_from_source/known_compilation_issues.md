### Known compilation issues {#known-compilation-issues}

If `configure` fails to locate MySQL headers and/or libraries, try checking for and installing `mysql-devel` package. On some systems, it is not installed by default.

If `make` fails with a message which look like

```

/bin/sh: g++: command not found
make[1]: *** [libsphinx_a-sphinx.o] Error 127

```

try checking for and installing `gcc-c++` package.

If you are getting compile-time errors which look like

```

sphinx.cpp:67: error: invalid application of `sizeof' to
    incomplete type `Private::SizeError<false>'

```

this means that some compile-time type size check failed. The most probable reason is that off_t type is less than 64-bit on your system. As a quick hack, you can edit sphinx.h and replace off_t with DWORD in a typedef for SphOffset_t, but note that this will prohibit you from using full-text indexes larger than 2 GB. Even if the hack helps, please report such issues, providing the exact error message and compiler/OS details, so I could properly fix them in next releases.

If you keep getting any other error, or the suggestions above do not seem to help you, please don&#039;t hesitate to contact me.