### html_remove_elements {#html-remove-elements}

A list of HTML elements for which to strip contents along with the elements themselves. Optional, default is empty string (do not strip contents of any elements).

This feature allows to strip element contents, ie. everything that is between the opening and the closing tags. It is useful to remove embedded scripts, CSS, etc. Short tag form for empty elements (ie. &lt;br /&gt;) is properly supported; ie. the text that follows such tag will &lt;b&gt;not&lt;/b&gt; be removed.

The value is a comma-separated list of element (tag) names whose contents should be removed. Tag names are case insensitive.

#### Example: {#example}

```

html_remove_elements = style, script

```