.. raw:: html

   <div class="navheader">

12.3.7. on\_file\_field\_error
`Prev <conf-max-file-field-buffer.html>`__ 
12.3. \ ``indexer`` program configuration options
 `Next <conf-lemmatizer-cache.html>`__

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

.. rubric:: 12.3.7. on\_file\_field\_error
   :name: on_file_field_error
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

How to handle IO errors in file fields. Optional, default is
``ignore_field``. Introduced in version 2.0.2-beta.

When there is a problem indexing a file referenced by a file field
(`Section 12.1.27, “sql\_file\_field” <conf-sql-file-field.html>`__),
``indexer`` can either index the document, assuming empty content in
this particular field, or skip the document, or fail indexing entirely.
``on_file_field_error`` directive controls that behavior. The values it
takes are:

.. raw:: html

   <div class="itemizedlist">

-  ``ignore_field``, index the current document without field;

-  ``skip_document``, skip the current document but continue indexing;

-  ``fail_index``, fail indexing with an error message.

.. raw:: html

   </div>

The problems that can arise are: open error, size error (file too big),
and data read error. Warning messages on any problem will be given at
all times, irregardless of the phase and the ``on_file_field_error``
setting.

Note that with ``on_file_field_error = skip_document`` documents will
only be ignored if problems are detected during an early check phase,
and **not** during the actual file parsing phase. ``indexer`` will open
every referenced file and check its size before doing any work, and then
open it again when doing actual parsing work. So in case a file goes
away between these two open attempts, the document will still be
indexed.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    on_file_field_error = skip_document

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+-----------------------------------+------------------------------------------+
| `Prev <conf-max-file-field-buffer.html>`__    | `Up <confgroup-indexer.html>`__   |  `Next <conf-lemmatizer-cache.html>`__   |
+-----------------------------------------------+-----------------------------------+------------------------------------------+
| 12.3.6. max\_file\_field\_buffer              | `Home <index.html>`__             |  12.3.8. lemmatizer\_cache               |
+-----------------------------------------------+-----------------------------------+------------------------------------------+

.. raw:: html

   </div>
