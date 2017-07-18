Comparison functions
~~~~~~~~~~~~~~~~~~~~

-  IF()
-  ``IF()`` behavior is slightly different that that of its MySQL
   counterpart. It takes 3 arguments, check whether the 1st argument is
   equal to 0.0, returns the 2nd argument if it is not zero, or the 3rd
   one when it is. Note that unlike comparison operators, ``IF()`` does
   <b>not</b> use a threshold! Therefore, it's safe to use comparison
   results as its 1st argument, but arithmetic operators might produce
   unexpected results. For instance, the following two calls will
   produce *different* results even though they are logically
   equivalent:

   ::


       IF ( sqrt(3)*sqrt(3)-3<>0, a, b )
       IF ( sqrt(3)*sqrt(3)-3, a, b )

   In the first case, the comparison operator <> will return 0.0 (false)
   because of a threshold, and ``IF()`` will always return ‘b’ as a
   result. In the second one, the same ``sqrt(3)*sqrt(3)-3`` expression
   will be compared with zero *without* threshold by the ``IF()``
   function itself. But its value will be slightly different from zero
   because of limited floating point calculations precision. Because of
   that, the comparison with 0.0 done by ``IF()`` will not pass, and the
   second variant will return ‘a’ as a result.

-  IN()
-  IN(expr,val1,val2,…), introduced in version 0.9.9-rc1, takes 2 or
   more arguments, and returns 1 if 1st argument (expr) is equal to any
   of the other arguments (val1..valN), or 0 otherwise. Currently, all
   the checked values (but not the expression itself!) are required to
   be constant. (Its technically possible to implement arbitrary
   expressions too, and that might be implemented in the future.)
   Constants are pre-sorted and then binary search is used, so IN() even
   against a big arbitrary list of constants will be very quick.
   Starting with 0.9.9-rc2, first argument can also be a MVA attribute.
   In that case, IN() will return 1 if any of the MVA values is equal to
   any of the other arguments. Starting with 2.0.1-beta, IN() also
   supports ``IN(expr,@uservar)`` syntax to check whether the value
   belongs to the list in the given global user variable. First argument
   can be JSON attribute since 2.2.1-beta.

-  INTERVAL()
-  INTERVAL(expr,point1,point2,point3,…), introduced in version
   0.9.9-rc1, takes 2 or more arguments, and returns the index of the
   argument that is less than the first argument: it returns 0 if
   expr<point1, 1 if point1<=expr<point2, and so on. It is required that
   point1<point2<…<pointN for this function to work correctly.
