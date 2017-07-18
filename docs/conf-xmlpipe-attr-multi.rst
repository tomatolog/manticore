.. raw:: html

   <div class="navheader">

12.1.39. xmlpipe\_attr\_multi
`Prev <conf-xmlpipe-attr-float.html>`__ 
12.1. Data source configuration options
 `Next <conf-xmlpipe-attr-multi-64.html>`__

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

.. rubric:: 12.1.39. xmlpipe\_attr\_multi
   :name: xmlpipe_attr_multi
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

xmlpipe MVA attribute declaration. Multi-value, optional. Applies to
``xmlpipe2`` source type only.

This setting declares an MVA attribute tag in xmlpipe2 stream. The
contents of the specified tag will be parsed and a list of integers that
will constitute the MVA will be extracted, similar to how
`sql\_attr\_multi <conf-sql-attr-multi.html>`__ parses SQL column
contents when ‘field’ MVA source type is specified.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    xmlpipe_attr_multi = taglist

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------------+----------------------------------+-----------------------------------------------+
| `Prev <conf-xmlpipe-attr-float.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-xmlpipe-attr-multi-64.html>`__   |
+--------------------------------------------+----------------------------------+-----------------------------------------------+
| 12.1.38. xmlpipe\_attr\_float              | `Home <index.html>`__            |  12.1.40. xmlpipe\_attr\_multi\_64            |
+--------------------------------------------+----------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
