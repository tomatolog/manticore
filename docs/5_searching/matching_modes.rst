Matching modes
--------------

So-called matching modes are a legacy feature that used to provide
(very) limited query syntax and ranking support. Currently, they are
deprecated in favor of `full-text query
language <../extended_query_syntax.md>`__ and so-called
`rankers <../search_results_ranking/README.md>`__. It is thus strongly
recommended to use SPH\_MATCH\_EXTENDED and proper query syntax rather
than any other legacy mode. All those other modes are actually
internally converted to extended syntax anyway. ManticoreAPI still defaults
to SPH\_MATCH\_ALL but that is for compatibility reasons only.

There are the following matching modes available:

-  SPH\_MATCH\_ALL, matches all query words;

-  SPH\_MATCH\_ANY, matches any of the query words;

-  SPH\_MATCH\_PHRASE, matches query as a phrase, requiring perfect
   match;

-  SPH\_MATCH\_BOOLEAN, matches query as a boolean expression (see `the
   section called “Boolean query
   syntax” <../boolean_query_syntax.md>`__);

-  SPH\_MATCH\_EXTENDED, matches query as an expression in Manticore
   internal query language (see `the section called “Extended query
   syntax” <../extended_query_syntax.md>`__);

-  SPH\_MATCH\_EXTENDED2, an alias for SPH\_MATCH\_EXTENDED (default
   mode);

-  SPH\_MATCH\_FULLSCAN, matches query, forcibly using the “full scan”
   mode as below. NB, any query terms will be ignored, such that
   filters, filter-ranges and grouping will still be applied, but no
   text-matching.

The SPH\_MATCH\_FULLSCAN mode will be automatically activated in place
of the specified matching mode when the following conditions are met:

1. The query string is empty (ie. its length is zero).

2. `docinfo <../index_configuration_options/docinfo.md>`__ storage is
   set to ``extern``.

In full scan mode, all the indexed documents will be considered as
matching. Such queries will still apply filters, sorting, and group by,
but will not perform any full-text searching. This can be useful to
unify full-text and non-full-text searching code, or to offload SQL
server (there are cases when Manticore scans will perform better than
analogous MySQL queries). An example of using the full scan mode might
be to find posts in a forum. By selecting the forum's user ID via
``SetFilter()`` but not actually providing any search text, Manticore will
match every document (i.e. every post) where ``SetFilter()`` would match
- in this case providing every post from that user. By default this will
be ordered by relevancy, followed by Manticore document ID in ascending
order (earliest first).
