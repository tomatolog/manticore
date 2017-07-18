.. raw:: html

   <div class="navheader">

12.2.1. type
`Prev <confgroup-index.html>`__ 
12.2. Index configuration options
 `Next <conf-source.html>`__

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

.. rubric:: 12.2.1. type
   :name: type
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Index type. Known values are ‘plain’, ‘distributed’, ‘rt’ and
‘template’. Optional, default is ‘plain’ (plain local index).

Sphinx supports several different types of indexes. Versions 0.9.x
supported two index types: plain local indexes that are stored and
processed on the local machine; and distributed indexes, that involve
not only local searching but querying remote ``searchd`` instances over
the network as well (see `Section 5.8, “Distributed
searching” <distributed.html>`__). Version 1.10-beta also adds support
for so-called real-time indexes (or RT indexes for short) that are also
stored and processed locally, but additionally allow for on-the-fly
updates of the full-text index (see `Chapter 4, *Real-time
indexes* <rt-indexes.html>`__). Note that *attributes* can be updated
on-the-fly using either plain local indexes or RT ones. In 2.2.1-beta
template indexes was introduced. They are actually a pseudo-indexes
because they do not store any data. That means they do not create any
files on your hard drive. But you can use them for keywords and snippets
generation, which may be useful in some cases.

Index type setting lets you choose the needed type. By default, plain
local index type will be assumed.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    type = distributed

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+---------------------------------+--------------------------------+
| `Prev <confgroup-index.html>`__      | `Up <confgroup-index.html>`__   |  `Next <conf-source.html>`__   |
+--------------------------------------+---------------------------------+--------------------------------+
| 12.2. Index configuration options    | `Home <index.html>`__           |  12.2.2. source                |
+--------------------------------------+---------------------------------+--------------------------------+

.. raw:: html

   </div>
