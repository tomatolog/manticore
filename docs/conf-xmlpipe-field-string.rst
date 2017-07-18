.. raw:: html

   <div class="navheader">

12.1.33. xmlpipe\_field\_string
`Prev <conf-xmlpipe-field.html>`__ 
12.1. Data source configuration options
 `Next <conf-xmlpipe-attr-uint.html>`__

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

.. rubric:: 12.1.33. xmlpipe\_field\_string
   :name: xmlpipe_field_string
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

xmlpipe field and string attribute declaration. Multi-value, optional.
Applies to ``xmlpipe2`` source type only. Refer to `Section 3.9,
“xmlpipe2 data source” <xmlpipe2.html>`__. Introduced in version
1.10-beta.

Makes the specified XML element indexed as both a full-text field and a
string attribute. Equivalent to <sphinx:field name=“field”
attr=“string”/> declaration within the XML file.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    xmlpipe_field_string = subject

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+----------------------------------+-------------------------------------------+
| `Prev <conf-xmlpipe-field.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-xmlpipe-attr-uint.html>`__   |
+---------------------------------------+----------------------------------+-------------------------------------------+
| 12.1.32. xmlpipe\_field               | `Home <index.html>`__            |  12.1.34. xmlpipe\_attr\_uint             |
+---------------------------------------+----------------------------------+-------------------------------------------+

.. raw:: html

   </div>
