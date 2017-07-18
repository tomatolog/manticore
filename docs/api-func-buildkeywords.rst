.. raw:: html

   <div class="navheader">

9.7.3. BuildKeywords
`Prev <api-func-updateatttributes.html>`__ 
9.7. Additional functionality
 `Next <api-func-escapestring.html>`__

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

.. rubric:: 9.7.3. BuildKeywords
   :name: buildkeywords
   :class: title

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

**Prototype:** function BuildKeywords ( $query, $index, $hits )

Extracts keywords from query using tokenizer settings for given index,
optionally with per-keyword occurrence statistics. Returns an array of
hashes with per-keyword information.

``$query`` is a query to extract keywords from. ``$index`` is a name of
the index to get tokenizing settings and keyword occurrence statistics
from. ``$hits`` is a boolean flag that indicates whether keyword
occurrence statistics are required.

Usage example:

.. code:: programlisting

    $keywords = $cl->BuildKeywords ( "this.is.my query", "test1", false );

.. raw:: html

   </div>

.. raw:: html

   <div class="navfooter">

--------------

+-----------------------------------------------+--------------------------------------------------------+------------------------------------------+
| `Prev <api-func-updateatttributes.html>`__    | `Up <api-funcgroup-additional-functionality.html>`__   |  `Next <api-func-escapestring.html>`__   |
+-----------------------------------------------+--------------------------------------------------------+------------------------------------------+
| 9.7.2. UpdateAttributes                       | `Home <index.html>`__                                  |  9.7.4. EscapeString                     |
+-----------------------------------------------+--------------------------------------------------------+------------------------------------------+

.. raw:: html

   </div>
