on\_file\_field\_error
~~~~~~~~~~~~~~~~~~~~~~

How to handle IO errors in file fields. Optional, default is
``ignore_field``. Introduced in version 2.0.2-beta.

When there is a problem indexing a file referenced by a file field (`the
section called
“sql\_file\_field” <../../data_source_configuration_options/sqlfile_field.rst>`__),
``indexer`` can either index the document, assuming empty content in
this particular field, or skip the document, or fail indexing entirely.
``on_file_field_error`` directive controls that behavior. The values it
takes are:

-  ``ignore_field``, index the current document without field;

-  ``skip_document``, skip the current document but continue indexing;

-  ``fail_index``, fail indexing with an error message.

The problems that can arise are: open error, size error (file too big),
and data read error. Warning messages on any problem will be given at
all times, irregardless of the phase and the ``on_file_field_error``
setting.

Note that with ``on_file_field_error = skip_document`` documents will
only be ignored if problems are detected during an early check phase,
and <b>not</b> during the actual file parsing phase. ``indexer`` will
open every referenced file and check its size before doing any work, and
then open it again when doing actual parsing work. So in case a file
goes away between these two open attempts, the document will still be
indexed.

Example:
^^^^^^^^

::


    on_file_field_error = skip_document

