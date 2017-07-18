## Sphinx deprecations and changes in default configuration {#sphinx-deprecations-and-changes-in-default-configuration}

In 2.2.1-beta version we decided to start removing some old features. All of them was &#039;unofficially&#039; deprecated for some time. And we&#039;re informing you now about it.

Changes are as follows:

*   32-bit document IDs are now deprecated. Our binary releases are now all built with 64-bit IDs by default. Note that they can still load older indexes with 32-bit IDs, but that support will eventually be removed. In fact, that was deprecated awhile ago, but now we just want to make it clear: we don&#039;t see any sense in trying to save your server&#039;s RAM this way.

*   dict=crc is now deprecated. It has a bunch of limitations, the most important ones being keyword collisions, and no (good) wildcard matching support. You can read more about those limitations in our documentation.

*   charset_type=sbcs is now deprecated, we&#039;re slowly switching to UTF-only. Even if your database is SBCS (likely for legacy reasons too, eh?), this should be absolutely trivial to workaround, just add a pre-query to fetch your data in UTF-8 and you&#039;re all set. Also, in fact, our current UTF-8 tokenizer is even faster than the SBCS one.

*   custom sort (@custom) is now removed from Sphinx. This feature was introduced long before sort by expression became a reality and it has been deprecated for a very long time.

*   enable_star is deprecated now. Previous default mode was enable_star=0 which was due to compatibility with a very old Sphinx version. Such implicit star search isn&#039;t very intuitive. So, we&#039;ve decided to eventually remove it and have marked it as deprecated just recently. We plan to totally remove this configuration key in the 2.2.X branch.

*   str2ordinal attributes are deprecated. This feature allows you to perform sorting by a string. But it&#039;s also possible to do this with ordinary string attributes, which is much easier to use. str2ordinal only covers a small part of this functionality and is not needed now.

*   str2wordcount attributes are deprecated. [index_field_lengths=1](../index_configuration_options/indexfield_lengths.md) will create an integer attribute with field length set automatically and we recommend to use this configuration key when you need to store field lengths. Also, index_field_lengths=1 allows you to use new ranking formulas like BM25F().

*   hit_format is deprecated. This is a hidden configuration key - it&#039;s not mentioned in our documentation. But, it&#039;s there and it&#039;s possible that someone may use it. And now we&#039;re urging you: don&#039;t use it. The default value is &#039;inline&#039; and it&#039;s a new standard. &#039;plain&#039; hit_format is obsolete and will be removed in the near future.

*   docinfo=inline is deprecated. You can now use [ondisk_attrs](../index_configuration_options/ondiskattrs.md) or [ondisk_attrs_default](../searchd_program_configuration_options/ondiskattrs_default.md) instead.

*   workers=threads is a new default for all OS now. We&#039;re gonna get rid of other modes in future.

*   mem_limit=128M is a new default.

*   rt_mem_limit=128M is a new default.

*   ondisk_dict is deprecated. No need to save RAM this way.

*   ondisk_dict_default is deprecated. No need to save RAM this way.

*   compat_sphinxql_magics was removed. Now you can&#039;t use an old result format and SphinxQL always looks more like ANSI SQL.

*   Completely removed xmlpipe. This was a very old ad hoc solution for a particular customer. xmlpipe2 surpasses it in every single aspect.

None of the different querying methods are deprecated, but as of version 2.2.1-beta, SphinxQL is the most advanced method. We plan to remove SphinxAPI and Sphinx SE someday so it would be a good idea to start using SphinxQL.

*   The SetWeights() API call has been deprecated for a long time and has now been removed from official APIs.

*   The default matching mode for the API is now &#039;extended&#039;. Actually, all other modes are deprecated. We recommend using the [extended query syntax](../extended_query_syntax.md) instead.

Changes for 2.2.2-beta:

*   Removed deprecated &quot;address&quot; and &quot;port&quot; directives. Use &quot;listen&quot; instead.

*   Removed str2wordcount attributes. Use [index_field_lengths=1](../index_configuration_options/indexfield_lengths.md) instead.

*   Removed str2ordinal attributes. Use string attributes for sorting.

*   ondisk_dict and ondisk_dict_default was removed.

*   Removed charset_type and mssql_unicode - we now support only UTF-8 encoding.

*   Removed deprecated enable_star. Now always work as with enable_star=1.

*   Removed CLI search which confused people instead of helping them and sql_query_info.

*   Deprecated SetMatchMode() API call.

*   Changed default [thread_stack](../searchd_program_configuration_options/threadstack.md) value to 1M.

*   Deprecated SetOverride() API call.

Changes for 2.2.3-beta:

*   Removed unneeded max_matches key from config file.