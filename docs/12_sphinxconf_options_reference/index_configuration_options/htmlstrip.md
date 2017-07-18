### html_strip {#html-strip}

Whether to strip HTML markup from incoming full-text data. Optional, default is 0. Known values are 0 (disable stripping) and 1 (enable stripping).

Both HTML tags and entities and considered markup and get processed.

HTML tags are removed, their contents (i.e., everything between &lt;P&gt; and &lt;/P&gt;) are left intact by default. You can choose to keep and index attributes of the tags (e.g., HREF attribute in an A tag, or ALT in an IMG one). Several well-known inline tags are completely removed, all other tags are treated as block level and replaced with whitespace. For example, &#039;te&lt;B&gt;st&lt;/B&gt;&#039; text will be indexed as a single keyword &#039;test&#039;, however, &#039;te&lt;P&gt;st&lt;/P&gt;&#039; will be indexed as two keywords &#039;te&#039; and &#039;st&#039;. Known inline tags are as follows: A, B, I, S, U, BASEFONT, BIG, EM, FONT, IMG, LABEL, SMALL, SPAN, STRIKE, STRONG, SUB, SUP, TT.

HTML entities get decoded and replaced with corresponding UTF-8 characters. Stripper supports both numeric forms (such as &amp;#239;) and text forms (such as &amp;oacute; or &amp;nbsp;). All entities as specified by HTML4 standard are supported.

Stripping should work with properly formed HTML and XHTML, but, just as most browsers, may produce unexpected results on malformed input (such as HTML with stray &lt;&#039;s or unclosed &gt;&#039;s).

Only the tags themselves, and also HTML comments, are stripped. To strip the contents of the tags too (eg. to strip embedded scripts), see [html_remove_elements](../../index_configuration_options/htmlremove_elements.md) option. There are no restrictions on tag names; ie. everything that looks like a valid tag start, or end, or a comment will be stripped.

#### Example: {#example}

```

html_strip = 1

```