ResetFilters
~~~~~~~~~~~~

<b>Prototype:</b> function ResetFilters ()

Clears all currently set filters.

This call is only normally required when using multi-queries. You might
want to set different filters for different queries in the batch. To do
that, you should call ``ResetFilters()`` and add new filters using the
respective calls.
