.. raw:: html

   <div class="navheader">

12.1.42. xmlpipe\_attr\_json
`Prev <conf-xmlpipe-attr-string.html>`__ 
12.1. Data source configuration options
 `Next <conf-xmlpipe-fixup-utf8.html>`__

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

.. rubric:: 12.1.42. xmlpipe\_attr\_json
   :name: xmlpipe_attr_json
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

JSON attribute declaration. Multi-value (ie. there may be more than one
such attribute declared), optional. Introduced in version 2.1.1-beta.

This directive is used to declare that the contents of a given XML tag
are to be treated as a JSON document and stored into a Sphinx index for
later use. Refer to `Section 12.1.24,
“sql\_attr\_json” <conf-sql-attr-json.html>`__ for more details on the
JSON attributes.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    xmlpipe_attr_json = properties

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+----------------------------------+--------------------------------------------+
| `Prev <conf-xmlpipe-attr-string.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-xmlpipe-fixup-utf8.html>`__   |
+---------------------------------------------+----------------------------------+--------------------------------------------+
| 12.1.41. xmlpipe\_attr\_string              | `Home <index.html>`__            |  12.1.43. xmlpipe\_fixup\_utf8             |
+---------------------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
