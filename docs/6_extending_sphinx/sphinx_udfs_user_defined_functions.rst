Manticore UDFs (User Defined Functions)
------------------------------------

Our expression engine can be extended with user defined functions, or
UDFs for short, like this:

::


    SELECT id, attr1, myudf(attr2, attr3+attr4) ...

You can load and unload UDFs dynamically into ``searchd`` without having
to restart the daemon, and used them in expressions when searching,
ranking, etc. Quick summary of the UDF features is as follows.

-  UDFs can take integer (both 32-bit and 64-bit), float, string, MVA,
   or PACKEDFACTORS() arguments.

-  UDFs can return integer, float, or string values.

-  UDFs can check the argument number, types, and names during the query
   setup phase, and raise errors.

-  Aggregation UDFs are not yet supported (but might be in the future).

UDFs have a wide variety of uses, for instance:

-  adding custom mathematical or string functions;

-  accessing the database or files from within Manticore;

-  implementing complex ranking functions.

UDFs reside in the external dynamic libraries (.so files on UNIX and
.dll on Windows systems). Library files need to reside in a trusted
folder specified by
`plugin\_dir <../common_section_configuration_options/plugindir.md>`__
directive, for obvious security reasons: securing a single folder is
easy; letting anyone install arbitrary code into ``searchd`` is a risk.
You can load and unload them dynamically into searchd with `CREATE
FUNCTION <../create_function_syntax.md>`__ and `DROP
FUNCTION <../drop_function_syntax.md>`__ ManticoreQL statements
respectively. Also, you can seamlessly reload UDFs (and other plugins)
with `RELOAD PLUGINS <../reload_plugins_syntax.md>`__ statement. Manticore
keeps track of the currently loaded functions, that is, every time you
create or drop an UDF, ``searchd`` writes its state to the
`sphinxql\_state <../searchd_program_configuration_options/sphinxqlstate.md>`__
file as a plain good old SQL script.

Once you successfully load an UDF, you can use it in your SELECT or
other statements just as well as any of the builtin functions:

::


    SELECT id, MYCUSTOMFUNC(groupid, authorname), ... FROM myindex

Multiple UDFs (and other plugins) may reside in a single library. That
library will only be loaded once. It gets automatically unloaded once
all the UDFs and plugins from it are dropped.

In theory you can write an UDF in any language as long as its compiler
is able to import standard C header, and emit standard dynamic libraries
with properly exported functions. Of course, the path of least
resistance is to write in either C++ or plain C. We provide an example
UDF library written in plain C and implementing several functions
(demonstrating a few different techniques) along with our source code,
see
`src/udfexample.c <https://github.com/sphinxsearch/sphinx/blob/master/src/udfexample.c>`__.
That example includes
`src/sphinxudf.h <https://github.com/sphinxsearch/sphinx/blob/master/src/sphinxudf.h>`__
header file definitions of a few UDF related structures and types. For
most UDFs and plugins, a mere ``#include &quot;sphinxudf.h&quot;``, like
in the example, should be completely sufficient, too. However, if you're
writing a ranking function and need to access the ranking signals
(factors) data from within the UDF, you will also need to compile and
link with ``src/sphinxudf.c`` (also available in our source code),
because the *implementations* of the fuctions that let you access the
signal data from within the UDF reside in that file.

Both ``sphinxudf.h`` header and ``sphinxudf.c`` are standalone. So you
can copy around those files only; they do not depend on any other bits
of Manticore source code.

Within your UDF, you <b>must</b> implement and export only a couple
functions, literally. First, for UDF interface version control, you
<b>must</b> define a function ``int LIBRARYNAME_ver()``, where
LIBRARYNAME is the name of your library file, and you must return
``SPH_UDF_VERSION`` (a value defined in ``sphinxudf.h``) from it. Here's
an example.

::


    #include <sphinxudf.h>

    // our library will be called udfexample.so, thus, so it must define
    // a version function named udfexample_ver()
    int udfexample_ver()
    {
        return SPH_UDF_VERSION;
    }

That protects you from accidentally loading a library with a mismatching
UDF interface version into a newer or older ``searchd``. Second, yout
<b>must</b> implement the actual function, too.
``sphinx_int64_t testfunc ( SPH_UDF_INIT * init, SPH_UDF_ARGS * args, char * error_flag ) { return 123; }``

UDF function names in ManticoreQL are case insensitive. However, the
respective C function names are not, they need to be all
<b>lower-case</b>, or the UDF will not load. More importantly, it is
vital that a) the calling convention is C (aka \_\_cdecl), b) arguments
list matches the plugin system expectations exactly, and c) the return
type matches the one you specify in ``CREATE FUNCTION``. Unfortunately,
there is no (easy) way for us to check for those mistakes when loading
the function, and they could crash the server and/or result in
unexpected results. Last but not least, all the C functions you
implement need to be thread-safe.

The first argument, a pointer to SPH\_UDF\_INIT structure, is
essentially a pointer to our function state. It is option. In the
example just above the function is stateless, it simply returns 123
every time it gets called. So we do not have to define an initialization
function, and we can simply ignore that argument.

The second argument, a pointer to SPH\_UDF\_ARGS, is the most important
one. All the actual call arguments are passed to your UDF via this
structure; it contians the call argument count, names, types, etc. So
whether your function gets called like ``SELECT id, testfunc(1)`` or
like ``SELECT id, testfunc(&#039;abc&#039;, 1000*id+gid, WEIGHT())`` or
anyhow else, it will receive the very same SPH\_UDF\_ARGS structure in
all of these cases. However, the data passed in the ``args`` structure
will be different. In the first example ``args-&gt;arg_count`` will be
set to 1, in the second example it will be set to 3,
``args-&gt;arg_types`` array will contain different type data, and so
on.

Finally, the third argument is an error flag. UDF can raise it to
indicate that some kinda of an internal error happened, the UDF can not
continue, and the query should terminate early. You should <b>not</b>
use this for argument type checks or for any other error reporting that
is likely to happen during normal use. This flag is designed to report
sudden critical runtime errors, such as running out of memory.

If we wanted to, say, allocate temporary storage for our function to
use, or check upfront whether the arguments are of the supported types,
then we would need to add two more functions, with UDF initialization
and deinitialization, respectively.

::


    int testfunc_init ( SPH_UDF_INIT * init, SPH_UDF_ARGS * args,
        char * error_message )
    {
        // allocate and initialize a little bit of temporary storage
        init->func_data = malloc ( sizeof(int) );
        *(int*)init->func_data = 123;

        // return a success code
        return 0;
    }

    void testfunc_deinit ( SPH_UDF_INIT * init )
    {
        // free up our temporary storage
        free ( init->func_data );
    }

Note how ``testfunc_init()`` also receives the call arguments structure.
By the time it is called it does not receive any actual values, so the
``args-&gt;arg_values`` will be NULL. But the argument names and types
are known and will be passed. You can check them in the initialization
function and return an error if they are of an unsupported type.

UDFs can receive arguments of pretty much any valid internal Manticore
type. Refer to ``sphinx_udf_argtype`` enumeration in ``sphinxudf.h`` for
a full list. Most of the types map straightforwardly to the respective C
types. The most notable exception is the SPH\_UDF\_TYPE\_FACTORS
argument type. You get that type by calling your UDF with a
`PACKEDFACTOR() <../5_searching/expressions,_functions,_and_operators/miscellaneous_functions.md#expr-func-packedfactors>`__
argument. It's data is a binary blob in a certain internal format, and
to extract individual ranking signals from that blob, you need to use
either of the two ``sphinx_factors_XXX()`` or
``sphinx_get_YYY_factor()`` families of functions. The first family
consists of just 3 functions, ``sphinx_factors_init()`` that initializes
the unpacked SPH\_UDF\_FACTORS structure, ``sphinx_factors_unpack()``
that unpacks a binary blob into it, and ``sphinx_factors_deinit()`` that
cleans up an deallocates the SPH\_UDF\_FACTORS. So you need to call
init() and unpack(), then you can use the SPH\_UDF\_FACTORS fields, and
then you need to cleanup with deinit(). That is simple, but results in a
bunch of memory allocations per each processed document, and might be
slow. The other interface, consisting of a bunch of
``sphinx_get_YYY_factor()`` functions, is a little more wordy to use,
but accesses the blob data directly and guarantees that there will be
zero allocations. So for top-notch ranking UDF performance, you want to
use that one.

As for the return types, UDFs can currently return a signle INTEGER,
BIGINT, FLOAT, or STRING value. The C function return type should be
sphinx\_int64\_t, sphinx\_int64\_t, double, or char\* respectively. In
the last case you <b>must</b> use ``args-&gt;fn_malloc`` function to
allocate the returned string values. Internally in your UDF you can use
whatever you want, so the ``testfunc_init()`` example above is correct
code even though it uses malloc() directly: you manage that pointer
yourself, it gets freed up using a matching free() call, and all is
well. However, the returned strings values are managed by Manticore and we
have our own allocator, so for the return values specifically, you need
to use it too.

Depending on how your UDFs are used in the query, the main function call
(``testfunc()`` in our example) might be called in a rather different
volume and order. Specifically,

-  UDFs referenced in WHERE, ORDER BY, or GROUP BY clauses must and will
   be evaluated for every matched document. They will be called in the
   natural matching order.

-  without subselects, UDFs that can be evaluated at the very last stage
   over the final result set will be evaluated that way, but before
   applying the LIMIT clause. They will be called in the result set
   order.

-  with subselects, such UDFs will also be evaluated after applying the
   inner LIMIT clause.

The calling sequence of the other functions is fixed, though. Namely,

-  ``testfunc_init()`` is called once when initializing the query. It
   can return a non-zero code to indicate a failure; in that case query
   will be terminated, and the error message from the ``error_message``
   buffer will be returned.

-  ``testfunc()`` is called for every eligible row (see above), whenever
   Manticore needs to compute the UDF value. It can also indicate an
   (internal) failure error by writing a non-zero byte value to
   ``error_flag``. In that case, it is guaranteed that will no more be
   called for subsequent rows, and a default return value of 0 will be
   substituted. Manticore might or might not choose to terminate such
   queries early, neither behavior is currently guaranteed.

-  ``testfunc_deinit()`` is called once when the query processing (in a
   given index shard) ends.

We do not yet support aggregation functions. In other words, your UDFs
will be called for just a single document at a time and are expected to
return some value for that document. Writing a function that can compute
an aggregate value like AVG() over the entire group of documents that
share the same GROUP BY key is not yet possible. However, you can use
UDFs within the builtin aggregate functions: that is, even though
MYCUSTOMAVG() is not supported yet, AVG(MYCUSTOMFUNC()) should work
alright!

UDFs are local. In order to use them on a cluster, you have to put the
same library on all its nodes and run CREATEs on all the nodes too. This
might change in the future versions.
