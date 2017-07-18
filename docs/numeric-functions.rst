.. raw:: html

   <div class="navheader">

5.5.2. Numeric functions
`Prev <operators.html>`__ 
5.5. Expressions, functions, and operators
 `Next <date-time-functions.html>`__

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

.. rubric:: 5.5.2. Numeric functions
   :name: numeric-functions
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="variablelist">

ABS()
    Returns the absolute value of the argument.

BITDOT()
    BITDOT(mask, w0, w1, …) returns the sum of products of an each bit
    of a mask multiplied with its weight. ``bit0*w0 + bit1*w1 + ...``

CEIL()
    Returns the smallest integer value greater or equal to the argument.

CONTAINS()
    CONTAINS(polygon, x, y) checks whether the (x,y) point is within the
    given polygon, and returns 1 if true, or 0 if false. The polygon has
    to be specified using either the
    `POLY2D() <numeric-functions.html#expr-func-poly2d>`__ function or
    the `GEOPOLY2D() <numeric-functions.html#expr-func-poly2d>`__
    function. The former function is intended for “small” polygons,
    meaning less than 500 km (300 miles) a side, and it doesn’t take
    into account the Earth’s curvature for speed. For larger distances,
    you should use GEOPOLY2D, which tessellates the given polygon in
    smaller parts, accounting for the Earth’s curvature. These functions
    were added in version 2.1.1-beta.

COS()
    Returns the cosine of the argument.

DOUBLE()
    Forcibly promotes given argument to floating point type. Intended to
    help enforce evaluation of numeric JSON fields. Introduced in
    version 2.2.1-beta.

EXP()
    Returns the exponent of the argument (e=2.718… to the power of the
    argument).

FIBONACCI()
    Returns the N-th Fibonacci number, where N is the integer argument.
    That is, arguments of 0 and up will generate the values 0, 1, 1, 2,
    3, 5, 8, 13 and so on. Note that the computations are done using
    32-bit integer math and thus numbers 48th and up will be returned
    modulo 2^32.

FLOOR()
    Returns the largest integer value lesser or equal to the argument.

GEOPOLY2D()
    GEOPOLY2D(x1,y1,x2,y2,x3,y3…) produces a polygon to be used with the
    `CONTAINS() <numeric-functions.html#expr-func-contains>`__ function.
    This function takes into account the Earth’s curvature by
    tessellating the polygon into smaller ones, and should be used for
    larger areas; see the
    `POLY2D() <numeric-functions.html#expr-func-poly2d>`__ function. The
    function expects coordinates to be in degrees, if radians are used
    it will give same result as POLY2D().

IDIV()
    Returns the result of an integer division of the first argument by
    the second argument. Both arguments must be of an integer type.

LN()
    Returns the natural logarithm of the argument (with the base of
    e=2.718…).

LOG10()
    Returns the common logarithm of the argument (with the base of 10).

LOG2()
    Returns the binary logarithm of the argument (with the base of 2).

MAX()
    Returns the bigger of two arguments.

MIN()
    Returns the smaller of two arguments.

POLY2D()
    POLY2D(x1,y1,x2,y2,x3,y3…) produces a polygon to be used with the
    `CONTAINS() <numeric-functions.html#expr-func-contains>`__ function.
    This polygon assumes a flat Earth, so it should not be too large;
    see the `POLY2D() <numeric-functions.html#expr-func-poly2d>`__
    function.

POW()
    Returns the first argument raised to the power of the second
    argument.

SIN()
    Returns the sine of the argument.

SQRT()
    Returns the square root of the argument.

UINT()
    Forcibly reinterprets given argument to 64-bit unsigned type.
    Introduced in version 2.2.1-beta.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------+-----------------------------+----------------------------------------+
| `Prev <operators.html>`__    | `Up <expressions.html>`__   |  `Next <date-time-functions.html>`__   |
+------------------------------+-----------------------------+----------------------------------------+
| 5.5.1. Operators             | `Home <index.html>`__       |  5.5.3. Date and time functions        |
+------------------------------+-----------------------------+----------------------------------------+

.. raw:: html

   </div>
