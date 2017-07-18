Type conversion functions
~~~~~~~~~~~~~~~~~~~~~~~~~

-  BIGINT()
-  Forcibly promotes the integer argument to 64-bit type, and does
   nothing on floating point argument. It's intended to help enforce
   evaluation of certain expressions (such as ``a*b``) in 64-bit mode
   even though all the arguments are 32-bit. Introduced in version
   0.9.9-rc1.

-  INTEGER()
-  Forcibly promotes given argument to 64-bit signed type. Intended to
   help enforce evaluation of numeric JSON fields. Introduced in version
   2.2.1-beta.

-  SINT()
-  Forcibly reinterprets its 32-bit unsigned integer argument as signed,
   and also expands it to 64-bit type (because 32-bit type is unsigned).
   It's easily illustrated by the following example: 1-2 normally
   evaluates to 4294967295, but SINT(1-2) evaluates to -1. Introduced in
   version 1.10-beta.
