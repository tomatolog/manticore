ondisk\_attrs\_default
~~~~~~~~~~~~~~~~~~~~~~

Instance-wide defaults for
`ondisk\_attrs <../../index_configuration_options/ondiskattrs.rst>`__
directive. Optional, default is 0 (all attributes are loaded in memory).
This directive lets you specify the default value of ondisk\_attrs for
all indexes served by this copy of searchd. Per-index directives take
precedence, and will overwrite this instance-wide default value,
allowing for fine-grain control.
