.. raw:: html

   <div class="navheader">

12.1.24. sql\_attr\_json
`Prev <conf-sql-attr-string.html>`__ 
12.1. Data source configuration options
 `Next <conf-sql-column-buffers.html>`__

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

.. rubric:: 12.1.24. sql\_attr\_json
   :name: sql_attr_json
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

JSON attribute declaration. Multi-value (ie. there may be more than one
such attribute declared), optional. Applies to SQL source types
(``mysql``, ``pgsql``, ``mssql``) only. Introduced in version
2.1.1-beta.

When indexing JSON attributes, Sphinx expects a text field with JSON
formatted data. As of 2.2.1-beta JSON attributes supports arbitrary JSON
data with no limitation in nested levels or types.

.. code:: programlisting

    {
        "id": 1,
        "gid": 2,
        "title": "some title",
        "tags": [
            "tag1",
            "tag2",
            "tag3"
            {
                "one": "two",
                "three": [4, 5]
            }
        ]
    }

These attributes allow Sphinx to work with documents without a fixed set
of attribute columns. When you filter on a key of a JSON attribute,
documents that don’t include the key will simply be ignored.

You can read more on JSON attributes in
http://sphinxsearch.com/blog/2013/08/08/full-json-support-in-trunk/.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    sql_attr_json = properties

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+----------------------------------+--------------------------------------------+
| `Prev <conf-sql-attr-string.html>`__    | `Up <confgroup-source.html>`__   |  `Next <conf-sql-column-buffers.html>`__   |
+-----------------------------------------+----------------------------------+--------------------------------------------+
| 12.1.23. sql\_attr\_string              | `Home <index.html>`__            |  12.1.25. sql\_column\_buffers             |
+-----------------------------------------+----------------------------------+--------------------------------------------+

.. raw:: html

   </div>
