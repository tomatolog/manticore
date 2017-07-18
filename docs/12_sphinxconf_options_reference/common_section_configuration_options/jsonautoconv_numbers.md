### json_autoconv_numbers {#json-autoconv-numbers}

Automatically detect and convert possible JSON strings that represent numbers, into numeric attributes. Optional, default value is 0 (do not convert strings into numbers). Added in 2.1.1-beta.

When this option is 1, values such as &quot;1234&quot; will be indexed as numbers instead of strings; if the option is 0, such values will be indexed as strings. This conversion applies to any data source, that is, JSON attributes originating from either SQL or XMLpipe2 sources will all be affected.

#### Example: {#example}

```

json_autoconv_numbers = 1

```