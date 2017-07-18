.. raw:: html

   <div class="navheader">

5.5.4. Type conversion functions
`Prev <date-time-functions.html>`__ 
5.5. Expressions, functions, and operators
 `Next <comparison-functions.html>`__

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

.. rubric:: 5.5.4. Type conversion functions
   :name: type-conversion-functions
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="variablelist">

BIGINT()
    Forcibly promotes the integer argument to 64-bit type, and does
    nothing on floating point argument. It’s intended to help enforce
    evaluation of certain expressions (such as ``a*b``) in 64-bit mode
    even though all the arguments are 32-bit. Introduced in version
    0.9.9-rc1.

INTEGER()
    Forcibly promotes given argument to 64-bit signed type. Intended to
    help enforce evaluation of numeric JSON fields. Introduced in
    version 2.2.1-beta.

SINT()
    Forcibly reinterprets its 32-bit unsigned integer argument as
    signed, and also expands it to 64-bit type (because 32-bit type is
    unsigned). It’s easily illustrated by the following example: 1-2
    normally evaluates to 4294967295, but SINT(1-2) evaluates to -1.
    Introduced in version 1.10-beta.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------+-----------------------------+-----------------------------------------+
| `Prev <date-time-functions.html>`__    | `Up <expressions.html>`__   |  `Next <comparison-functions.html>`__   |
+----------------------------------------+-----------------------------+-----------------------------------------+
| 5.5.3. Date and time functions         | `Home <index.html>`__       |  5.5.5. Comparison functions            |
+----------------------------------------+-----------------------------+-----------------------------------------+

.. raw:: html

   </div>
