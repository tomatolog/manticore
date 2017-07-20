lemmatizer\_base
~~~~~~~~~~~~~~~~

Lemmatizer dictionaries base path. Optional, default is /usr/local/share
(as in –datadir switch to ./configure script).

Our lemmatizer implementation (see `the section called
“morphology” <../../index_configuration_options/morphology.md>`__ for a
discussion of what lemmatizers are) is dictionary driven.
lemmatizer\_base directive configures the base dictionary path. File
names are hardcoded and specific to a given lemmatizer; the Russian
lemmatizer uses ru.pak dictionary file. The dictionaries can be obtained
from the Manticore website.

Example:
^^^^^^^^

::


    lemmatizer_base = /usr/local/share/sphinx/dicts/

