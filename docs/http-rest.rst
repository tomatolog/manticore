.. raw:: html

   <div class="navheader">

5.11. HTTP protocol
`Prev <sphinxql.html>`__ 
Chapter 5. Searching
 `Next <multi-queries.html>`__

--------------

.. raw:: html

   </div>

.. raw:: html

   <div class="sect1">

.. raw:: html

   <div class="titlepage">

.. raw:: html

   <div>

.. raw:: html

   <div>

.. rubric:: 5.11. HTTP protocol
   :name: http-protocol
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Starting with 2.3.2-beta, Sphinx search daemon supports HTTP protocol
and can be accessed with regular HTTP clients. Available only with
workers = thread\_pool.

To enabled the HTTP protocol, a `listen <conf-listen.html>`__ directive
with http specified as a protocol needs to be declared:

.. code:: programlisting

    listen = localhost:8080:http

Supported endpoints:

.. raw:: html

   <div class="itemizedlist">

-  / - default response, returns a simple HTML page

-  /search - allows a simple full-text search, parameters can be : index
   (index or list of indexes), match (equivalent of MATCH()), select (as
   SELECT clause), group (grouping attribute), order (SQL-like sorting),
   limit (equivalent of LIMIT 0,N)

   .. code:: programlisting

       curl -X POST 'http://sphinxsearch:9308/search/' 
       -d 'index=forum&match=@subject php sphinx&select=id,subject,author_id&limit=5'

-  / sql - allows running a SELECT SphinxQL, set as query parameter

   .. code:: programlisting

        curl -X POST 'http://sphinxsearch:9308/sql/' 
       -d 'query=select id,subject,author_id  from forum where match('@subject php sphinx')  group by author_id order by id desc limit 0,5'

.. raw:: html

   </div>

The result for /sql/ and /search/ endpoints is an array of attrs,matches
and meta, same as for SphinxAPI, encoded as a JSON object.

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+----------------------------------------------+---------------------------+----------------------------------+
| `Prev <sphinxql.html>`__                     | `Up <searching.html>`__   |  `Next <multi-queries.html>`__   |
+----------------------------------------------+---------------------------+----------------------------------+
| 5.10. MySQL protocol support and SphinxQL    | `Home <index.html>`__     |  5.12. Multi-queries             |
+----------------------------------------------+---------------------------+----------------------------------+

.. raw:: html

   </div>
