CALL SUGGEST syntax
-------------------

::


    CALL SUGGEST(word, index [,options])

CALL SUGGEST statement, introduced in version 2.3.2-beta. Works the same
as CALL QUSUGGEST, except that if a bag of words is present, the
statement will return suggestions only for the f.html word, ignoring the
rest. If the f.html paramenter is a word, the functionality of CALL
SUGGEST and CALL QSUGGEST is the same.
