Expressions, functions, and operators
-------------------------------------

Manticore lets you use arbitrary arithmetic expressions both via SphinxQL
and ManticoreAPI, involving attribute values, internal attributes (document
ID and relevance weight), arithmetic operations, a number of built-in
functions, and user-defined functions. This section documents the
supported operators and functions. Here's the complete reference list
for quick access.

-  `Arithmetic operators: +, -, \*, /, %, DIV,
   MOD <operators.md#expr-ari-ops>`__

-  `Comparison operators: <, > <=, >=, =,
   <> <operators.md#expr-comp-ops>`__

-  `Boolean operators: AND, OR, NOT <operators.md#expr-bool-ops>`__

-  `Bitwise operators: &, \| <operators.md#expr-bitwise-ops>`__

-  `ABS() <numeric_functions.md#expr-func-abs>`__

-  `ALL() <miscellaneous_functions.md#expr-func-all>`__

-  `ANY() <miscellaneous_functions.md#expr-func-any>`__

-  `ATAN2() <miscellaneous_functions.md#expr-func-atan2>`__

-  `BIGINT() <type_conversion_functions.md#expr-func-bigint>`__

-  `BITDOT() <numeric_functions.md#expr-func-bitdot>`__

-  `CEIL() <numeric_functions.md#expr-func-ceil>`__

-  `CONTAINS() <numeric_functions.md#expr-func-contains>`__

-  `COS() <numeric_functions.md#expr-func-cos>`__

-  `CRC32() <miscellaneous_functions.md#expr-func-crc32>`__

-  `DAY() <date_and_time_functions.md#expr-func-day>`__

-  `DOUBLE() <numeric_functions.md#expr-func-double>`__

-  `EXP() <numeric_functions.md#expr-func-exp>`__

-  `FIBONACCI() <numeric_functions.md#expr-func-fibonacci>`__

-  `FLOOR() <numeric_functions.md#expr-func-floor>`__

-  `GEODIST() <miscellaneous_functions.md#expr-func-geodist>`__

-  `GEOPOLY2D() <numeric_functions.md#expr-func-geopoly2d>`__

-  `GREATEST() <miscellaneous_functions.md#expr-func-greatest>`__

-  `HOUR() <date_and_time_functions.md#expr-func-hour>`__

-  `IDIV() <numeric_functions.md#expr-func-idiv>`__

-  `IF() <comparison_functions.md#expr-func-if>`__

-  `IN() <comparison_functions.md#expr-func-in>`__

-  `INDEXOF() <miscellaneous_functions.md#expr-func-indexof>`__

-  `INTEGER() <type_conversion_functions.md#expr-func-integer>`__

-  `INTERVAL() <comparison_functions.md#expr-func-interval>`__

-  `LEAST() <miscellaneous_functions.md#expr-func-least>`__

-  `LENGTH() <miscellaneous_functions.md#expr-func-length>`__

-  `LN() <numeric_functions.md#expr-func-ln>`__

-  `LOG10() <numeric_functions.md#expr-func-log10>`__

-  `LOG2() <numeric_functions.md#expr-func-log2>`__

-  `MAX() <numeric_functions.md#expr-func-max>`__

-  `MIN() <numeric_functions.md#expr-func-min>`__

-  `MINUTE() <date_and_time_functions.md#expr-func-minute>`__

-  `MIN\_TOP\_SORTVAL() <miscellaneous_functions.md#expr-func-min-top-sortval>`__

-  `MIN\_TOP\_WEIGHT() <miscellaneous_functions.md#expr-func-min-top-weight>`__

-  `MONTH() <date_and_time_functions.md#expr-func-month>`__

-  `NOW() <date_and_time_functions.md#expr-func-now>`__

-  `POLY2D() <numeric_functions.md#expr-func-poly2d>`__

-  `POW() <numeric_functions.md#expr-func-pow>`__

-  `RAND() <miscellaneous_functions.md#expr-func-rand>`__

-  `REMAP() <miscellaneous_functions.md#expr-func-remap>`__

-  `SECOND() <date_and_time_functions.md#expr-func-second>`__

-  `SIN() <numeric_functions.md#expr-func-sin>`__

-  `SINT() <type_conversion_functions.md#expr-func-sint>`__

-  `SQRT() <numeric_functions.md#expr-func-sqrt>`__

-  `UINT() <numeric_functions.md#expr-func-uint>`__

-  `YEAR() <date_and_time_functions.md#expr-func-year>`__

-  `YEARMONTH() <date_and_time_functions.md#expr-func-yearmonth>`__

-  `YEARMONTHDAY() <date_and_time_functions.md#expr-func-yearmonthday>`__
