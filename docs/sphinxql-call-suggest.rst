.. raw:: html

   <div class="navheader">

8.17. CALL SUGGEST syntax
`Prev <sphinxql-call-qsuggest.html>`__ 
Chapter 8. SphinxQL reference
 `Next <sphinxql-show-tables.html>`__

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

.. rubric:: 8.17. CALL SUGGEST syntax
   :name: call-suggest-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. code:: programlisting

    CALL SUGGEST(word, index [,options])

CALL SUGGEST statement, introduced in version 2.3.2-beta. Works the same
as CALL QUSUGGEST, except that if a bag of words is present, the
statement will return suggestions only for the first word, ignoring the
rest. If the first paramenter is a word, the functionality of CALL
SUGGEST and CALL QSUGGEST is the same.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+------------------------------------+-----------------------------------------+
| `Prev <sphinxql-call-qsuggest.html>`__    | `Up <sphinxql-reference.html>`__   |  `Next <sphinxql-show-tables.html>`__   |
+-------------------------------------------+------------------------------------+-----------------------------------------+
| 8.16. CALL QSUGGEST syntax                | `Home <index.html>`__              |  8.18. SHOW TABLES syntax               |
+-------------------------------------------+------------------------------------+-----------------------------------------+

.. raw:: html

   </div>
