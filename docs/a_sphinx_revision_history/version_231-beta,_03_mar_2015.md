## Version 2.3.1-beta, 03 mar 2015 {#version-2-3-1-beta-03-mar-2015}

### Major features {#major-features}

*   added [query cache](../query_cache.md)

*   added thread pool mode, and the respective [workers = thread_pool](../searchd_program_configuration_options/workers.md), [max_children](../searchd_program_configuration_options/maxchildren.md), [net_workers](../searchd_program_configuration_options/networkers.md), [queue_max_length](../searchd_program_configuration_options/queuemax_length.md) directives

*   added vip suffixes to [listener](../searchd_program_configuration_options/listen.md) protocols (sphinx_vip, mysql41_vip)

### Removals {#removals}

*   removed fork and prefork modes

*   removed `prefork_rotation_throttle` directive

### Minor features {#minor-features}

*   added [RELOAD PLUGINS](../reload_plugins_syntax.md) SphinxQL statement

*   added [FLUSH ATTRIBUTES](../flush_attributes_syntax.md) SphinxQL statement

### Bug fixes {#bug-fixes}

*   fixed #2167, `--keep_attrs` did not work with `--rotate`

*   fixed #2161, RT indexing could fail with `index_token_filter` because of multiple errorneous filter loads

*   fixed #2154, crash in `ZONE` operator