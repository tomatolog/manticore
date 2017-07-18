## Boolean query syntax {#boolean-query-syntax}

Boolean queries allow the following special operators to be used:

*   operator OR:

    ```
    hello | world
    ```

*   operator NOT:

    ```

    hello -world
    hello !world

    ```

*   grouping:

    ```
    ( hello world )
    ```

Here&#039;s an example query which uses all these operators:

###### Example 5.1. Boolean query example {#example-5-1-boolean-query-example}

```

( cat -dog ) | ( cat -mouse)

```

There always is implicit AND operator, so &quot;hello world&quot; query actually means &quot;hello &amp; world&quot;.

OR operator precedence is higher than AND, so &quot;looking for cat | dog | mouse&quot; means &quot;looking for ( cat | dog | mouse )&quot; and _not_ &quot;(looking for cat) | dog | mouse&quot;.

Since version 2.1.1-beta, queries may be automatically optimized if OPTION boolean_simplify=1 is specified. Some transformations performed by this optimization include:

*   Excess brackets: ((A | B) | C) becomes ( A | B | C ); ((A B) C) becomes ( A B C )

*   Excess AND NOT: ((A !N1) !N2) becomes (A !(N1 | N2))

*   Common NOT: ((A !N) | (B !N)) becomes ((A|B) !N)

*   Common Compound NOT: ((A !(N AA)) | (B !(N BB))) becomes (((A|B) !N) | (A !AA) | (B !BB)) if the cost of evaluating N is greater than the added together costs of evaluating A and B

*   Common subterm: ((A (N | AA)) | (B (N | BB))) becomes (((A|B) N) | (A AA) | (B BB)) if the cost of evaluating N is greater than the added together costs of evaluating A and B

*   Common keywords: (A | &quot;A B&quot;~N) becomes A; (&quot;A B&quot; | &quot;A B C&quot;) becomes &quot;A B&quot;; (&quot;A B&quot;~N | &quot;A B C&quot;~N) becomes (&quot;A B&quot;~N)

*   Common phrase: (&quot;X A B&quot; | &quot;Y A B&quot;) becomes ((&quot;X|Y&quot;) &quot;A B&quot;)

*   Common AND NOT: ((A !X) | (A !Y) | (A !Z)) becomes (A !(X Y Z))

*   Common OR NOT: ((A !(N | N1)) | (B !(N | N2))) becomes (( (A !N1) | (B !N2) ) !N)

Note that optimizing the queries consumes CPU time, so for simple queries -or for hand-optimized queries- you&#039;ll do better with the default boolean_simplify=0 value. Simplifications are often better for complex queries, or algorithmically generated queries.

Queries like &quot;-dog&quot;, which implicitly include all documents from the collection, can not be evaluated. This is both for technical and performance reasons. Technically, Sphinx does not always keep a list of all IDs. Performance-wise, when the collection is huge (ie. 10-100M documents), evaluating such queries could take very long.