seamless\_rotate
~~~~~~~~~~~~~~~~

Prevents ``searchd`` stalls while rotating indexes with huge amounts of
data to precache. Optional, default is 1 (enable seamless rotation). On
Windows systems seamless rotation is disabled by default.

Indexes may contain some data that needs to be precached in RAM. At the
moment, ``.spa``, ``.spi`` and ``.spm`` files are fully precached (they
contain attribute data, MVA data, and keyword index, respectively.)
Without seamless rotate, rotating an index tries to use as little RAM as
possible and works as follows:

1. new queries are temporarily rejected (with “retry” error code);

2. ``searchd`` waits for all currently running queries to finish;

3. old index is deallocated and its files are renamed;

4. new index files are renamed and required RAM is allocated;

5. new index attribute and dictionary data is preloaded to RAM;

6. ``searchd`` resumes serving queries from new index.

However, if there's a lot of attribute or dictionary data, then
preloading step could take noticeable time - up to several minutes in
case of preloading 1-5+ GB files.

With seamless rotate enabled, rotation works as follows:

1. new index RAM storage is allocated;

2. new index attribute and dictionary data is asynchronously preloaded
   to RAM;

3. on success, old index is deallocated and both indexes' files are
   renamed;

4. on failure, new index is deallocated;

5. at any given moment, queries are served either from old or new index
   copy.

Seamless rotate comes at the cost of higher **peak** memory usage during
the rotation (because both old and new copies of ``.spa/.spi/.spm`` data
need to be in RAM while preloading new copy). Average usage stays the
same.

Example:
^^^^^^^^

::


    seamless_rotate = 1

