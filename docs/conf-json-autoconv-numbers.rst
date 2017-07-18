.. raw:: html

   <div class="navheader">

12.5.3. json\_autoconv\_numbers
`Prev <conf-on-json-attr-error.html>`__ 
12.5. Common section configuration options
 `Next <conf-json-autoconv-keynames.html>`__

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

.. rubric:: 12.5.3. json\_autoconv\_numbers
   :name: json_autoconv_numbers
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Automatically detect and convert possible JSON strings that represent
numbers, into numeric attributes. Optional, default value is 0 (do not
convert strings into numbers). Added in 2.1.1-beta.

When this option is 1, values such as “1234” will be indexed as numbers
instead of strings; if the option is 0, such values will be indexed as
strings. This conversion applies to any data source, that is, JSON
attributes originating from either SQL or XMLpipe2 sources will all be
affected.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    json_autoconv_numbers = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+------------------------------------------------+
| `Prev <conf-on-json-attr-error.html>`__    | `Up <confgroup-common.html>`__   |  `Next <conf-json-autoconv-keynames.html>`__   |
+--------------------------------------------+----------------------------------+------------------------------------------------+
| 12.5.2. on\_json\_attr\_error              | `Home <index.html>`__            |  12.5.4. json\_autoconv\_keynames              |
+--------------------------------------------+----------------------------------+------------------------------------------------+

.. raw:: html

   </div>
