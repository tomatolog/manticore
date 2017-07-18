.. raw:: html

   <div class="navheader">

9.6.3. RunQueries
`Prev <api-func-addquery.html>`__ 
9.6. Querying
 `Next <api-func-resetfilters.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect2">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 9.6.3. RunQueries
   :name: runqueries
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function RunQueries ()

Connect to searchd, runs a batch of all queries added using
``AddQuery()``, obtains and returns the result sets. Returns false and
sets ``GetLastError()`` message on general error (such as network I/O
failure). Returns a plain array of result sets on success.

Each result set in the returned array is exactly the same as the result
set returned from ```Query()`` <api-func-query.html>`__.

Note that the batch query request itself almost always succeeds - unless
there’s a network error, blocking index rotation in progress, or another
general failure which prevents the whole request from being processed.

However individual queries within the batch might very well fail. In
this case their respective result sets will contain non-empty
``"error"`` message, but no matches or query statistics. In the extreme
case all queries within the batch could fail. There still will be no
general error reported, because API was able to successfully connect to
``searchd``, submit the batch, and receive the results - but every
result set will have a specific error message.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+--------------------------------------+----------------------------------------+------------------------------------------+
| `Prev <api-func-addquery.html>`__    | `Up <api-funcgroup-querying.html>`__   |  `Next <api-func-resetfilters.html>`__   |
+--------------------------------------+----------------------------------------+------------------------------------------+
| 9.6.2. AddQuery                      | `Home <index.html>`__                  |  9.6.4. ResetFilters                     |
+--------------------------------------+----------------------------------------+------------------------------------------+

.. raw:: html

   </div>
