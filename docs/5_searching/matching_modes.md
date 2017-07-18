## Matching modes {#matching-modes}

So-called matching modes are a legacy feature that used to provide (very) limited query syntax and ranking support. Currently, they are deprecated in favor of [full-text query language](../extended_query_syntax.md) and so-called [rankers](../search_results_ranking/README.md). Starting with version 0.9.9-release, it is thus strongly recommended to use SPH_MATCH_EXTENDED and proper query syntax rather than any other legacy mode. All those other modes are actually internally converted to extended syntax anyway. SphinxAPI still defaults to SPH_MATCH_ALL but that is for compatibility reasons only.

There are the following matching modes available:

*   SPH_MATCH_ALL, matches all query words;

*   SPH_MATCH_ANY, matches any of the query words;

*   SPH_MATCH_PHRASE, matches query as a phrase, requiring perfect match;

*   SPH_MATCH_BOOLEAN, matches query as a boolean expression (see [the section called “Boolean query syntax”](../boolean_query_syntax.md));

*   SPH_MATCH_EXTENDED, matches query as an expression in Sphinx internal query language (see [the section called “Extended query syntax”](../extended_query_syntax.md));

*   SPH_MATCH_EXTENDED2, an alias for SPH_MATCH_EXTENDED (default mode);

*   SPH_MATCH_FULLSCAN, matches query, forcibly using the &quot;full scan&quot; mode as below. NB, any query terms will be ignored, such that filters, filter-ranges and grouping will still be applied, but no text-matching.

SPH_MATCH_EXTENDED2 was used during 0.9.8 and 0.9.9 development cycle, when the internal matching engine was being rewritten (for the sake of additional functionality and better performance). By 0.9.9-release, the older version was removed, and SPH_MATCH_EXTENDED and SPH_MATCH_EXTENDED2 are now just aliases.

The SPH_MATCH_FULLSCAN mode will be automatically activated in place of the specified matching mode when the following conditions are met:

1.  The query string is empty (ie. its length is zero).

2.  [docinfo](../index_configuration_options/docinfo.md) storage is set to `extern`.

In full scan mode, all the indexed documents will be considered as matching. Such queries will still apply filters, sorting, and group by, but will not perform any full-text searching. This can be useful to unify full-text and non-full-text searching code, or to offload SQL server (there are cases when Sphinx scans will perform better than analogous MySQL queries). An example of using the full scan mode might be to find posts in a forum. By selecting the forum&#039;s user ID via `SetFilter()` but not actually providing any search text, Sphinx will match every document (i.e. every post) where `SetFilter()` would match - in this case providing every post from that user. By default this will be ordered by relevancy, followed by Sphinx document ID in ascending order (earliest first).