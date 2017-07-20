docinfo
~~~~~~~

Document attribute values (docinfo) storage mode. Optional, default is
‘extern’. Known values are ‘none’, ‘extern’ and ‘inline’.

Docinfo storage mode defines how exactly docinfo will be physically
stored on disk and RAM. “none” means that there will be no docinfo at
all (ie. no attributes). Normally you need not to set “none” explicitly
because Manticore will automatically select “none” when there are no
attributes configured. “inline” means that the docinfo will be stored in
the ``.spd`` file, along with the document ID lists. “extern” means that
the docinfo will be stored separately (externally) from document ID
lists, in a special ``.spa`` file.

Basically, externally stored docinfo must be kept in RAM when querying.
for performance reasons. So in some cases “inline” might be the only
option. However, such cases are infrequent, and docinfo defaults to
“extern”. Refer to `the section called
“Attributes” <../../attributes.md>`__ for in-depth discussion and RAM
usage estimates.

Example:
^^^^^^^^

::


    docinfo = inline

