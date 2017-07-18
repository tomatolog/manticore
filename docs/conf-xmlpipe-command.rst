.. raw:: html

   <div class="navheader">

12.1.31. xmlpipe\_command
`Prev <conf-sql-ranged-throttle.html>`__ 
12.1. Data source configuration options
 `Next <conf-xmlpipe-field.html>`__

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

.. rubric:: 12.1.31. xmlpipe\_command
   :name: xmlpipe_command
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Shell command that invokes xmlpipe2 stream producer. Mandatory. Applies
to ``xmlpipe2`` source types only.

Specifies a command that will be executed and which output will be
parsed for documents. Refer to `Section 3.9, “xmlpipe2 data
source” <xmlpipe2.html>`__ for specific format description.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    xmlpipe_command = cat /home/sphinx/test.xml

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------------+----------------------------------+---------------------------------------+
| `Prev <conf-sql-ranged-throttle.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-xmlpipe-field.html>`__   |
+---------------------------------------------+----------------------------------+---------------------------------------+
| 12.1.30. sql\_ranged\_throttle              | `Home <index.html>`__            |  12.1.32. xmlpipe\_field              |
+---------------------------------------------+----------------------------------+---------------------------------------+

.. raw:: html

   </div>
