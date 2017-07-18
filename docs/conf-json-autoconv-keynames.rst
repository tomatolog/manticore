.. raw:: html

   <div class="navheader">

12.5.4. json\_autoconv\_keynames
`Prev <conf-json-autoconv-numbers.html>`__ 
12.5. Common section configuration options
 `Next <conf-rlp-root.html>`__

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

.. rubric:: 12.5.4. json\_autoconv\_keynames
   :name: json_autoconv_keynames
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Whether and how to auto-convert key names within JSON attributes. Known
value is ‘lowercase’. Optional, default value is unspecified (do not
convert anything). Added in 2.1.1-beta.

When this directive is set to ‘lowercase’, key names within JSON
attributes will be automatically brought to lower case when indexing.
This conversion applies to any data source, that is, JSON attributes
originating from either SQL or XMLpipe2 sources will all be affected.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    json_autoconv_keynames = lowercase

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+----------------------------------+----------------------------------+
| `Prev <conf-json-autoconv-numbers.html>`__    | `Up <confgroup-common.html>`__   |  `Next <conf-rlp-root.html>`__   |
+-----------------------------------------------+----------------------------------+----------------------------------+
| 12.5.3. json\_autoconv\_numbers               | `Home <index.html>`__            |  12.5.5. rlp\_root               |
+-----------------------------------------------+----------------------------------+----------------------------------+

.. raw:: html

   </div>
