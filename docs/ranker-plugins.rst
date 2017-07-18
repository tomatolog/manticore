.. raw:: html

   <div class="navheader">

6.3. Ranker plugins
`Prev <sphinx-plugins.html>`__ 
Chapter 6. Extending Sphinx
 `Next <command-line-tools.html>`__

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

.. rubric:: 6.3. Ranker plugins
   :name: ranker-plugins
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Ranker plugins let you implement a custom ranker that receives all the
occurrences of the keywords matched in the document, and computes a
WEIGHT() value. They can be called as follows:

.. code:: programlisting

    SELECT id, attr1 FROM test WHERE match('hello')
    OPTION ranker=myranker('option1=1');

The call workflow is as follows:

.. raw:: html

   <div class="orderedlist">

1. ``XXX_init()`` gets called once per query per index, in the very
   beginning. A few query-wide options are passed to it through a
   ``SPH_RANKER_INIT`` structure, including the user options strings (in
   the example just above, “option1=1” is that string).
2. ``XXX_update()`` gets called multiple times per matched document,
   with every matched keyword occurrence passed as its parameter, a
   ``SPH_RANKER_HIT`` structure. The occurrences within each document
   are guaranteed to be passed in the order of ascending
   ``hit->hit_pos`` values.
3. ``XXX_finalize()`` gets called once per matched document, once there
   are no more keyword occurrences. It must return the WEIGHT() value.
   This is the only mandatory function.
4. ``XXX_deinit()`` gets called once per query, in the very end.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------+----------------------------------+--------------------------------------------+
| `Prev <sphinx-plugins.html>`__    | `Up <extending-sphinx.html>`__   |  `Next <command-line-tools.html>`__        |
+-----------------------------------+----------------------------------+--------------------------------------------+
| 6.2. Sphinx plugins               | `Home <index.html>`__            |  Chapter 7. Command line tools reference   |
+-----------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
