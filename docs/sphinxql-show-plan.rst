.. raw:: html

   <div class="navheader">

8.38. SHOW PLAN syntax
`Prev <sphinxql-optimize-index.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-databases.html>`__

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

.. rubric:: 8.38. SHOW PLAN syntax
   :name: show-plan-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW PLAN

SHOW PLAN statement, added in 2.1.2-release, displays the execution plan
of the previous SELECT statement. The plan gets generated and stored
during the actual execution, so profiling must be enabled in the current
session **before** running that statement. That can be done with a
``SET profiling=1`` statement.

Here’s a complete instrumentation example:

.. code:: programlisting

    mysql> SET profiling=1 \G
    Query OK, 0 rows affected (0.00 sec)

    mysql> SELECT id FROM lj WHERE MATCH('the i') LIMIT 1 \G
    *************************** 1. row ***************************
    id: 39815
    1 row in set (1.53 sec)

    mysql> SHOW PLAN \G
    *************************** 1. row ***************************
    Variable: transformed_tree
       Value: AND(
      AND(KEYWORD(the, querypos=1)),
      AND(KEYWORD(i, querypos=2)))
    1 row in set (0.00 sec)

And here’s a less trivial example that shows how the actually evaluated
query tree can be rather different from the original one because of
expansions and other transformations:

.. code:: programlisting

    mysql> SELECT * FROM test WHERE MATCH('@title abc* @body hey') \G SHOW PLAN \G
    ...
    *************************** 1. row ***************************
    Variable: transformed_tree
       Value: AND(
      OR(fields=(title), KEYWORD(abcx, querypos=1, expanded), KEYWORD(abcm, querypos=1, expanded)),
      AND(fields=(body), KEYWORD(hey, querypos=2)))
    1 row in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+------------------------------------+--------------------------------------------+
| `Prev <sphinxql-optimize-index.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-databases.html>`__   |
+--------------------------------------------+------------------------------------+--------------------------------------------+
| 8.37. OPTIMIZE INDEX syntax                | `Home <index.html>`__              |  8.39. SHOW DATABASES syntax               |
+--------------------------------------------+------------------------------------+--------------------------------------------+

.. raw:: html

   </div>
