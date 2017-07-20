blend\_mode
~~~~~~~~~~~

Blended tokens indexing mode. Optional, default is ``trim_none``.

By default, tokens that mix blended and non-blended characters get
indexed in there entirety. For instance, when both at-sign and an
exclamation are in ``blend_chars``, “@dude!” will get result in two
tokens indexed: “@dude!” (with all the blended characters) and “dude”
(without any). Therefore “@dude&quot; query will *not* match it.

``blend_mode`` directive adds flexibility to this indexing behavior. It
takes a comma-separated list of options.

::


    blend_mode = option [, option [, ...]]
    option = trim_none | trim_head | trim_tail | trim_both | skip_pure

Options specify token indexing variants. If multiple options are
specified, multiple variants of the same token will be indexed. Regular
keywords (resulting from that token by replacing blended with
whitespace) are always be indexed.

-  trim\_none
-  Index the entire token.

-  trim\_head
-  Trim heading blended characters, and index the resulting token.

-  trim\_tail
-  Trim trailing blended characters, and index the resulting token.

-  trim\_both
-  Trim both heading and trailing blended characters, and index the
   resulting token.

-  skip\_pure
-  Do not index the token if it's purely blended, that is, consists of
   blended characters only.

Returning to the “@dude!” example above, setting
``blend_mode = trim_head, trim_tail`` will result in two tokens being
indexed, “@dude&quot; and”dude!“. In this particular example,
``trim_both`` would have no effect, because trimming both blended
characters results in”dude" which is already indexed as a regular
keyword. Indexing “@U.S.A.” with ``trim_both`` (and assuming that dot is
blended two) would result in “U.S.A” being indexed. Last but not least,
``skip_pure`` enables you to fully ignore sequences of blended
characters only. For example, “one @@@ two” would be indexed exactly as
“one two”, and match that as a phrase. That is not the case by default
because a fully blended token gets indexed and offsets the second
keyword position.

Default behavior is to index the entire token, equivalent to
``blend_mode = trim_none``.

Example:
^^^^^^^^

::


    blend_mode = trim_tail, skip_pure

