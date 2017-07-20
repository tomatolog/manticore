xmlpipe\_fixup\_utf8
~~~~~~~~~~~~~~~~~~~~

Perform Manticore-side UTF-8 validation and filtering to prevent XML parser
from choking on non-UTF-8 documents. Optional, default is 0. Applies to
``xmlpipe2`` source type only.

Under certain occasions it might be hard or even impossible to guarantee
that the incoming XMLpipe2 document bodies are in perfectly valid and
conforming UTF-8 encoding. For instance, documents with national
single-byte encodings could sneak into the stream. libexpat XML parser
is fragile, meaning that it will stop processing in such cases. UTF8
fixup feature lets you avoid that. When fixup is enabled, Manticore will
preprocess the incoming stream before passing it to the XML parser and
replace invalid UTF-8 sequences with spaces.

Example:
^^^^^^^^

::


    xmlpipe_fixup_utf8 = 1

