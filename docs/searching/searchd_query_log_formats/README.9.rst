``searchd`` query log formats
-----------------------------

Two query log formats are supported. Plain text format is still the
default one. However, while it might be more convenient for manual
monitoring and review, but hard to replay for benchmarks, it only logs
*search* queries but not the other types of requests, does not always
contain the complete search query data, etc. The default text format is
also harder (and sometimes impossible) to replay for benchmarking
purposes. The ``sphinxql`` format alleviates that. It aims to be
complete and automatable, even though at the cost of brevity and
readability.
