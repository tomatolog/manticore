global\_idf
~~~~~~~~~~~

The path to a file with global (cluster-wide) keyword IDFs. Optional,
default is empty (use local IDFs). Added in 2.1.1-beta.

On a multi-index cluster, per-keyword frequencies are quite likely to
differ across different indexes. That means that when the ranking
function uses TF-IDF based values, such as BM25 family of factors, the
results might be ranked slightly different depending on what cluster
node they reside.

The easiest way to fix that issue is to create and utilize a global
frequency dictionary, or a global IDF file for short. This directive
lets you specify the location of that file. It it suggested (but not
required) to use a .idf extension. When the IDF file is specified for a
given index *and* and OPTION global\_idf is set to 1, the engine will
use the keyword frequencies and collection documents count from the
global\_idf file, rather than just the local index. That way, IDFs and
the values that depend on them will stay consistent across the cluster.

IDF files can be shared across multiple indexes. Only a single copy of
an IDF file will be loaded by ``searchd``, even when many indexes refer
to that file. Should the contents of an IDF file change, the new
contents can be loaded with a SIGHUP.

You can build an .idf file using ``indextool`` utility, by dumping
dictionaries using ``--dumpdict`` switch first, then converting those to
.idf format using ``--buildidf``, then merging all .idf files across
cluser using ``--mergeidf``. Refer to `the section called “``indextool``
command reference” <../../indextool_command_reference.md>`__ for more
information.

Example:
^^^^^^^^

::


    global_idf = /usr/local/sphinx/var/global.idf

