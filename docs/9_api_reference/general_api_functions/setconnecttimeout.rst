SetConnectTimeout
~~~~~~~~~~~~~~~~~

<b>Prototype:</b> function SetConnectTimeout ( $timeout )

Sets the time allowed to spend connecting to the server before giving
up.

Under some circumstances, the server can be delayed in responding,
either due to network delays, or a query backlog. In either instance,
this allows the client application programmer some degree of control
over how their program interacts with ``searchd`` when not available,
and can ensure that the client application does not fail due to
exceeding the script execution limits (especially in PHP).

In the event of a failure to connect, an appropriate error code should
be returned back to the application in order for application-level error
handling to advise the user.
