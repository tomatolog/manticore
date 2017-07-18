.. raw:: html

   <div class="navheader">

12.2.25. phrase\_boundary
`Prev <conf-ngram-chars.html>`__ 
12.2. Index configuration options
 `Next <conf-phrase-boundary-step.html>`__

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

.. rubric:: 12.2.25. phrase\_boundary
   :name: phrase_boundary
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Phrase boundary characters list. Optional, default is empty.

This list controls what characters will be treated as phrase boundaries,
in order to adjust word positions and enable phrase-level search
emulation through proximity search. The syntax is similar to
`charset\_table <conf-charset-table.html>`__. Mappings are not allowed
and the boundary characters must not overlap with anything else.

On phrase boundary, additional word position increment (specified by
`phrase\_boundary\_step <conf-phrase-boundary-step.html>`__) will be
added to current word position. This enables phrase-level searching
through proximity queries: words in different phrases will be guaranteed
to be more than phrase\_boundary\_step distance away from each other; so
proximity search within that distance will be equivalent to phrase-level
search.

Phrase boundary condition will be raised if and only if such character
is followed by a separator; this is to avoid abbreviations such as
S.T.A.L.K.E.R or URLs being treated as several phrases.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    phrase_boundary = ., ?, !, U+2026 # horizontal ellipsis

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+---------------------------------+----------------------------------------------+
| `Prev <conf-ngram-chars.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-phrase-boundary-step.html>`__   |
+-------------------------------------+---------------------------------+----------------------------------------------+
| 12.2.24. ngram\_chars               | `Home <index.html>`__           |  12.2.26. phrase\_boundary\_step             |
+-------------------------------------+---------------------------------+----------------------------------------------+

.. raw:: html

   </div>
