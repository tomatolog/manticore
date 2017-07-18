.. raw:: html

   <div class="navheader">

12.2.4. docinfo
`Prev <conf-path.html>`__ 
12.2. Index configuration options
 `Next <conf-mlock.html>`__

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

.. rubric:: 12.2.4. docinfo
   :name: docinfo
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Document attribute values (docinfo) storage mode. Optional, default is
‘extern’. Known values are ‘none’, ‘extern’ and ‘inline’.

Docinfo storage mode defines how exactly docinfo will be physically
stored on disk and RAM. “none” means that there will be no docinfo at
all (ie. no attributes). Normally you need not to set “none” explicitly
because Sphinx will automatically select “none” when there are no
attributes configured. “inline” means that the docinfo will be stored in
the ``.spd`` file, along with the document ID lists. “extern” means that
the docinfo will be stored separately (externally) from document ID
lists, in a special ``.spa`` file.

Basically, externally stored docinfo must be kept in RAM when querying.
for performance reasons. So in some cases “inline” might be the only
option. However, such cases are infrequent, and docinfo defaults to
“extern”. Refer to `Section 3.3, “Attributes” <attributes.html>`__ for
in-depth discussion and RAM usage estimates.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    docinfo = inline

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+------------------------------+---------------------------------+-------------------------------+
| `Prev <conf-path.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-mlock.html>`__   |
+------------------------------+---------------------------------+-------------------------------+
| 12.2.3. path                 | `Home <index.html>`__           |  12.2.5. mlock                |
+------------------------------+---------------------------------+-------------------------------+

.. raw:: html

   </div>
