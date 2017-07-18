.. raw:: html

   <div class="navheader">

5.2. Boolean query syntax
`Prev <matching-modes.html>`__ 
Chapter 5. Searching
 `Next <extended-syntax.html>`__

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

.. rubric:: 5.2. Boolean query syntax
   :name: boolean-query-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Boolean queries allow the following special operators to be used:

.. raw:: html

   <div class="itemizedlist">

-  operator OR:

   .. code:: programlisting

       hello | world

-  operator NOT:

   .. code:: programlisting

       hello -world
       hello !world

-  grouping:

   .. code:: programlisting

       ( hello world )

.. raw:: html

   </div>

Here’s an example query which uses all these operators:

.. raw:: html

   <div class="example">

**Example 5.1. Boolean query example**

.. raw:: html

   <div class="example-contents">

.. code:: programlisting

    ( cat -dog ) | ( cat -mouse)

.. raw:: html

   </div>

.. raw:: html

   </div>

| 

There always is implicit AND operator, so “hello world” query actually
means “hello & world”.

OR operator precedence is higher than AND, so “looking for cat \| dog \|
mouse” means “looking for ( cat \| dog \| mouse )” and *not* “(looking
for cat) \| dog \| mouse”.

Since version 2.1.1-beta, queries may be automatically optimized if
OPTION boolean\_simplify=1 is specified. Some transformations performed
by this optimization include:

.. raw:: html

   <div class="itemizedlist">

-  Excess brackets: ((A \| B) \| C) becomes ( A \| B \| C ); ((A B) C)
   becomes ( A B C )

-  Excess AND NOT: ((A !N1) !N2) becomes (A !(N1 \| N2))

-  Common NOT: ((A !N) \| (B !N)) becomes ((A\|B) !N)

-  Common Compound NOT: ((A !(N AA)) \| (B !(N BB))) becomes (((A\|B)
   !N) \| (A !AA) \| (B !BB)) if the cost of evaluating N is greater
   than the added together costs of evaluating A and B

-  Common subterm: ((A (N \| AA)) \| (B (N \| BB))) becomes (((A\|B) N)
   \| (A AA) \| (B BB)) if the cost of evaluating N is greater than the
   added together costs of evaluating A and B

-  Common keywords: (A \| “A B”~N) becomes A; (“A B” \| “A B C”) becomes
   “A B”; (“A B”~N \| “A B C”~N) becomes (“A B”~N)

-  Common phrase: (“X A B” \| “Y A B”) becomes ((“X\|Y”) “A B”)

-  Common AND NOT: ((A !X) \| (A !Y) \| (A !Z)) becomes (A !(X Y Z))

-  Common OR NOT: ((A !(N \| N1)) \| (B !(N \| N2))) becomes (( (A !N1)
   \| (B !N2) ) !N)

.. raw:: html

   </div>

Note that optimizing the queries consumes CPU time, so for simple
queries -or for hand-optimized queries- you’ll do better with the
default boolean\_simplify=0 value. Simplifications are often better for
complex queries, or algorithmically generated queries.

Queries like “-dog”, which implicitly include all documents from the
collection, can not be evaluated. This is both for technical and
performance reasons. Technically, Sphinx does not always keep a list of
all IDs. Performance-wise, when the collection is huge (ie. 10-100M
documents), evaluating such queries could take very long.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+---------------------------+------------------------------------+
| `Prev <matching-modes.html>`__    | `Up <searching.html>`__   |  `Next <extended-syntax.html>`__   |
+-----------------------------------+---------------------------+------------------------------------+
| 5.1. Matching modes               | `Home <index.html>`__     |  5.3. Extended query syntax        |
+-----------------------------------+---------------------------+------------------------------------+

.. raw:: html

   </div>
