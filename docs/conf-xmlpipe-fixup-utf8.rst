.. raw:: html

   <div class="navheader">

12.1.43. xmlpipe\_fixup\_utf8
`Prev <conf-xmlpipe-attr-json.html>`__ 
12.1. Data source configuration options
 `Next <conf-mssql-winauth.html>`__

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

.. rubric:: 12.1.43. xmlpipe\_fixup\_utf8
   :name: xmlpipe_fixup_utf8
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Perform Sphinx-side UTF-8 validation and filtering to prevent XML parser
from choking on non-UTF-8 documents. Optional, default is 0. Applies to
``xmlpipe2`` source type only.

Under certain occasions it might be hard or even impossible to guarantee
that the incoming XMLpipe2 document bodies are in perfectly valid and
conforming UTF-8 encoding. For instance, documents with national
single-byte encodings could sneak into the stream. libexpat XML parser
is fragile, meaning that it will stop processing in such cases. UTF8
fixup feature lets you avoid that. When fixup is enabled, Sphinx will
preprocess the incoming stream before passing it to the XML parser and
replace invalid UTF-8 sequences with spaces.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    xmlpipe_fixup_utf8 = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-------------------------------------------+----------------------------------+---------------------------------------+
| `Prev <conf-xmlpipe-attr-json.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-mssql-winauth.html>`__   |
+-------------------------------------------+----------------------------------+---------------------------------------+
| 12.1.42. xmlpipe\_attr\_json              | `Home <index.html>`__            |  12.1.44. mssql\_winauth              |
+-------------------------------------------+----------------------------------+---------------------------------------+

.. raw:: html

   </div>
