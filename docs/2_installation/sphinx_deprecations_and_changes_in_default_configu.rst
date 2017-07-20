Manticore deprecations and changes in default configuration
--------------------------------------------------------

Changes are as follows:

-  32-bit document IDs are now deprecated. Our binary releases are now
   all built with 64-bit IDs by default. Note that they can still load
   older indexes with 32-bit IDs, but that support will eventually be
   removed. In fact, that was deprecated awhile ago, but now we just
   want to make it clear: we don't see any sense in trying to save your
   server's RAM this way.

-  dict=crc is now deprecated. It has a bunch of limitations, the most
   important ones being keyword collisions, and no (good) wildcard
   matching support. You can read more about those limitations in our
   documentation.

-  charset\_type=sbcs is now deprecated, we're slowly switching to
   UTF-only. Even if your database is SBCS (likely for legacy reasons
   too, eh?), this should be absolutely trivial to workaround, just add
   a pre-query to fetch your data in UTF-8 and you're all set. Also, in
   fact, our current UTF-8 tokenizer is even faster than the SBCS one.

-  custom sort (@custom) is now removed from Manticore. This feature was
   introduced long before sort by expression became a reality and it has
   been deprecated for a very long time.

-  hit\_format is deprecated. This is a hidden configuration key - it's
   not mentioned in our documentation. But, it's there and it's possible
   that someone may use it. And now we're urging you: don't use it. The
   default value is ‘inline’ and it's a new standard. ‘plain’
   hit\_format is obsolete and will be removed in the near future.

-  docinfo=inline is deprecated. You can now use
   `ondisk\_attrs <../index_configuration_options/ondiskattrs.md>`__ or
   `ondisk\_attrs\_default <../searchd_program_configuration_options/ondiskattrs_default.md>`__
   instead.

-  workers=threads is a new default for all OS now. We're gonna get rid
   of other modes in future.

-  mem\_limit=128M is a new default.

-  rt\_mem\_limit=128M is a new default.

-  ondisk\_dict is deprecated. No need to save RAM this way.

-  ondisk\_dict\_default is deprecated. No need to save RAM this way.

None of the different querying methods are deprecated, but SphinxQL is
the most advanced method. We plan to remove ManticoreAPI and Manticore SE
someday so it would be a good idea to start using SphinxQL.

-  The SetWeights() API call has been deprecated for a long time and has
   now been removed from official APIs.

-  The default matching mode for the API is now ‘extended’. Actually,
   all other modes are deprecated. We recommend using the `extended
   query syntax <../extended_query_syntax.md>`__ instead.
