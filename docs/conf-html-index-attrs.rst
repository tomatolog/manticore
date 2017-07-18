.. raw:: html

   <div class="navheader">

12.2.28. html\_index\_attrs
`Prev <conf-html-strip.html>`__ 
12.2. Index configuration options
 `Next <conf-html-remove-elements.html>`__

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

.. rubric:: 12.2.28. html\_index\_attrs
   :name: html_index_attrs
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A list of markup attributes to index when stripping HTML. Optional,
default is empty (do not index markup attributes).

Specifies HTML markup attributes whose contents should be retained and
indexed even though other HTML markup is stripped. The format is per-tag
enumeration of indexable attributes, as shown in the example below.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    html_index_attrs = img=alt,title; a=title;

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------+---------------------------------+----------------------------------------------+
| `Prev <conf-html-strip.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-html-remove-elements.html>`__   |
+------------------------------------+---------------------------------+----------------------------------------------+
| 12.2.27. html\_strip               | `Home <index.html>`__           |  12.2.29. html\_remove\_elements             |
+------------------------------------+---------------------------------+----------------------------------------------+

.. raw:: html

   </div>
