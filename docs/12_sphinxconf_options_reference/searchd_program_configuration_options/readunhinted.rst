read\_unhinted
~~~~~~~~~~~~~~

Unhinted read size. Optional, default is 32K.

When querying, some reads know in advance exactly how much data is there
to be read, but some currently do not. Most prominently, hit list size
in not currently known in advance. This setting lest you control how
much data to read in such cases. It will impact hit list IO time,
reducing it for lists larger than unhinted read size, but raising it for
smaller lists. It will <b>not</b> affect RAM use because read buffer
will be already allocated. So it should be not greater than
read\_buffer.

Example:
^^^^^^^^

::


    read_unhinted = 32K

