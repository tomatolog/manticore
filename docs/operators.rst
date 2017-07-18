.. raw:: html

   <div class="navheader">

5.5.1. Operators
`Prev <expressions.html>`__ 
5.5. Expressions, functions, and operators
 `Next <numeric-functions.html>`__

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

.. rubric:: 5.5.1. Operators
   :name: operators
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="variablelist">

Arithmetic operators: +, -, \*, /, %, DIV, MOD
    The standard arithmetic operators. Arithmetic calculations involving
    those can be performed in three different modes: (a) using
    single-precision, 32-bit IEEE 754 floating point values (the
    default), (b) using signed 32-bit integers, (c) using 64-bit signed
    integers. The expression parser will automatically switch to integer
    mode if there are no operations the result in a floating point
    value. Otherwise, it will use the default floating point mode. For
    instance, ``a+b`` will be computed using 32-bit integers if both
    arguments are 32-bit integers; or using 64-bit integers if both
    arguments are integers but one of them is 64-bit; or in floats
    otherwise. However, ``a/b`` or ``sqrt(a)`` will always be computed
    in floats, because these operations return a result of non-integer
    type. To avoid the first, you can either use ``IDIV(a,b)`` or
    ``a DIV b`` form. Also, ``a*b`` will not be automatically promoted
    to 64-bit when the arguments are 32-bit. To enforce 64-bit results,
    you can use BIGINT(). (But note that if there are non-integer
    operations, BIGINT() will simply be ignored.)

Comparison operators: <, > <=, >=, =, <>
    Comparison operators (eg. = or <=) return 1.0 when the condition is
    true and 0.0 otherwise. For instance, ``(a=b)+3`` will evaluate to 4
    when attribute ‘a’ is equal to attribute ‘b’, and to 3 when ‘a’ is
    not. Unlike MySQL, the equality comparisons (ie. = and <> operators)
    introduce a small equality threshold (1e-6 by default). If the
    difference between compared values is within the threshold, they
    will be considered equal.

Boolean operators: AND, OR, NOT
    Boolean operators (AND, OR, NOT) were introduced in 0.9.9-rc2 and
    behave as usual. They are left-associative and have the least
    priority compared to other operators. NOT has more priority than AND
    and OR but nevertheless less than any other operator. AND and OR
    have the same priority so brackets use is recommended to avoid
    confusion in complex expressions.

Bitwise operators: &, \|
    These operators perform bitwise AND and OR respectively. The
    operands must be of an integer types. Introduced in version
    1.10-beta.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+-----------------------------+--------------------------------------+
| `Prev <expressions.html>`__                   | `Up <expressions.html>`__   |  `Next <numeric-functions.html>`__   |
+-----------------------------------------------+-----------------------------+--------------------------------------+
| 5.5. Expressions, functions, and operators    | `Home <index.html>`__       |  5.5.2. Numeric functions            |
+-----------------------------------------------+-----------------------------+--------------------------------------+

.. raw:: html

   </div>
