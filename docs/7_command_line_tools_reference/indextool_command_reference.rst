``indextool`` command reference
-------------------------------

``indextool`` is one of the helper tools within the Sphinx package,
introduced in version 0.9.9-rc2. It is used to dump miscellaneous debug
information about the physical index. (Additional functionality such as
index verification is planned in the future, hence the indextool name
rather than just indexdump.) Its general usage is:

::


    indextool <command> [options]

Options apply to all commands:

-  ``--config &lt;file&gt;`` (``-c &lt;file&gt;`` for short) overrides
   the built-in config file names.

-  ``--quiet`` (``-q`` for short) keep indextool quiet - it will not
   output banner, etc.

The commands are as follows:

-  ``--checkconfig`` just loads and verifies the config file to check if
   it's valid, without syntax errors. This option was added in version
   2.1.1-beta.

-  ``--build-infixes INDEXNAME`` build infixes for an existing
   dict=keywords index (upgrades .sph, .spi in place). You can use this
   option for legacy index files that already use dict=keywords, but now
   need to support infix searching too; updating the index files with
   indextool may prove easier or faster than regenerating them from
   scratch with indexer. This option was added in version 2.1.1-beta.

-  ``--dumpheader FILENAME.sph`` quickly dumps the provided index header
   file without touching any other index files or even the configuration
   file. The report provides a breakdown of all the index settings, in
   particular the entire attribute and field list. Prior to 0.9.9-rc2,
   this command was present in now removed CLI search utility.

-  ``--dumpconfig FILENAME.sph`` dumps the index definition from the
   given index header file in (almost) compliant ``sphinx.conf`` file
   format. Added in version 2.0.1-beta.

-  ``--dumpheader INDEXNAME`` dumps index header by index name with
   looking up the header path in the configuration file.

-  ``--dumpdict INDEXNAME`` dumps dictionary. This was added in version
   2.1.1-beta.

-  ``--dumpdocids INDEXNAME`` dumps document IDs by index name. It takes
   the data from attribute (.spa) file and therefore requires
   docinfo=extern to work.

-  ``--dumphitlist INDEXNAME KEYWORD`` dumps all the hits (occurrences)
   of a given keyword in a given index, with keyword specified as text.

-  ``--dumphitlist INDEXNAME --wordid ID`` dumps all the hits
   (occurrences) of a given keyword in a given index, with keyword
   specified as internal numeric ID.

-  ``--fold INDEXNAME OPTFILE`` This options is useful too see how
   actually tokenizer proceeds input. You can feed indextool with text
   from file if specified or from stdin otherwise. The output will
   contain spaces instead of separators (accordingly to your
   charset\_table settings) and lowercased letters in words.

-  ``--htmlstrip INDEXNAME`` filters stdin using HTML stripper settings
   for a given index, and prints the filtering results to stdout. Note
   that the settings will be taken from sphinx.conf, and not the index
   header.

-  ``--morph INDEXNAME`` applies morphology to the given stdin and
   prints the result to stdout.

-  ``--check INDEXNAME`` checks the index data files for consistency
   errors that might be introduced either by bugs in ``indexer`` and/or
   hardware faults. Starting with version 2.1.1-beta, ``--check`` also
   works on RT indexes, RAM and disk chunks.

-  ``--strip-path`` strips the path names from all the file names
   referenced from the index (stopwords, wordforms, exceptions, etc).
   This is useful for checking indexes built on another machine with
   possibly different path layouts.

-  ``--optimize-rt-klists`` optimizes the kill list memory use in the
   disk chunk of a given RT index. That is a one-off optimization
   intended for rather old RT indexes, created by development versions
   prior to 1.10-beta release. As of 1.10-beta releases, this kill list
   optimization (purging) should happen automatically, and there should
   never be a need to use this option.

-  ``--rotate`` works only with ``--check`` and defines whether to check
   index waiting for rotation, i.e. with .new extension. This is useful
   when you want to check your index before actually using it.
