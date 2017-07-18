.. raw:: html

   <div class="navheader">

5.3. Extended query syntax
`Prev <boolean-syntax.html>`__ 
Chapter 5. Searching
 `Next <weighting.html>`__

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

.. rubric:: 5.3. Extended query syntax
   :name: extended-query-syntax
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

The following special operators and modifiers can be used when using the
extended matching mode:

.. raw:: html

   <div class="itemizedlist">

-  operator OR:

   .. code:: programlisting

       hello | world

-  operator MAYBE (introduced in verion 2.2.3-beta):

   .. code:: programlisting

       hello MAYBE world

-  operator NOT:

   .. code:: programlisting

       hello -world
       hello !world

-  field search operator:

   .. code:: programlisting

       @title hello @body world

-  field position limit modifier (introduced in version 0.9.9-rc1):

   .. code:: programlisting

       @body[50] hello

-  multiple-field search operator:

   .. code:: programlisting

       @(title,body) hello world

-  ignore field search operator (will ignore any matches of ‘hello
   world’ from field ‘title’):

   .. code:: programlisting

       @!title hello world

-  ignore multiple-field search operator (if we have fields title,
   subject and body then @!(title) is equivalent to @(subject,body)):

   .. code:: programlisting

       @!(title,body) hello world

-  all-field search operator:

   .. code:: programlisting

       @* hello

-  phrase search operator:

   .. code:: programlisting

       "hello world"

-  proximity search operator:

   .. code:: programlisting

       "hello world"~10

-  quorum matching operator:

   .. code:: programlisting

       "the world is a wonderful place"/3

-  strict order operator (aka operator “before”):

   .. code:: programlisting

       aaa << bbb << ccc

-  exact form modifier (introduced in version 0.9.9-rc1):

   .. code:: programlisting

       raining =cats and =dogs

-  field-start and field-end modifier (introduced in version 0.9.9-rc2):

   .. code:: programlisting

       ^hello world$

-  keyword IDF boost modifier (introduced in version 2.2.3-beta):

   .. code:: programlisting

       boosted^1.234 boostedfieldend$^1.234

-  NEAR, generalized proximity operator (introduced in version
   2.0.1-beta):

   .. code:: programlisting

       hello NEAR/3 world NEAR/4 "my test"

-  SENTENCE operator (introduced in version 2.0.1-beta):

   .. code:: programlisting

       all SENTENCE words SENTENCE "in one sentence"

-  PARAGRAPH operator (introduced in version 2.0.1-beta):

   .. code:: programlisting

       "Bill Gates" PARAGRAPH "Steve Jobs"

-  ZONE limit operator:

   .. code:: programlisting

       ZONE:(h3,h4)

   only in these titles

-  ZONESPAN limit operator:

   .. code:: programlisting

       ZONESPAN:(h2)

   only in a (single) title

.. raw:: html

   </div>

Here’s an example query that uses some of these operators:

.. raw:: html

   <div class="example">

**Example 5.2. Extended matching mode: query example**

.. raw:: html

   <div class="example-contents">

.. code:: programlisting

    "hello world" @title "example program"~5 @body python -(php|perl) @* code

.. raw:: html

   </div>

.. raw:: html

   </div>

| 
| The full meaning of this search is:

.. raw:: html

   <div class="itemizedlist">

-  Find the words ‘hello’ and ‘world’ adjacently in any field in a
   document;

-  Additionally, the same document must also contain the words ‘example’
   and ‘program’ in the title field, with up to, but not including, 5
   words between the words in question; (E.g. “example PHP program”
   would be matched however “example script to introduce outside data
   into the correct context for your program” would not because two
   terms have 5 or more words between them)

-  Additionally, the same document must contain the word ‘python’ in the
   body field, but not contain either ‘php’ or ‘perl’;

-  Additionally, the same document must contain the word ‘code’ in any
   field.

.. raw:: html

   </div>

There always is implicit AND operator, so “hello world” means that both
“hello” and “world” must be present in matching document.

OR operator precedence is higher than AND, so “looking for cat \| dog \|
mouse” means “looking for ( cat \| dog \| mouse )” and *not* “(looking
for cat) \| dog \| mouse”.

Field limit operator limits subsequent searching to a given field.
Normally, query will fail with an error message if given field name does
not exist in the searched index. However, that can be suppressed by
specifying “@@relaxed” option at the very beginning of the query:

.. code:: programlisting

    @@relaxed @nosuchfield my query

This can be helpful when searching through heterogeneous indexes with
different schemas.

Field position limit, introduced in version 0.9.9-rc1, additionally
restricts the searching to first N position within given field (or
fields). For example, “@body[50] hello” will **not** match the documents
where the keyword ‘hello’ occurs at position 51 and below in the body.

Proximity distance is specified in words, adjusted for word count, and
applies to all words within quotes. For instance, “cat dog mouse”~5
query means that there must be less than 8-word span which contains all
3 words, ie. “CAT aaa bbb ccc DOG eee fff MOUSE” document will *not*
match this query, because this span is exactly 8 words long.

Quorum matching operator introduces a kind of fuzzy matching. It will
only match those documents that pass a given threshold of given words.
The example above (“the world is a wonderful place”/3) will match all
documents that have at least 3 of the 6 specified words. Operator is
limited to 255 keywords. Instead of an absolute number, you can also
specify a number between 0.0 and 1.0 (standing for 0% and 100%), and
Sphinx will match only documents with at least the specified percentage
of given words. The same example above could also have been written “the
world is a wonderful place”/0.5 and it would match documents with at
least 50% of the 6 words.

Strict order operator (aka operator “before”), introduced in version
0.9.9-rc2, will match the document only if its argument keywords occur
in the document exactly in the query order. For instance, “black << cat”
query (without quotes) will match the document “black and white cat” but
*not* the “that cat was black” document. Order operator has the lowest
priority. It can be applied both to just keywords and more complex
expressions, ie. this is a valid query:

.. code:: programlisting

    (bag of words) << "exact phrase" << red|green|blue

Exact form keyword modifier, introduced in version 0.9.9-rc1, will match
the document only if the keyword occurred in exactly the specified form.
The default behavior is to match the document if the stemmed keyword
matches. For instance, “runs” query will match both the document that
contains “runs” *and* the document that contains “running”, because both
forms stem to just “run” - while “=runs” query will only match the first
document. Exact form operator requires
`index\_exact\_words <conf-index-exact-words.html>`__ option to be
enabled. This is a modifier that affects the keyword and thus can be
used within operators such as phrase, proximity, and quorum operators.
Starting with 2.2.2-beta, it is possible to apply an exact form modifier
to the phrase operator. It’s really just syntax sugar - it adds an exact
form modifier to all terms contained within the phrase.

.. code:: programlisting

    ="exact phrase"

Field-start and field-end keyword modifiers, introduced in version
0.9.9-rc2, will make the keyword match only if it occurred at the very
start or the very end of a fulltext field, respectively. For instance,
the query “^hello world$” (with quotes and thus combining phrase
operator and start/end modifiers) will only match documents that contain
at least one field that has exactly these two keywords.

Starting with 0.9.9-rc1, arbitrarily nested brackets and negations are
allowed. However, the query must be possible to compute without
involving an implicit list of all documents:

.. code:: programlisting

    // correct query
    aaa -(bbb -(ccc ddd))

    // queries that are non-computable
    -aaa
    aaa | -bbb

Starting with 2.2.2-beta, the phrase search operator may include a
‘match any term’ modifier. Terms within the phrase operator are position
significant. When the ‘match any term’ modifier is implemented, the
position of the subsequent terms from that phrase query will be shifted.
Therefore, ‘match any’ has no impact on search performance.

.. code:: programlisting

    "exact * phrase * * for terms"

**NEAR operator**, added in 2.0.1-beta, is a generalized version of a
proximity operator. The syntax is ``NEAR/N``, it is case-sensitive, and
no spaces are allowed between the NEAR keyword, the slash sign, and the
distance value.

The original proximity operator only worked on sets of keywords. NEAR is
more generic and can accept arbitrary subexpressions as its two
arguments, matching the document when both subexpressions are found
within N words of each other, no matter in which order. NEAR is left
associative and has the same (lowest) precedence as BEFORE.

You should also note how a ``(one NEAR/7 two NEAR/7 three)`` query using
NEAR is not really equivalent to a ``("one two three"~7)`` one using
keyword proximity operator. The difference here is that the proximity
operator allows for up to 6 non-matching words between all the 3
matching words, but the version with NEAR is less restrictive: it would
allow for up to 6 words between ‘one’ and ‘two’ and then for up to 6
more between that two-word matching and a ‘three’ keyword.

**SENTENCE and PARAGRAPH operators**, added in 2.0.1-beta, matches the
document when both its arguments are within the same sentence or the
same paragraph of text, respectively. The arguments can be either
keywords, or phrases, or the instances of the same operator. Here are a
few examples:

.. code:: programlisting

    one SENTENCE two
    one SENTENCE "two three"
    one SENTENCE "two three" SENTENCE four

The order of the arguments within the sentence or paragraph does not
matter. These operators only work on indexes built with
`index\_sp <conf-index-sp.html>`__ (sentence and paragraph indexing
feature) enabled, and revert to a mere AND otherwise. Refer to the
``index_sp`` directive documentation for the notes on what’s considered
a sentence and a paragraph.

**ZONE limit operator**, added in 2.0.1-beta, is quite similar to field
limit operator, but restricts matching to a given in-field zone or a
list of zones. Note that the subsequent subexpressions are *not*
required to match in a single contiguous span of a given zone, and may
match in multiple spans. For instance, ``(ZONE:th hello world)`` query
*will* match this example document:

.. code:: programlisting

    <th>Table 1. Local awareness of Hello Kitty brand.</th>
    .. some table data goes here ..
    <th>Table 2. World-wide brand awareness.</th>

ZONE operator affects the query until the next field or ZONE limit
operator, or the closing parenthesis. It only works on the indexes built
with zones support (see `Section 12.2.9,
“index\_zones” <conf-index-zones.html>`__) and will be ignored
otherwise.

**ZONESPAN limit operator**, added in 2.1.1-beta, is similar to the ZONE
operator, but requires the match to occur in a single contiguous span.
In the example above, ``(ZONESPAN:th hello world)>`` would not match the
document, since “hello” and “world” do not occur within the same span.

**MAYBE** operator was added in 2.2.3-beta. It works much like \|
operator but doesn’t return documents which match only right subtree
expression.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+---------------------------+--------------------------------+
| `Prev <boolean-syntax.html>`__    | `Up <searching.html>`__   |  `Next <weighting.html>`__     |
+-----------------------------------+---------------------------+--------------------------------+
| 5.2. Boolean query syntax         | `Home <index.html>`__     |  5.4. Search results ranking   |
+-----------------------------------+---------------------------+--------------------------------+

.. raw:: html

   </div>
