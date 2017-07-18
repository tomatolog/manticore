.. raw:: html

   <div class="navheader">

12.5.1. lemmatizer\_base
`Prev <confgroup-common.html>`__ 
12.5. Common section configuration options
 `Next <conf-on-json-attr-error.html>`__

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

.. rubric:: 12.5.1. lemmatizer\_base
   :name: lemmatizer_base
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Lemmatizer dictionaries base path. Optional, default is /usr/local/share
(as in –datadir switch to ./configure script). Added in version
2.1.1-beta.

Our lemmatizer implementation (see `Section 12.2.6,
“morphology” <conf-morphology.html>`__ for a discussion of what
lemmatizers are) is dictionary driven. lemmatizer\_base directive
configures the base dictionary path. File names are hardcoded and
specific to a given lemmatizer; the Russian lemmatizer uses ru.pak
dictionary file. The dictionaries can be obtained from the Sphinx
website.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    lemmatizer_base = /usr/local/share/sphinx/dicts/

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+----------------------------------+--------------------------------------------+
| `Prev <confgroup-common.html>`__              | `Up <confgroup-common.html>`__   |  `Next <conf-on-json-attr-error.html>`__   |
+-----------------------------------------------+----------------------------------+--------------------------------------------+
| 12.5. Common section configuration options    | `Home <index.html>`__            |  12.5.2. on\_json\_attr\_error             |
+-----------------------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
