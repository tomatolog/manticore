ResetGroupBy
~~~~~~~~~~~~

<b>Prototype:</b> function ResetGroupBy ()

Clears all currently group-by settings, and disables group-by.

This call is only normally required when using multi-queries. You can
change individual group-by settings using ``SetGroupBy()`` and
``SetGroupDistinct()`` calls, but you can not disable group-by using
those calls. ``ResetGroupBy()`` fully resets previous group-by settings
and disables group-by mode in the current state, so that subsequent
``AddQuery()`` calls can perform non-grouping searches.
