.. raw:: html

   <div class="navheader">

5.5. Expressions, functions, and operators
`Prev <formulas-for-builtin-rankers.html>`__ 
Chapter 5. Searching
 `Next <operators.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 5.5. Expressions, functions, and operators
   :name: expressions-functions-and-operators
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="toc">

`5.5.1. Operators <operators.html>`__
`5.5.2. Numeric functions <numeric-functions.html>`__
`5.5.3. Date and time functions <date-time-functions.html>`__
`5.5.4. Type conversion functions <type-conversion-functions.html>`__
`5.5.5. Comparison functions <comparison-functions.html>`__
`5.5.6. Miscellaneous functions <misc-functions.html>`__

.. raw:: html

   </div>

Sphinx lets you use arbitrary arithmetic expressions both via SphinxQL
and SphinxAPI, involving attribute values, internal attributes (document
ID and relevance weight), arithmetic operations, a number of built-in
functions, and user-defined functions. This section documents the
supported operators and functions. Here’s the complete reference list
for quick access.

.. raw:: html

   <div class="itemizedlist">

-  `Arithmetic operators: +, -, \*, /, %, DIV,
   MOD <operators.html#expr-ari-ops>`__

-  `Comparison operators: <, > <=, >=, =,
   <> <operators.html#expr-comp-ops>`__

-  `Boolean operators: AND, OR, NOT <operators.html#expr-bool-ops>`__

-  `Bitwise operators: &, \| <operators.html#expr-bitwise-ops>`__

-  `ABS() <numeric-functions.html#expr-func-abs>`__

-  `ALL() <misc-functions.html#expr-func-all>`__

-  `ANY() <misc-functions.html#expr-func-any>`__

-  `ATAN2() <misc-functions.html#expr-func-atan2>`__

-  `BIGINT() <type-conversion-functions.html#expr-func-bigint>`__

-  `BITDOT() <numeric-functions.html#expr-func-bitdot>`__

-  `CEIL() <numeric-functions.html#expr-func-ceil>`__

-  `CONTAINS() <numeric-functions.html#expr-func-contains>`__

-  `COS() <numeric-functions.html#expr-func-cos>`__

-  `CRC32() <misc-functions.html#expr-func-crc32>`__

-  `DAY() <date-time-functions.html#expr-func-day>`__

-  `DOUBLE() <numeric-functions.html#expr-func-double>`__

-  `EXP() <numeric-functions.html#expr-func-exp>`__

-  `FIBONACCI() <numeric-functions.html#expr-func-fibonacci>`__

-  `FLOOR() <numeric-functions.html#expr-func-floor>`__

-  `GEODIST() <misc-functions.html#expr-func-geodist>`__

-  `GEOPOLY2D() <numeric-functions.html#expr-func-geopoly2d>`__

-  `GREATEST() <misc-functions.html#expr-func-greatest>`__

-  `HOUR() <date-time-functions.html#expr-func-hour>`__

-  `IDIV() <numeric-functions.html#expr-func-idiv>`__

-  `IF() <comparison-functions.html#expr-func-if>`__

-  `IN() <comparison-functions.html#expr-func-in>`__

-  `INDEXOF() <misc-functions.html#expr-func-indexof>`__

-  `INTEGER() <type-conversion-functions.html#expr-func-integer>`__

-  `INTERVAL() <comparison-functions.html#expr-func-interval>`__

-  `LEAST() <misc-functions.html#expr-func-least>`__

-  `LENGTH() <misc-functions.html#expr-func-length>`__

-  `LN() <numeric-functions.html#expr-func-ln>`__

-  `LOG10() <numeric-functions.html#expr-func-log10>`__

-  `LOG2() <numeric-functions.html#expr-func-log2>`__

-  `MAX() <numeric-functions.html#expr-func-max>`__

-  `MIN() <numeric-functions.html#expr-func-min>`__

-  `MINUTE() <date-time-functions.html#expr-func-minute>`__

-  `MIN\_TOP\_SORTVAL() <misc-functions.html#expr-func-min-top-sortval>`__

-  `MIN\_TOP\_WEIGHT() <misc-functions.html#expr-func-min-top-weight>`__

-  `MONTH() <date-time-functions.html#expr-func-month>`__

-  `NOW() <date-time-functions.html#expr-func-now>`__

-  `POLY2D() <numeric-functions.html#expr-func-poly2d>`__

-  `POW() <numeric-functions.html#expr-func-pow>`__

-  `RAND() <misc-functions.html#expr-func-rand>`__

-  `REMAP() <misc-functions.html#expr-func-remap>`__

-  `SECOND() <date-time-functions.html#expr-func-second>`__

-  `SIN() <numeric-functions.html#expr-func-sin>`__

-  `SINT() <type-conversion-functions.html#expr-func-sint>`__

-  `SQRT() <numeric-functions.html#expr-func-sqrt>`__

-  `UINT() <numeric-functions.html#expr-func-uint>`__

-  `YEAR() <date-time-functions.html#expr-func-year>`__

-  `YEARMONTH() <date-time-functions.html#expr-func-yearmonth>`__

-  `YEARMONTHDAY() <date-time-functions.html#expr-func-yearmonthday>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------------------------+---------------------------+------------------------------+
| `Prev <formulas-for-builtin-rankers.html>`__               | `Up <searching.html>`__   |  `Next <operators.html>`__   |
+------------------------------------------------------------+---------------------------+------------------------------+
| 5.4.8. Formula expressions for all the built-in rankers    | `Home <index.html>`__     |  5.5.1. Operators            |
+------------------------------------------------------------+---------------------------+------------------------------+

.. raw:: html

   </div>
