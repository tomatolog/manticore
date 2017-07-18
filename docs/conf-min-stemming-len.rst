.. raw:: html

   <div class="navheader">

12.2.10. min\_stemming\_len
`Prev <conf-index-zones.html>`__ 
12.2. Index configuration options
 `Next <conf-stopwords.html>`__

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

.. rubric:: 12.2.10. min\_stemming\_len
   :name: min_stemming_len
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Minimum word length at which to enable stemming. Optional, default is 1
(stem everything). Introduced in version 0.9.9-rc1.

Stemmers are not perfect, and might sometimes produce undesired results.
For instance, running “gps” keyword through Porter stemmer for English
results in “gp”, which is not really the intent. ``min_stemming_len``
feature lets you suppress stemming based on the source word length, ie.
to avoid stemming too short words. Keywords that are shorter than the
given threshold will not be stemmed. Note that keywords that are exactly
as long as specified **will** be stemmed. So in order to avoid stemming
3-character keywords, you should specify 4 for the value. For more
finely grained control, refer to `wordforms <conf-wordforms.html>`__
feature.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    min_stemming_len = 4

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------+---------------------------------+-----------------------------------+
| `Prev <conf-index-zones.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-stopwords.html>`__   |
+-------------------------------------+---------------------------------+-----------------------------------+
| 12.2.9. index\_zones                | `Home <index.html>`__           |  12.2.11. stopwords               |
+-------------------------------------+---------------------------------+-----------------------------------+

.. raw:: html

   </div>
