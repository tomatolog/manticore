.. raw:: html

   <div class="navheader">

Chapter 9. API reference
`Prev <sphinxql-upgrading-magics.html>`__ 
 
 `Next <api-funcgroup-general.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="chapter">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="toc">

**Table of Contents**

`9.1. General API functions <api-funcgroup-general.html>`__
`9.2. General query
settings <api-funcgroup-general-query-settings.html>`__
`9.3. Full-text search query
settings <api-funcgroup-fulltext-query-settings.html>`__
`9.4. Result set filtering settings <api-funcgroup-filtering.html>`__
`9.5. GROUP BY settings <api-funcgroup-groupby.html>`__
`9.6. Querying <api-funcgroup-querying.html>`__
`9.7. Additional
functionality <api-funcgroup-additional-functionality.html>`__
`9.8. Persistent connections <api-funcgroup-pconn.html>`__

.. raw:: html

   </div>

There is a number of native searchd client API implementations for
Sphinx. As of time of this writing, we officially support our own PHP,
Python, and Java implementations. There also are third party free,
open-source API implementations for Perl, Ruby, and C++.

The reference API implementation is in PHP, because (we believe) Sphinx
is most widely used with PHP than any other language. This reference
documentation is in turn based on reference PHP API, and all code
samples in this section will be given in PHP.

However, all other APIs provide the same methods and implement the very
same network protocol. Therefore the documentation does apply to them as
well. There might be minor differences as to the method naming
conventions or specific data structures used. But the provided
functionality must not differ across languages.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------------+-------------------------+------------------------------------------+
| `Prev <sphinxql-upgrading-magics.html>`__           |                         |  `Next <api-funcgroup-general.html>`__   |
+-----------------------------------------------------+-------------------------+------------------------------------------+
| 8.49. SphinxQL upgrade notes, version 2.0.1-beta    | `Home <index.html>`__   |  9.1. General API functions              |
+-----------------------------------------------------+-------------------------+------------------------------------------+

.. raw:: html

   </div>
