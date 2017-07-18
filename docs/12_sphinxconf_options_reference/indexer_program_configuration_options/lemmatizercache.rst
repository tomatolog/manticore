lemmatizer\_cache
~~~~~~~~~~~~~~~~~

Lemmatizer cache size. Optional, default is 256K. Added in version
2.1.1-beta.

Our lemmatizer implementation (see `the section called
“morphology” <../../index_configuration_options/morphology.md>`__ for a
discussion of what lemmatizers are) uses a compressed dictionary format
that enables a space/speed tradeoff. It can either perform lemmatization
off the compressed data, using more CPU but less RAM, or it can
decompress and precache the dictionary either partially or fully, thus
using less CPU but more RAM. And the lemmatizer\_cache directive lets
you control how much RAM exactly can be spent for that uncompressed
dictionary cache.

Currently, the only available dictionary is ru.pak, the Russian one. The
compressed dictionary is approximately 10 MB in size. Note that the
dictionary stays in memory at all times, too. The default cache size is
256 KB. The accepted cache sizes are 0 to 2047 MB. It's safe to raise
the cache size too high; the lemmatizer will only use the needed memory.
For instance, the entire Russian dictionary decompresses to
approximately 110 MB; and thus setting lemmatizer\_cache anywhere higher
than that will not affect the memory use: even when 1024 MB is allowed
for the cache, if only 110 MB is needed, it will only use those 110 MB.

On our benchmarks, the total indexing time with different cache sizes
was as follows:

-  9.07 sec, morphology = lemmatize\_ru, lemmatizer\_cache = 0
-  8.60 sec, morphology = lemmatize\_ru, lemmatizer\_cache = 256K
-  8.33 sec, morphology = lemmatize\_ru, lemmatizer\_cache = 8M
-  7.95 sec, morphology = lemmatize\_ru, lemmatizer\_cache = 128M
-  6.85 sec, morphology = stem\_ru (baseline)

Your mileage may vary, but a simple rule of thumb would be to either go
with the small default 256 KB cache when pressed for memory, or spend
128 MB extra RAM and cache the entire dictionary for maximum indexing
performance.

Example:
^^^^^^^^

::


    lemmatizer_cache = 256M # cache it all

