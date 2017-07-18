.. raw:: html

   <div class="navheader">

2.6. Sphinx deprecations and changes in default configuration
`Prev <installing-windows.html>`__ 
Chapter 2. Installation
 `Next <quick-tour.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 2.6. Sphinx deprecations and changes in default
   configuration
   :name: sphinx-deprecations-and-changes-in-default-configuration
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

In 2.2.1-beta version we decided to start removing some old features.
All of them was ‘unofficially’ deprecated for some time. And we’re
informing you now about it.

Changes are as follows:

.. raw:: html

   <div class="itemizedlist">

-  32-bit document IDs are now deprecated. Our binary releases are now
   all built with 64-bit IDs by default. Note that they can still load
   older indexes with 32-bit IDs, but that support will eventually be
   removed. In fact, that was deprecated awhile ago, but now we just
   want to make it clear: we don’t see any sense in trying to save your
   server’s RAM this way.

-  dict=crc is now deprecated. It has a bunch of limitations, the most
   important ones being keyword collisions, and no (good) wildcard
   matching support. You can read more about those limitations in our
   documentation.

-  charset\_type=sbcs is now deprecated, we’re slowly switching to
   UTF-only. Even if your database is SBCS (likely for legacy reasons
   too, eh?), this should be absolutely trivial to workaround, just add
   a pre-query to fetch your data in UTF-8 and you’re all set. Also, in
   fact, our current UTF-8 tokenizer is even faster than the SBCS one.

-  custom sort (@custom) is now removed from Sphinx. This feature was
   introduced long before sort by expression became a reality and it has
   been deprecated for a very long time.

-  enable\_star is deprecated now. Previous default mode was
   enable\_star=0 which was due to compatibility with a very old Sphinx
   version. Such implicit star search isn’t very intuitive. So, we’ve
   decided to eventually remove it and have marked it as deprecated just
   recently. We plan to totally remove this configuration key in the
   2.2.X branch.

-  str2ordinal attributes are deprecated. This feature allows you to
   perform sorting by a string. But it’s also possible to do this with
   ordinary string attributes, which is much easier to use. str2ordinal
   only covers a small part of this functionality and is not needed now.

-  str2wordcount attributes are deprecated.
   `index\_field\_lengths=1 <conf-index-field-lengths.html>`__ will
   create an integer attribute with field length set automatically and
   we recommend to use this configuration key when you need to store
   field lengths. Also, index\_field\_lengths=1 allows you to use new
   ranking formulas like BM25F().

-  hit\_format is deprecated. This is a hidden configuration key - it’s
   not mentioned in our documentation. But, it’s there and it’s possible
   that someone may use it. And now we’re urging you: don’t use it. The
   default value is ‘inline’ and it’s a new standard. ‘plain’
   hit\_format is obsolete and will be removed in the near future.

-  docinfo=inline is deprecated. You can now use
   `ondisk\_attrs <conf-ondisk-attrs.html>`__ or
   `ondisk\_attrs\_default <conf-ondisk-attrs-default.html>`__ instead.

-  workers=threads is a new default for all OS now. We’re gonna get rid
   of other modes in future.

-  mem\_limit=128M is a new default.

-  rt\_mem\_limit=128M is a new default.

-  ondisk\_dict is deprecated. No need to save RAM this way.

-  ondisk\_dict\_default is deprecated. No need to save RAM this way.

-  compat\_sphinxql\_magics was removed. Now you can’t use an old result
   format and SphinxQL always looks more like ANSI SQL.

-  Completely removed xmlpipe. This was a very old ad hoc solution for a
   particular customer. xmlpipe2 surpasses it in every single aspect.

.. raw:: html

   </div>

None of the different querying methods are deprecated, but as of version
2.2.1-beta, SphinxQL is the most advanced method. We plan to remove
SphinxAPI and Sphinx SE someday so it would be a good idea to start
using SphinxQL.

.. raw:: html

   <div class="itemizedlist">

-  The SetWeights() API call has been deprecated for a long time and has
   now been removed from official APIs.

-  The default matching mode for the API is now ‘extended’. Actually,
   all other modes are deprecated. We recommend using the `extended
   query syntax <extended-syntax.html>`__ instead.

.. raw:: html

   </div>

Changes for 2.2.2-beta:

.. raw:: html

   <div class="itemizedlist">

-  Removed deprecated “address” and “port” directives. Use “listen”
   instead.

-  Removed str2wordcount attributes. Use
   `index\_field\_lengths=1 <conf-index-field-lengths.html>`__ instead.

-  Removed str2ordinal attributes. Use string attributes for sorting.

-  ondisk\_dict and ondisk\_dict\_default was removed.

-  Removed charset\_type and mssql\_unicode - we now support only UTF-8
   encoding.

-  Removed deprecated enable\_star. Now always work as with
   enable\_star=1.

-  Removed CLI search which confused people instead of helping them and
   sql\_query\_info.

-  Deprecated SetMatchMode() API call.

-  Changed default `thread\_stack <conf-thread-stack.html>`__ value to
   1M.

-  Deprecated SetOverride() API call.

.. raw:: html

   </div>

Changes for 2.2.3-beta:

.. raw:: html

   <div class="itemizedlist">

-  Removed unneeded max\_matches key from config file.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+---------------------------------------+------------------------------+---------------------------------+
| `Prev <installing-windows.html>`__    | `Up <installation.html>`__   |  `Next <quick-tour.html>`__     |
+---------------------------------------+------------------------------+---------------------------------+
| 2.5. Installing Sphinx on Windows     | `Home <index.html>`__        |  2.7. Quick Sphinx usage tour   |
+---------------------------------------+------------------------------+---------------------------------+

.. raw:: html

   </div>
