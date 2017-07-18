on\_json\_attr\_error
~~~~~~~~~~~~~~~~~~~~~

What to do if JSON format errors are found. Optional, default value is
``ignore_attr`` (ignore errors). Applies only to ``sql_attr_json``
attributes. Added in 2.1.1-beta.

By default, JSON format errors are ignored (``ignore_attr``) and the
indexer tool will just show a warning. Setting this option to
``fail_index`` will rather make indexing fail at the first JSON format
error.

Example:
^^^^^^^^

::


    on_json_attr_error = ignore_attr

