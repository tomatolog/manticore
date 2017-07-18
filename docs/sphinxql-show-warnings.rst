.. raw:: html

   <div class="navheader">

8.4. SHOW WARNINGS syntax
`Prev <sphinxql-show-meta.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-status.html>`__

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

.. rubric:: 8.4. SHOW WARNINGS syntax
   :name: show-warnings-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    SHOW WARNINGS

**SHOW WARNINGS** statement, introduced in version 0.9.9-rc2, can be
used to retrieve the warning produced by the latest query. The error
message will be returned along with the query itself:

.. code:: programlisting

    mysql> SELECT * FROM test1 WHERE MATCH('@@title hello') \G
    ERROR 1064 (42000): index test1: syntax error, unexpected TOK_FIELDLIMIT
    near '@title hello'

    mysql> SELECT * FROM test1 WHERE MATCH('@title -hello') \G
    ERROR 1064 (42000): index test1: query is non-computable (single NOT operator)

    mysql> SELECT * FROM test1 WHERE MATCH('"test doc"/3') \G
    *************************** 1. row ***************************
            id: 4
        weight: 2500
      group_id: 2
    date_added: 1231721236
    1 row in set, 1 warning (0.00 sec)

    mysql> SHOW WARNINGS \G
    *************************** 1. row ***************************
      Level: warning
       Code: 1000
    Message: quorum threshold too high (words=2, thresh=3); replacing quorum operator
             with AND operator
    1 row in set (0.00 sec)

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+------------------------------------+-----------------------------------------+
| `Prev <sphinxql-show-meta.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-status.html>`__   |
+---------------------------------------+------------------------------------+-----------------------------------------+
| 8.3. SHOW META syntax                 | `Home <index.html>`__              |  8.5. SHOW STATUS syntax                |
+---------------------------------------+------------------------------------+-----------------------------------------+

.. raw:: html

   </div>
