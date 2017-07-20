Sphinx plugins
--------------

Here's the complete plugin type list.

-  UDF plugins;

-  ranker plugins;

-  indexing-time token filter plugins;

-  query-time token filter plugins.

This section discusses writing and managing plugins in general; things
specific to writing this or that type of a plugin are then discussed in
their respective subsections.

So, how do you write and use a plugin? Four-line crash course goes as
follows:

-  create a dynamic library (either .so or.dll), most likely in C or
   C++;

-  load that plugin into searchd using `CREATE
   PLUGIN <../create_plugin_syntax.md>`__;

-  invoke it using the plugin specific calls (typically using this or
   that OPTION).

-  to unload or reload a plugin use `DROP
   PLUGIN <../drop_plugin_syntax.md>`__ and `RELOAD
   PLUGINS <../reload_plugins_syntax.md>`__ respectively.

Note that while UDFs are first-class plugins they are nevertheless
installed using a separate `CREATE
FUNCTION <../create_function_syntax.md>`__ statement. It lets you
specify the return type neatly so there was especially little reason to
ruin backwards compatibility *and* change the syntax.

Dynamic plugins are supported in `workers =
threads <../searchd_program_configuration_options/workers.md>`__ and
`workers =
thread\_pool <../searchd_program_configuration_options/workers.md>`__
mode only. Multiple plugins (and/or UDFs) may reside in a single library
file. So you might choose to either put all your project-specific
plugins in a single common uber-library; or you might choose to have a
separate library for every UDF and plugin; that is up to you.

Just as with UDFs, you want to include ``src/sphinxudf.h`` header file.
At the very least, you will need the SPH\_UDF\_VERSION constant to
implement a proper version function. Depending on the specific plugin
type, you might or might not need to link your plugin with
``src/sphinxudf.c``. However, all the functions implemented in
``sphinxudf.c`` are about unpacking the PACKEDFACTORS() blob, and no
plugin types are exposed to that kind of data. So currently, you would
never need to link with the C-file, just the header would be sufficient.
(In fact, if you copy over the UDF version number, then for some of the
plugin types you would not even need the header file.)

Formally, plugins are just sets of C functions that follow a certain
naming parttern. You are typically required to define just one key
function that does the most important work, but you may define a bunch
of other functions, too. For example, to implement a ranker called
“myrank”, you must define ``myrank_finalize()`` function that actually
returns the rank value, however, you might also define
``myrank_init()``, ``myrank_update()``, and ``myrank_deinit()``
functions. Specific sets of well-known suffixes and the call arguments
do differ based on the plugin type, but \_init() and \_deinit() are
generic, every plugin has those. Protip: for a quick reference on the
known suffixes and their argument types, refer to ``sphinxplugin.h``, we
define the call prototoypes in the very beginning of that file.

Despite having the public interface defined in ye good olde good pure C,
our plugins essentially follow the *object-oriented model*. Indeed,
every ``_init()`` function receives a ``void ** userdata``
out-parameter. And the pointer value that you store at ``(*userdata)``
location is then be passed as a 1st argument to all the other plugin
functions. So you can think of a plugin as *class* that gets
instantiated every time an object of that class is needed to handle a
request: the ``userdata`` pointer would be its ``this`` pointer; the
functions would be its methods, and the ``_init()`` and ``_deinit()``
functions would be the constructor and destructor respectively.

Why this (minor) OOP-in-C complication? Well, plugins run in a
multi-threaded environment, and some of them have to be stateful. You
can't keep that state in a global variable in your plugin. So we have to
pass around a userdata parameter anyway to let you keep that state. And
that naturally brings us to the OOP model. And if you've got a simple,
stateless plugin, the interface lets you omit the ``_init()`` and
``_deinit()`` and whatever other functions just as well.

To summarize, here goes the simplest complete ranker plugin, in just 3
lines of C code.

::


    // gcc -fPIC -shared -o myrank.so myrank.c
    #include "sphinxudf.h"
    int myrank_ver() { return SPH_UDF_VERSION; }
    int myrank_finalize(void *u, int w) { return 123; }

And this is how you use it:

::


    mysql> CREATE PLUGIN myrank TYPE 'ranker' SONAME 'myrank.dll';
    Query OK, 0 rows affected (0.00 sec)

    mysql> SELECT id, weight() FROM test1 WHERE MATCH('test')
        -> OPTION ranker=myrank('');
    +------+----------+
    | id   | weight() |
    +------+----------+
    |    1 |      123 |
    |    2 |      123 |
    +------+----------+
    2 rows in set (0.01 sec)

