Version 2.3.1-beta, 03 mar 2015
-------------------------------

Major features
~~~~~~~~~~~~~~

-  added `query cache <../query_cache.html>`__

-  added thread pool mode, and the respective `workers =
   thread\_pool <../searchd_program_configuration_options/workers.html>`__,
   `max\_children <../searchd_program_configuration_options/maxchildren.html>`__,
   `net\_workers <../searchd_program_configuration_options/networkers.html>`__,
   `queue\_max\_length <../searchd_program_configuration_options/queuemax_length.html>`__
   directives

-  added vip suffixes to
   `listener <../searchd_program_configuration_options/listen.html>`__
   protocols (sphinx\_vip, mysql41\_vip)

Removals
~~~~~~~~

-  removed fork and prefork modes

-  removed ``prefork_rotation_throttle`` directive

Minor features
~~~~~~~~~~~~~~

-  added `RELOAD PLUGINS <../reload_plugins_syntax.html>`__ SphinxQL
   statement

-  added `FLUSH ATTRIBUTES <../flush_attributes_syntax.html>`__ SphinxQL
   statement

Bug fixes
~~~~~~~~~

-  fixed #2167, ``--keep_attrs`` did not work with ``--rotate``

-  fixed #2161, RT indexing could fail with ``index_token_filter``
   because of multiple errorneous filter loads

-  fixed #2154, crash in ``ZONE`` operator
