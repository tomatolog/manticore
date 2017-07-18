BuildKeywords
~~~~~~~~~~~~~

<b>Prototype:</b> function BuildKeywords ( $query, $index, $hits )

Extracts keywords from query using tokenizer settings for given index,
optionally with per-keyword occurrence statistics. Returns an array of
hashes with per-keyword information.

``$query`` is a query to extract keywords from. ``$index`` is a name of
the index to get tokenizing settings and keyword occurrence statistics
from. ``$hits`` is a boolean flag that indicates whether keyword
occurrence statistics are required.

Usage example:

::


    $keywords = $cl->BuildKeywords ( "this.is.my query", "test1", false );

