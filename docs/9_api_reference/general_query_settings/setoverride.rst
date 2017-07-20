SetOverride
~~~~~~~~~~~

<b>DEPRECATED</b>

<b>Prototype:</b> function SetOverride ( $attrname, $attrtype, $values )

Sets temporary (per-query) per-document attribute value overrides. Only
supports scalar attributes. $values must be a hash that maps document
IDs to overridden attribute values.

Override feature lets you “temporary” update attribute values for some
documents within a single query, leaving all other queries unaffected.
This might be useful for personalized data. For example, assume you're
implementing a personalized search function that wants to boost the
posts that the user's friends recommend. Such data is not just dynamic,
but also personal; so you can't simply put it in the index because you
don't want everyone's searches affected. Overrides, on the other hand,
are local to a single query and invisible to everyone else. So you can,
say, setup a “friends\_weight” value for every document, defaulting to
0, then temporary override it with 1 for documents 123, 456 and 789
(recommended by exactly the friends of current user), and use that value
when ranking.
