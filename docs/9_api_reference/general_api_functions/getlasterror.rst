GetLastError
~~~~~~~~~~~~

<b>Prototype:</b> function GetLastError()

Returns last error message, as a string, in human readable format. If
there were no errors during the previous API call, empty string is
returned.

You should call it when any other function (such as
`Query() <../../querying/query.html>`__) fails (typically, the failing
function returns false). The returned string will contain the error
description.

The error message is *not* reset by this call; so you can safely call it
several times if needed.
