Miscellaneous functions
~~~~~~~~~~~~~~~~~~~~~~~

-  ALL()
-  ALL(cond FOR var IN json.array) function was introduced in
   2.2.1-beta. It applies to JSON arrays and returns 1 if condition is
   true for all elements in array and 0 otherwise. ‘cond’ is a general
   expression which additionally can use ‘var’ as current value of an
   array element within itself.

   ::


       SELECT ALL(x>3 AND x<7 FOR x IN j.intarray) FROM test;

-  ANY()
-  ANY(cond FOR var IN json.array) function was introduced in
   2.2.1-beta. It works similar to `ALL() <#expr-func-all>`__ except for
   it returns 1 if condition is true for any element in array.

-  ATAN2()
-  Returns the arctangent function of two arguments, expressed in
   <b>radians</b>.

-  CRC32()
-  Returns the CRC32 value of a string argument. Introduced in version
   2.0.1-beta.

-  GEODIST()
-  GEODIST(lat1, lon1, lat2, lon2, […]) function, introduced in version
   0.9.9-rc2, computes geosphere distance between two given points
   specified by their coordinates. Note that by default both latitudes
   and longitudes must be in <b>radians</b> and the result will be in
   <b>meters</b>. You can use arbitrary expression as any of the four
   coordinates. An optimized path will be selected when one pair of the
   arguments refers directly to a pair attributes and the other one is
   constant.

   Starting with version 2.2.1-beta, GEODIST() also takes an optional
   5th argument that lets you easily convert between input and output
   units, and pick the specific geodistance formula to use. The complete
   syntax and a few examples are as follows:

   ::


       GEODIST(lat1, lon1, lat2, lon2, { option=value, ... })

       GEODIST(40.7643929, -73.9997683, 40.7642578, -73.9994565, {in=degrees, out=feet})
       GEODIST(51.50, -0.12, 29.98, 31.13, {in=deg, out=mi}}

   The known options and their values are:

   -  ``in = {deg | degrees | rad | radians}``, specifies the input
      units;
   -  ``out = {m | meters | km | kilometers | ft | feet | mi | miles}``,
      specifies the output units;
   -  ``method = {haversine | adaptive}``, specifies the geodistance
      calculation method.

   Upto version 2.1.x (inclusive), “haversine” method was the default.
   Starting with 2.2.1-beta, the default method changed to “adaptive”, a
   new, well optimized implementation that is both more precise *and*
   much faster at all times.

-  GREATEST()
-  GREATEST(attr\_json.some\_array) was introduced in version
   2.2.1-beta. First argument is JSON array and return value is the
   greatest value in that array. Also works for MVA.

-  INDEXOF()
-  INDEXOF(cond FOR var IN json.array) function was introduced in
   2.2.1-beta. It iterates through all elements in array and returns
   index of first element for which ‘cond’ is true and -1 if ‘cond’ is
   false for every element in array.

   ::


       SELECT INDEXOF(name='John' FOR name IN j.peoples) FROM test;

-  LEAST()
-  LEAST(attr\_json.some\_array) was introduced in version 2.2.1-beta.
   First argument is JSON array and return value is the least value in
   that array. Also works for MVA.

-  LENGTH()
-  LENGTH(attr\_mva) function, introduced in version 2.1.2-stable,
   returns amount of elements in MVA set. It works with both 32-bit and
   64-bit MVA attributes. LENGTH(attr\_json) was introduced in version
   2.2.1-beta. It returns length of a field in JSON. Return value
   depends on type of a field. For example LENGTH(json\_attr.some\_int)
   always returns 1 and LENGTH(json\_attr.some\_array) returns number of
   elements in array.

-  MIN\_TOP\_SORTVAL()
-  Returns sort key value of the worst found element in the current
   top-N matches if sort key is float and 0 otherwise.

-  MIN\_TOP\_WEIGHT()
-  Returns weight of the worst found element in the current top-N
   matches.

-  PACKEDFACTORS()
-  PACKEDFACTORS(), introduced in version 2.1.1-beta, can be used in
   queries, either to just see all the weighting factors calculated when
   doing the matching, or to provide a binary attribute that can be used
   to write a custom ranking UDF. This function works only if expression
   ranker is specified and the query is not a full scan, otherwise it
   will return an error. Starting with 2.2.2-beta PACKEDFACTORS() can
   take an optional argument that disables ATC ranking factor
   calculation:

   ::


       PACKEDFACTORS({no_atc=1})

   Calculating ATC slows down query processing considerably, so this
   option can be useful if you need to see the ranking factors, but do
   not need ATC. Starting with 2.2.3-beta PACKEDFACTORS() can also be
   told to format its output as JSON:

   ::


       PACKEDFACTORS({json=1})

   The respective outputs in either key-value pair or JSON format would
   look as follows below. (Note that the examples below are wrapped for
   readability; actual returned values would be single-line.)

   ::


       mysql> SELECT id, PACKEDFACTORS() FROM test1
           -> WHERE MATCH('test one') OPTION ranker=expr('1') \G
       *************************** 1\. row ***************************
                    id: 1
       packedfactors(): bm25=569, bm25a=0.617197, field_mask=2, doc_word_count=2,
           field1=(lcs=1, hit_count=2, word_count=2, tf_idf=0.152356,
               min_idf=-0.062982, max_idf=0.215338, sum_idf=0.152356, min_hit_pos=4,
               min_best_span_pos=4, exact_hit=0, max_window_hits=1, min_gaps=2,
               exact_order=1, lccs=1, wlccs=0.215338, atc=-0.003974),
           word0=(tf=1, idf=-0.062982),
           word1=(tf=1, idf=0.215338)
       1 row in set (0.00 sec)

       mysql> SELECT id, PACKEDFACTORS({json=1}) FROM test1
           -> WHERE MATCH('test one') OPTION ranker=expr('1') \G
       *************************** 1\. row ***************************
                            id: 1
       packedfactors({json=1}):
       {

           "bm25": 569,
           "bm25a": 0.617197,
           "field_mask": 2,
           "doc_word_count": 2,
           "fields": [
               {
                   "lcs": 1,
                   "hit_count": 2,
                   "word_count": 2,
                   "tf_idf": 0.152356,
                   "min_idf": -0.062982,
                   "max_idf": 0.215338,
                   "sum_idf": 0.152356,
                   "min_hit_pos": 4,
                   "min_best_span_pos": 4,
                   "exact_hit": 0,
                   "max_window_hits": 1,
                   "min_gaps": 2,
                   "exact_order": 1,
                   "lccs": 1,
                   "wlccs": 0.215338,
                   "atc": -0.003974
               }
           ],
           "words": [
               {
                   "tf": 1,
                   "idf": -0.062982
               },
               {
                   "tf": 1,
                   "idf": 0.215338
               }
           ]

       }
       1 row in set (0.01 sec)

   This function can be used to implement custom ranking functions in
   UDFs, as in

   ::


       SELECT *, CUSTOM_RANK(PACKEDFACTORS()) AS r
       FROM my_index
       WHERE match('hello')
       ORDER BY r DESC
       OPTION ranker=expr('1');

   Where CUSTOM\_RANK() is a function implemented in an UDF. It should
   declare a SPH\_UDF\_FACTORS structure (defined in ``sphinxudf.h``),
   initialize this structure, unpack the factors into it before usage,
   and deinitialize it afterwards, as follows:

   ::


       SPH_UDF_FACTORS factors;
       sphinx_factors_init(&factors);
       sphinx_factors_unpack((DWORD*)args->arg_values[0], &factors);
       // ... can use the contents of factors variable here ...
       sphinx_factors_deinit(&factors);

   PACKEDFACTORS() data is available at all query stages, not just when
   doing the initial matching and ranking pass. That enables another
   particularly interesting application of PACKEDFACTORS(), namely
   <b>re-ranking</b>.

   In the example just above, we used an expression-based ranker with a
   dummy expression, and sorted the result set by the value computed by
   our UDF. In other words, we used the UDF to *rank* all our results.
   Assume now, for the sake of an example, that our UDF is extremely
   expensive to compute and has a throughput of just 10,000 calls per
   second. Assume that our query matches 1,000,000 documents. To
   maintain reasonable performance, we would then want to use a (much)
   simpler expression to do most of our ranking, and then apply the
   expensive UDF to only a few top results, say, top-100 results. Or, in
   other words, build top-100 results using a simpler ranking function
   and then *re-rank* those with a complex one. We can do that just as
   well with subselects:

   ::


       SELECT * FROM (
           SELECT *, CUSTOM_RANK(PACKEDFACTORS()) AS r
           FROM my_index WHERE match('hello')
           OPTION ranker=expr('sum(lcs)*1000+bm25')
           ORDER BY WEIGHT() DESC
           LIMIT 100
       ) ORDER BY r DESC LIMIT 10

   In this example, expression-based ranker will be called for every
   matched document to compute WEIGHT(). So it will get called 1,000,000
   times. But the UDF computation can be postponed until the outer sort.
   And it also will be done for just the top-100 matches by WEIGHT(),
   according to the inner limit. So the UDF will only get called 100
   times. And then the final top-10 matches by UDF value will be
   selected and returned to the application.

   For reference, in the distributed case PACKEDFACTORS() data gets sent
   from the agents to master in a binary format, too. This makes it
   technically feasible to implement additional re-ranking pass (or
   passes) on the master node, if needed.

   If used with SphinxQL but not called from any UDFs, the result of
   PACKEDFACTORS() is simply formatted as plain text, which can be used
   to manually assess the ranking factors. Note that this feature is not
   currently supported by the Sphinx API.

-  REMAP()
-  REMAP(condition, expression, (cond1, cond2, …), (expr1, expr2, …))
   function was added in 2.2.2-beta. It allows you to make some
   exceptions of an expression values depending on condition values.
   Condition expression should always result integer, expression can
   result in integer or float.

   ::


       SELECT REMAP(userid, karmapoints, (1, 67), (999, 0)) FROM users;
       SELECT REMAP(id%10, salary, (0), (0.0)) FROM employes;

-  rand()
-  RAND(seed) function was added in 2.3.2-beta. Returns a random float
   between 0..1. Optional, an integer seed value can be specified.
