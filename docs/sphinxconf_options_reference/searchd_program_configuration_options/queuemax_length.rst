queue\_max\_length
~~~~~~~~~~~~~~~~~~

Maximum pending queries queue length for workers=thread\_pool mode,
default is 0 (unlimited).

In case of high CPU load thread pool queries queue may grow all the
time. This directive lets you constrain queue length and start rejecting
incoming queries at some point with a “maxed out” message.
