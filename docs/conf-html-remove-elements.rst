.. raw:: html

   <div class="navheader">

12.2.29. html\_remove\_elements
`Prev <conf-html-index-attrs.html>`__ 
12.2. Index configuration options
 `Next <conf-local.html>`__

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

.. rubric:: 12.2.29. html\_remove\_elements
   :name: html_remove_elements
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

A list of HTML elements for which to strip contents along with the
elements themselves. Optional, default is empty string (do not strip
contents of any elements).

This feature allows to strip element contents, ie. everything that is
between the opening and the closing tags. It is useful to remove
embedded scripts, CSS, etc. Short tag form for empty elements (ie. <br
/>) is properly supported; ie. the text that follows such tag will
**not** be removed.

The value is a comma-separated list of element (tag) names whose
contents should be removed. Tag names are case insensitive.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    html_remove_elements = style, script

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------------------+---------------------------------+-------------------------------+
| `Prev <conf-html-index-attrs.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-local.html>`__   |
+------------------------------------------+---------------------------------+-------------------------------+
| 12.2.28. html\_index\_attrs              | `Home <index.html>`__           |  12.2.30. local               |
+------------------------------------------+---------------------------------+-------------------------------+

.. raw:: html

   </div>
