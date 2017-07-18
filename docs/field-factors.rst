.. raw:: html

   <div class="navheader">

5.4.6. Field-level ranking factors
`Prev <document-factors.html>`__ 
5.4. Search results ranking
 `Next <factor-aggr-functions.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 5.4.6. Field-level ranking factors
   :name: field-level-ranking-factors
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A **field-level factor** is a numeric value computed by the ranking
engine for every matched in-document text field with regards to the
current query. As more than one field can be matched by a query, but the
final weight needs to be a single integer value, these values need to be
folded into a single one. To achieve that, field-level factors can only
be used within a field aggregation function, they can **not** be used
anywhere in the expression. For example, you can not use ``(lcs+bm25)``
as your ranking expression, as ``lcs`` takes multiple values (one in
every matched field). You should use ``(sum(lcs)+bm25)`` instead, that
expression sums ``lcs`` over all matching fields, and then adds ``bm25``
to that per-field sum. Currently implemented field-level factors are:

.. raw:: html

   <div class="itemizedlist">

-  ``lcs`` (integer), the length of a maximum verbatim match between the
   document and the query, counted in words. LCS stands for Longest
   Common Subsequence (or Subset). Takes a minimum value of 1 when only
   stray keywords were matched in a field, and a maximum value of query
   keywords count when the entire query was matched in a field verbatim
   (in the exact query keywords order). For example, if the query is
   ‘hello world’ and the field contains these two words quoted from the
   query (that is, adjacent to each other, and exactly in the query
   order), ``lcs`` will be 2. For example, if the query is ‘hello world
   program’ and the field contains ‘hello world’, ``lcs`` will be 2.
   Note that any subset of the query keyword works, not just a subset of
   adjacent keywords. For example, if the query is ‘hello world program’
   and the field contains ‘hello (test program)’, ``lcs`` will be 2 just
   as well, because both ‘hello’ and ‘program’ matched in the same
   respective positions as they were in the query. Finally, if the query
   is ‘hello world program’ and the field contains ‘hello world
   program’, ``lcs`` will be 3. (Hopefully that is unsurprising at this
   point.)

-  ``user_weight`` (integer), the user specified per-field weight (refer
   to `SetFieldWeights() <api-func-setfieldweights.html>`__ in SphinxAPI
   and `OPTION field\_weights <sphinxql-select.html>`__ in SphinxQL
   respectively). The weights default to 1 if not specified explicitly.

-  ``hit_count`` (integer), the number of keyword occurrences that
   matched in the field. Note that a single keyword may occur multiple
   times. For example, if ‘hello’ occurs 3 times in a field and ‘world’
   occurs 5 times, ``hit_count`` will be 8.

-  ``word_count`` (integer), the number of unique keywords matched in
   the field. For example, if ‘hello’ and ‘world’ occur anywhere in a
   field, ``word_count`` will be 2, irregardless of how many times do
   both keywords occur.

-  ``tf_idf`` (float), the sum of TF\*IDF over all the keywords matched
   in the field. IDF is the Inverse Document Frequency, a floating point
   value between 0 and 1 that describes how frequent is the keywords
   (basically, 0 for a keyword that occurs in every document indexed,
   and 1 for a unique keyword that occurs in just a single document). TF
   is the Term Frequency, the number of matched keyword occurrences in
   the field. As a side note, ``tf_idf`` is actually computed by summing
   IDF over all matched occurrences. That’s by construction equivalent
   to summing TF\*IDF over all matched keywords.

-  ``min_hit_pos`` (integer), the position of the first matched keyword
   occurrence, counted in words. Indexing begins from position 1.

-  ``min_best_span_pos`` (integer), the position of the first maximum
   LCS occurrences span. For example, assume that our query was ‘hello
   world program’ and ‘hello world’ subphrase was matched twice in the
   field, in positions 13 and 21. Assume that ‘hello’ and ‘world’
   additionally occurred elsewhere in the field, but never next to each
   other and thus never as a subphrase match. In that case,
   ``min_best_span_pos`` will be 13. Note how for the single keyword
   queries ``min_best_span_pos`` will always equal ``min_hit_pos``.

-  ``exact_hit`` (boolean), whether a query was an exact match of the
   entire current field. Used in the SPH04 ranker.

-  ``min_idf``, ``max_idf``, and ``sum_idf`` (float), added in version
   2.1.1-beta. These factors respectively represent the min(idf),
   max(idf) and sum(idf) over all keywords that were matched in the
   field.

-  ``exact_order`` (boolean), added in version 2.2.1-beta. Whether all
   of the query keywords were matched in the field in the exact query
   order. For example, ``(microsoft office)`` query would yield
   exact\_order=1 in a field with the following contents:
   ``(We use Microsoft software in our office.)``. However, the very
   same query in a ``(Our office is Microsoft free.)`` field would yield
   exact\_order=0.

-  ``min_gaps`` (integer), added in version 2.2.1-beta, the minimum
   number of positional gaps between (just) the keywords matched in
   field. Always 0 when less than 2 keywords match; always greater or
   equal than 0 otherwise.

   For example, with a ``[big wolf]`` query, ``[big bad wolf]`` field
   would yield min\_gaps=1; ``[big bad hairy wolf]`` field would yield
   min\_gaps=2; ``[the wolf was scary and big]`` field would yield
   min\_gaps=3; etc. However, a field like ``[i heard a wolf howl]``
   would yield min\_gaps=0, because only one keyword would be matching
   in that field, and, naturally, there would be no gaps between the
   *matched*\ keywords.

   Therefore, this is a rather low-level, “raw” factor that you would
   most likely want to *adjust* before actually using for ranking.
   Specific adjustments depend heavily on your data and the resulting
   formula, but here are a few ideas you can start with: (a) any
   min\_gaps based boosts could be simply ignored when word\_count<2;
   (b) non-trivial min\_gaps values (i.e. when word\_count>=2) could be
   clamped with a certain “worst case” constant while trivial values
   (i.e. when min\_gaps=0 and word\_count<2) could be replaced by that
   constant; (c) a transfer function like 1/(1+min\_gaps) could be
   applied (so that better, smaller min\_gaps values would maximize it
   and worse, bigger min\_gaps values would fall off slowly); and so on.

-  ``lccs`` (integer), added in version 2.2.1-beta. Longest Common
   Contiguous Subsequence. A length of the longest subphrase that is
   common between the query and the document, computed in keywords.

   LCCS factor is rather similar to LCS but more restrictive, in a
   sense. While LCS could be greater than 1 though no two query words
   are matched next to each other, LCCS would only get greater than 1 if
   there are *exact*, contiguous query subphrases in the document. For
   example, (one two three four five) query vs (one hundred three
   hundred five hundred) document would yield lcs=3, but lccs=1, because
   even though mutual dispositions of 3 keywords (one, three, five)
   match between the query and the document, no 2 matching positions are
   actually next to each other.

   Note that LCCS still does not differentiate between the frequent and
   rare keywords; for that, see WLCCS.

-  ``wlccs`` (float), added in version 2.2.1-beta. Weighted Longest
   Common Contiguous Subsequence. A sum of IDFs of the keywords of the
   longest subphrase that is common between the query and the document.

   WLCCS is computed very similarly to LCCS, but every “suitable”
   keyword occurrence increases it by the keyword IDF rather than just
   by 1 (which is the case with LCS and LCCS). That lets us rank
   sequences of more rare and important keywords higher than sequences
   of frequent keywords, even if the latter are longer. For example, a
   query ``(Zanzibar bed and breakfast)`` would yield lccs=1 for a
   ``(hotels of Zanzibar)`` document, but lccs=3 against
   ``(London bed and breakfast)``, even though “Zanzibar” is actually
   somewhat more rare than the entire “bed and breakfast” phrase. WLCCS
   factor alleviates that problem by using the keyword frequencies.

-  ``atc`` (float), added in version 2.2.1-beta. Aggregate Term
   Closeness. A proximity based measure that grows higher when the
   document contains more groups of more closely located and more
   important (rare) query keywords. **WARNING:** you should use ATC with
   OPTION idf=’plain,tfidf\_unnormalized’; otherwise you would get
   unexpected results.

   ATC basically works as follows. For every keyword *occurrence* in the
   document, we compute the so called *term closeness*. For that, we
   examine all the other closest occurrences of all the query keywords
   (keyword itself included too) to the left and to the right of the
   subject occurrence, compute a distance dampening coefficient as k =
   pow(distance, -1.75) for those occurrences, and sum the dampened
   IDFs. Thus for every occurrence of every keyword, we get a
   “closeness” value that describes the “neighbors” of that occurrence.
   We then multiply those per-occurrence closenesses by their respective
   subject keyword IDF, sum them all, and finally, compute a logarithm
   of that sum.

   Or in other words, we process the best (closest) matched keyword
   pairs in the document, and compute pairwise “closenesses” as the
   product of their IDFs scaled by the distance coefficient:

   .. code:: programlisting

       pair_tc = idf(pair_word1) * idf(pair_word2) * pow(pair_distance, -1.75)

   We then sum such closenesses, and compute the final, log-dampened ATC
   value:

   .. code:: programlisting

       atc = log(1+sum(pair_tc))

   Note that this final dampening logarithm is exactly the reason you
   should use OPTION idf=plain, because without it, the expression
   inside the log() could be negative.

   Having closer keyword occurrences actually contributes *much* more to
   ATC than having more frequent keywords. Indeed, when the keywords are
   right next to each other, distance=1 and k=1; when there just one
   word in between them, distance=2 and k=0.297, with two words between,
   distance=3 and k=0.146, and so on. At the same time IDF attenuates
   somewhat slower. For example, in a 1 million document collection, the
   IDF values for keywords that match in 10, 100, and 1000 documents
   would be respectively 0.833, 0.667, and 0.500. So a keyword pair with
   two rather rare keywords that occur in just 10 documents each but
   with 2 other words in between would yield pair\_tc = 0.101 and thus
   just barely outweigh a pair with a 100-doc and a 1000-doc keyword
   with 1 other word between them and pair\_tc = 0.099. Moreover, a pair
   of two *unique*, 1-doc keywords with 3 words between them would get a
   pair\_tc = 0.088 and lose to a pair of two 1000-doc keywords located
   right next to each other and yielding a pair\_tc = 0.25. So,
   basically, while ATC does combine both keyword frequency and
   proximity, it is still somewhat favoring the proximity.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------+------------------------------------------------+
| `Prev <document-factors.html>`__         | `Up <weighting.html>`__   |  `Next <factor-aggr-functions.html>`__         |
+------------------------------------------+---------------------------+------------------------------------------------+
| 5.4.5. Document-level ranking factors    | `Home <index.html>`__     |  5.4.7. Ranking factor aggregation functions   |
+------------------------------------------+---------------------------+------------------------------------------------+

.. raw:: html

   </div>
