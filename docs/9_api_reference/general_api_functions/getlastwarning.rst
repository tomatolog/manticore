GetLastWarning
~~~~~~~~~~~~~~

<b>Prototype:</b> function GetLastWarning ()

Returns last warning message, as a string, in human readable format. If
there were no warnings during the previous API call, empty string is
returned.

You should call it to verify whether your request (such as
`Query() <../../querying/query.md>`__) was completed but with warnings.
For instance, search query against a distributed index might complete
successfully even if several remote agents timed out. In that case, a
warning message would be produced.

The warning message is *not* reset by this call; so you can safely call
it several times if needed.
