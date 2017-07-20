Chapter 8. ManticoreQL reference
=============================

ManticoreQL is our SQL dialect that exposes all of the search daemon
functionality using a standard SQL syntax with a few Manticore-specific
extensions. Everything available via the ManticoreAPI is also available via
ManticoreQL but not vice versa; for instance, writes into RT indexes are
only available via ManticoreQL. This chapter documents supported ManticoreQL
statements syntax.

.. toctree::
   :glob:

   8_sphinxql_reference/*