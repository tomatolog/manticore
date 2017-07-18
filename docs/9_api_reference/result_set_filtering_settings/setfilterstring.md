### SetFilterString {#setfilterstring}

&lt;b&gt;Prototype:&lt;/b&gt; function SetFilterString ( $attribute, $value, $exclude=false )

Adds new string value filter.

On this call, additional new filter is added to the existing list of filters. `$attribute` must be a string with attribute name. `$value` must be a string. `$exclude` must be a boolean value; it controls whether to accept the matching documents (default mode, when `$exclude` is false) or reject them.

Only those documents where `$attribute` column value stored in the index matches string value from `$value` will be matched (or rejected, if `$exclude` is true).