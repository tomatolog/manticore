embedded\_limit
~~~~~~~~~~~~~~~

Embedded exceptions, wordforms, or stopwords file size limit. Optional,
default is 16K.

Indexer can either save the file name, or embed the file contents
directly into the index. Files sized under ``embedded_limit`` get stored
into the index. For bigger files, only the file names are stored. This
also simplifies moving index files to a different machine; you may get
by just copying a single file.

With smaller files, such embedding reduces the number of the external
files on which the index depends, and helps maintenance. But at the same
time it makes no sense to embed a 100 MB wordforms dictionary into a
tiny delta index. So there needs to be a size threshold, and
``embedded_limit`` is that threshold.

Example:
^^^^^^^^

::


    embedded_limit = 32K

