### IsConnectError {#isconnecterror}

&lt;b&gt;Prototype:&lt;/b&gt; function IsConnectError ()

Checks whether the last error was a network error on API side, or a remote error reported by searchd. Returns true if the last connection attempt to searchd failed on API side, false otherwise (if the error was remote, or there were no connection attempts at all). Introduced in version 0.9.9-rc1.