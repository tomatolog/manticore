.. raw:: html

   <div class="navheader">

12.2.3. path
`Prev <conf-source.html>`__ 
12.2. Index configuration options
 `Next <conf-docinfo.html>`__

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

.. rubric:: 12.2.3. path
   :name: path
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Index files path and file name (without extension). Mandatory.

Path specifies both directory and file name, but without extension.
``indexer`` will append different extensions to this path when
generating final names for both permanent and temporary index files.
Permanent data files have several different extensions starting with
‘.sp’; temporary files’ extensions start with ‘.tmp’. It’s safe to
remove ``.tmp*`` files is if indexer fails to remove them automatically.

For reference, different index files store the following data:

.. raw:: html

   <div class="itemizedlist">

-  ``.spa`` stores document attributes (used in `extern
   docinfo <conf-docinfo.html>`__ storage mode only);

-  ``.spd`` stores matching document ID lists for each word ID;

-  ``.sph`` stores index header information;

-  ``.spi`` stores word lists (word IDs and pointers to ``.spd`` file);

-  ``.spk`` stores kill-lists;

-  ``.spm`` stores MVA data;

-  ``.spp`` stores hit (aka posting, aka word occurrence) lists for each
   word ID;

-  ``.sps`` stores string attribute data.

-  ``.spe`` stores skip-lists to speed up doc-list filtering

.. raw:: html

   </div>

.. rubric:: Example:
   :name: example

.. code:: programlisting

    path = /var/data/test1

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------+---------------------------------+---------------------------------+
| `Prev <conf-source.html>`__    | `Up <confgroup-index.html>`__   |  `Next <conf-docinfo.html>`__   |
+--------------------------------+---------------------------------+---------------------------------+
| 12.2.2. source                 | `Home <index.html>`__           |  12.2.4. docinfo                |
+--------------------------------+---------------------------------+---------------------------------+

.. raw:: html

   </div>
