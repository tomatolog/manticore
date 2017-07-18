.. raw:: html

   <div class="navheader">

12.5.2. on\_json\_attr\_error
`Prev <conf-lemmatizer-base.html>`__ 
12.5. Common section configuration options
 `Next <conf-json-autoconv-numbers.html>`__

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

.. rubric:: 12.5.2. on\_json\_attr\_error
   :name: on_json_attr_error
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

What to do if JSON format errors are found. Optional, default value is
``ignore_attr`` (ignore errors). Applies only to ``sql_attr_json``
attributes. Added in 2.1.1-beta.

By default, JSON format errors are ignored (``ignore_attr``) and the
indexer tool will just show a warning. Setting this option to
``fail_index`` will rather make indexing fail at the first JSON format
error.

.. rubric:: Example:
   :name: example

.. code:: programlisting

    on_json_attr_error = ignore_attr

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------+----------------------------------+-----------------------------------------------+
| `Prev <conf-lemmatizer-base.html>`__    | `Up <confgroup-common.html>`__   |  `Next <conf-json-autoconv-numbers.html>`__   |
+-----------------------------------------+----------------------------------+-----------------------------------------------+
| 12.5.1. lemmatizer\_base                | `Home <index.html>`__            |  12.5.3. json\_autoconv\_numbers              |
+-----------------------------------------+----------------------------------+-----------------------------------------------+

.. raw:: html

   </div>
