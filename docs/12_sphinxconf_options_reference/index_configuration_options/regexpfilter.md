### regexp_filter {#regexp-filter}

Regular expressions (regexps) to filter the fields and queries with. Optional, multi-value, default is an empty list of regexps. Added in 2.1.1-beta.

In certain applications (like product search) there can be many different ways to call a model, or a product, or a property, and so on. For instance, &#039;iphone 3gs&#039; and &#039;iphone 3 gs&#039; (or even &#039;iphone3 gs&#039;) are very likely to mean the same product. Or, for a more tricky example, &#039;13-inch&#039;, &#039;13 inch&#039;, &#039;13&quot;&#039;, and &#039;13in&#039; in a laptop screen size descriptions do mean the same.

Regexps provide you with a mechanism to specify a number of rules specific to your application to handle such cases. In the first &#039;iphone 3gs&#039; example, you could possibly get away with a wordforms files tailored to handle a handful of iPhone models. However even in a comparatively simple second &#039;13-inch&#039; example there is just way too many individual forms and you are better off specifying rules that would normalize both &#039;13-inch&#039; and &#039;13in&#039; to something identical.

Regular expressions listed in `regexp_filter` are applied in the order they are listed. That happens at the earliest stage possible, before any other processing, even before tokenization. That is, regexps are applied to the raw source fields when indeixng, and to the raw search query text when searching.

We use the [RE2 engine](https://github.com/google/re2) to implement regexps. So when building from the source, the library must be installed in the system and Sphinx must be configured built with a `--with-re2` switch. Binary packages should come with RE2 builtin.

#### Example: {#example}

```

# index '13-inch' as '13inch'
regexp_filter = \b(\d+)\" => \1inch

# index 'blue' or 'red' as 'color'
regexp_filter = (blue|red) => color

```