.. raw:: html

   <div class="navheader">

5.6. Sorting modes
`Prev <misc-functions.html>`__ 
Chapter 5. Searching
 `Next <clustering.html>`__

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

.. rubric:: 5.6. Sorting modes
   :name: sorting-modes
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

There are the following result sorting modes available:

.. raw:: html

   <div class="itemizedlist">

-  SPH\_SORT\_RELEVANCE mode, that sorts by relevance in descending
   order (best matches first);

-  SPH\_SORT\_ATTR\_DESC mode, that sorts by an attribute in descending
   order (bigger attribute values first);

-  SPH\_SORT\_ATTR\_ASC mode, that sorts by an attribute in ascending
   order (smaller attribute values first);

-  SPH\_SORT\_TIME\_SEGMENTS mode, that sorts by time segments (last
   hour/day/week/month) in descending order, and then by relevance in
   descending order;

-  SPH\_SORT\_EXTENDED mode, that sorts by SQL-like combination of
   columns in ASC/DESC order;

-  SPH\_SORT\_EXPR mode, that sorts by an arithmetic expression.

.. raw:: html

   </div>

SPH\_SORT\_RELEVANCE ignores any additional parameters and always sorts
matches by relevance rank. All other modes require an additional sorting
clause, with the syntax depending on specific mode.
SPH\_SORT\_ATTR\_ASC, SPH\_SORT\_ATTR\_DESC and
SPH\_SORT\_TIME\_SEGMENTS modes require simply an attribute name.
SPH\_SORT\_RELEVANCE is equivalent to sorting by “@weight DESC, @id ASC”
in extended sorting mode, SPH\_SORT\_ATTR\_ASC is equivalent to
“attribute ASC, @weight DESC, @id ASC”, and SPH\_SORT\_ATTR\_DESC to
“attribute DESC, @weight DESC, @id ASC” respectively.

.. rubric:: SPH\_SORT\_TIME\_SEGMENTS mode
   :name: sph_sort_time_segments-mode

In SPH\_SORT\_TIME\_SEGMENTS mode, attribute values are split into
so-called time segments, and then sorted by time segment first, and by
relevance second.

The segments are calculated according to the *current timestamp* at the
time when the search is performed, so the results would change over
time. The segments are as follows:

.. raw:: html

   <div class="itemizedlist">

-  last hour,

-  last day,

-  last week,

-  last month,

-  last 3 months,

-  everything else.

.. raw:: html

   </div>

These segments are hardcoded, but it is trivial to change them if
necessary.

This mode was added to support searching through blogs, news headlines,
etc. When using time segments, recent records would be ranked higher
because of segment, but within the same segment, more relevant records
would be ranked higher - unlike sorting by just the timestamp attribute,
which would not take relevance into account at all.

.. rubric:: SPH\_SORT\_EXTENDED mode
   :name: sph_sort_extended-mode

In SPH\_SORT\_EXTENDED mode, you can specify an SQL-like sort expression
with up to 5 attributes (including internal attributes), eg:

.. code:: programlisting

    @relevance DESC, price ASC, @id DESC

Both internal attributes (that are computed by the engine on the fly)
and user attributes that were configured for this index are allowed.
Internal attribute names must start with magic @-symbol; user attribute
names can be used as is. In the example above, ``@relevance`` and
``@id`` are internal attributes and ``price`` is user-specified.

Known internal attributes are:

.. raw:: html

   <div class="itemizedlist">

-  @id (match ID)

-  @weight (match weight)

-  @rank (match weight)

-  @relevance (match weight)

-  @random (return results in random order)

.. raw:: html

   </div>

``@rank`` and ``@relevance`` are just additional aliases to ``@weight``.

.. rubric:: SPH\_SORT\_EXPR mode
   :name: sph_sort_expr-mode

Expression sorting mode lets you sort the matches by an arbitrary
arithmetic expression, involving attribute values, internal attributes
(@id and @weight), arithmetic operations, and a number of built-in
functions. Here’s an example:

.. code:: programlisting

    $cl->SetSortMode ( SPH_SORT_EXPR,
        "@weight + ( user_karma + ln(pageviews) )*0.1" );

The operators and functions supported in the expressions are discussed
in a separate section, `Section 5.5, “Expressions, functions, and
operators” <expressions.html>`__.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+---------------------------+----------------------------------------------+
| `Prev <misc-functions.html>`__    | `Up <searching.html>`__   |  `Next <clustering.html>`__                  |
+-----------------------------------+---------------------------+----------------------------------------------+
| 5.5.6. Miscellaneous functions    | `Home <index.html>`__     |  5.7. Grouping (clustering) search results   |
+-----------------------------------+---------------------------+----------------------------------------------+

.. raw:: html

   </div>
