### GetLastError {#getlasterror}

&lt;b&gt;Prototype:&lt;/b&gt; function GetLastError()

Returns last error message, as a string, in human readable format. If there were no errors during the previous API call, empty string is returned.

You should call it when any other function (such as [Query()](../../querying/query.md)) fails (typically, the failing function returns false). The returned string will contain the error description.

The error message is _not_ reset by this call; so you can safely call it several times if needed.