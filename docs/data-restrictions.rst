.. raw:: html

   <div class="navheader">

3.6. Restrictions on the source data
`Prev <indexes.html>`__ 
Chapter 3. Indexing
 `Next <charsets.html>`__

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

.. rubric:: 3.6. Restrictions on the source data
   :name: restrictions-on-the-source-data
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

There are a few different restrictions imposed on the source data which
is going to be indexed by Sphinx, of which the single most important one
is:

 **ALL DOCUMENT IDS MUST BE UNIQUE UNSIGNED NON-ZERO INTEGER NUMBERS
(32-BIT OR 64-BIT, DEPENDING ON BUILD TIME SETTINGS).**

If this requirement is not met, different bad things can happen. For
instance, Sphinx can crash with an internal assertion while indexing; or
produce strange results when searching due to conflicting IDs. Also, a
1000-pound gorilla might eventually come out of your display and start
throwing barrels at you. You’ve been warned.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------+--------------------------+---------------------------------------------------------------------------+
| `Prev <indexes.html>`__    | `Up <indexing.html>`__   |  `Next <charsets.html>`__                                                 |
+----------------------------+--------------------------+---------------------------------------------------------------------------+
| 3.5. Indexes               | `Home <index.html>`__    |  3.7. Charsets, case folding, translation tables, and replacement rules   |
+----------------------------+--------------------------+---------------------------------------------------------------------------+

.. raw:: html

   </div>
