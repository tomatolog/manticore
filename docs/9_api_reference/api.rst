API reference
========================

There is a number of native searchd client API implementations for
Manticore. As of time of this writing, we officially support our own PHP,
Python, and Java implementations. There also are third party free,
open-source API implementations for Perl, Ruby, and C++.

The reference API implementation is in PHP, because (we believe) Manticore
is most widely used with PHP than any other language. This reference
documentation is in turn based on reference PHP API, and all code
samples in this section will be given in PHP.

However, all other APIs provide the same methods and implement the very
same network protocol. Therefore the documentation does apply to them as
well. There might be minor differences as to the method naming
conventions or specific data structures used. But the provided
functionality must not differ across languages.

.. toctree::
   :maxdepth: 4
   
   general_api_functions
   general_query_settings
   
 
.. toctree::
   :glob:
   :maxdepth: 2
   
   full-text_search_query_settings/*
   

.. toctree::
   :glob:
   :maxdepth: 2
   
   result_set_filtering_settings/*
   group_by_settings/*
   querying/*
   additional_functionality/*
   persistent_connections/*