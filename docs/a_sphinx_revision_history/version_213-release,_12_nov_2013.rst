Version 2.1.3-release, 12 nov 2013
----------------------------------

Bug fixes
~~~~~~~~~

-  fixed #1753, path to re2 sources could not be set using
   ``--with-re2``, options ``--with-re2-libs`` and
   ``--with-re2-includes`` added to ``configure``

-  fixed #1739, erroneous conversion of RAM chunk into disk chunk when
   loading id32 index with id64 binary

-  fixed #1738, unlinking RAM chunk when converting it to disk chunk

-  fixed #1710, unable to filter by attributes created by
   index\_field\_lengths=1

-  fixed #1716, random crash with with multiple running threads

-  fixed crash while querying index with lemmatizer and wordforms
