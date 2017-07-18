## Extended query syntax {#extended-query-syntax}

The following special operators and modifiers can be used when using the extended matching mode:

*   operator OR:

    ```
    hello | world
    ```

*   operator MAYBE (introduced in verion 2.2.3-beta):

    ```
    hello MAYBE world
    ```

*   operator NOT:

    ```

    hello -world
    hello !world

    ```

*   field search operator:

    ```
    @title hello @body world
    ```

*   field position limit modifier (introduced in version 0.9.9-rc1):

    ```
    @body[50] hello
    ```

*   multiple-field search operator:

    ```
    @(title,body) hello world
    ```

*   ignore field search operator (will ignore any matches of &#039;hello world&#039; from field &#039;title&#039;):

    ```
    @!title hello world
    ```

*   ignore multiple-field search operator (if we have fields title, subject and body then @!(title) is equivalent to @(subject,body)):

    ```
    @!(title,body) hello world
    ```

*   all-field search operator:

    ```
    @* hello
    ```

*   phrase search operator:

    ```
    "hello world"
    ```

*   proximity search operator:

    ```
    "hello world"~10
    ```

*   quorum matching operator:

    ```
    "the world is a wonderful place"/3
    ```

*   strict order operator (aka operator &quot;before&quot;):

    ```
    aaa << bbb << ccc
    ```

*   exact form modifier (introduced in version 0.9.9-rc1):

    ```
    raining =cats and =dogs
    ```

*   field-start and field-end modifier (introduced in version 0.9.9-rc2):

    ```
    ^hello world$
    ```

*   keyword IDF boost modifier (introduced in version 2.2.3-beta):

    ```
    boosted^1.234 boostedfieldend$^1.234
    ```

*   NEAR, generalized proximity operator (introduced in version 2.0.1-beta):

    ```
    hello NEAR/3 world NEAR/4 "my test"
    ```

*   SENTENCE operator (introduced in version 2.0.1-beta):

    ```
    all SENTENCE words SENTENCE "in one sentence"
    ```

*   PARAGRAPH operator (introduced in version 2.0.1-beta):

    ```
    "Bill Gates" PARAGRAPH "Steve Jobs"
    ```

*   ZONE limit operator:

    ```
    ZONE:(h3,h4)
    ```

    only in these titles

*   ZONESPAN limit operator:

    ```
    ZONESPAN:(h2)
    ```

    only in a (single) title

Here&#039;s an example query that uses some of these operators:

###### Example 5.2. Extended matching mode: query example {#example-5-2-extended-matching-mode-query-example}

```

"hello world" @title "example program"~5 @body python -(php|perl) @* code

```

The full meaning of this search is:

*   Find the words &#039;hello&#039; and &#039;world&#039; adjacently in any field in a document;

*   Additionally, the same document must also contain the words &#039;example&#039; and &#039;program&#039; in the title field, with up to, but not including, 5 words between the words in question; (E.g. &quot;example PHP program&quot; would be matched however &quot;example script to introduce outside data into the correct context for your program&quot; would not because two terms have 5 or more words between them)

*   Additionally, the same document must contain the word &#039;python&#039; in the body field, but not contain either &#039;php&#039; or &#039;perl&#039;;

*   Additionally, the same document must contain the word &#039;code&#039; in any field.

There always is implicit AND operator, so &quot;hello world&quot; means that both &quot;hello&quot; and &quot;world&quot; must be present in matching document.

OR operator precedence is higher than AND, so &quot;looking for cat | dog | mouse&quot; means &quot;looking for ( cat | dog | mouse )&quot; and _not_ &quot;(looking for cat) | dog | mouse&quot;.

Field limit operator limits subsequent searching to a given field. Normally, query will fail with an error message if given field name does not exist in the searched index. However, that can be suppressed by specifying &quot;@@relaxed&quot; option at the very beginning of the query:

```

@@relaxed @nosuchfield my query

```

This can be helpful when searching through heterogeneous indexes with different schemas.

Field position limit, introduced in version 0.9.9-rc1, additionally restricts the searching to first N position within given field (or fields). For example, &quot;@body[50] hello&quot; will &lt;b&gt;not&lt;/b&gt; match the documents where the keyword &#039;hello&#039; occurs at position 51 and below in the body.

Proximity distance is specified in words, adjusted for word count, and applies to all words within quotes. For instance, &quot;cat dog mouse&quot;~5 query means that there must be less than 8-word span which contains all 3 words, ie. &quot;CAT aaa bbb ccc DOG eee fff MOUSE&quot; document will _not_ match this query, because this span is exactly 8 words long.

Quorum matching operator introduces a kind of fuzzy matching. It will only match those documents that pass a given threshold of given words. The example above (&quot;the world is a wonderful place&quot;/3) will match all documents that have at least 3 of the 6 specified words. Operator is limited to 255 keywords. Instead of an absolute number, you can also specify a number between 0.0 and 1.0 (standing for 0% and 100%), and Sphinx will match only documents with at least the specified percentage of given words. The same example above could also have been written &quot;the world is a wonderful place&quot;/0.5 and it would match documents with at least 50% of the 6 words.

Strict order operator (aka operator &quot;before&quot;), introduced in version 0.9.9-rc2, will match the document only if its argument keywords occur in the document exactly in the query order. For instance, &quot;black &lt;&lt; cat&quot; query (without quotes) will match the document &quot;black and white cat&quot; but _not_ the &quot;that cat was black&quot; document. Order operator has the lowest priority. It can be applied both to just keywords and more complex expressions, ie. this is a valid query:

```

(bag of words) << "exact phrase" << red|green|blue

```

Exact form keyword modifier, introduced in version 0.9.9-rc1, will match the document only if the keyword occurred in exactly the specified form. The default behavior is to match the document if the stemmed keyword matches. For instance, &quot;runs&quot; query will match both the document that contains &quot;runs&quot; _and_ the document that contains &quot;running&quot;, because both forms stem to just &quot;run&quot; - while &quot;=runs&quot; query will only match the first document. Exact form operator requires [index_exact_words](../index_configuration_options/indexexact_words.md) option to be enabled. This is a modifier that affects the keyword and thus can be used within operators such as phrase, proximity, and quorum operators. Starting with 2.2.2-beta, it is possible to apply an exact form modifier to the phrase operator. It&#039;s really just syntax sugar - it adds an exact form modifier to all terms contained within the phrase.

```

="exact phrase"

```

Field-start and field-end keyword modifiers, introduced in version 0.9.9-rc2, will make the keyword match only if it occurred at the very start or the very end of a fulltext field, respectively. For instance, the query &quot;^hello world$&quot; (with quotes and thus combining phrase operator and start/end modifiers) will only match documents that contain at least one field that has exactly these two keywords.

Starting with 0.9.9-rc1, arbitrarily nested brackets and negations are allowed. However, the query must be possible to compute without involving an implicit list of all documents:

```

// correct query
aaa -(bbb -(ccc ddd))

// queries that are non-computable
-aaa
aaa | -bbb

```

Starting with 2.2.2-beta, the phrase search operator may include a &#039;match any term&#039; modifier. Terms within the phrase operator are position significant. When the &#039;match any term&#039; modifier is implemented, the position of the subsequent terms from that phrase query will be shifted. Therefore, &#039;match any&#039; has no impact on search performance.

```

"exact * phrase * * for terms"

```

&lt;b&gt;NEAR operator&lt;/b&gt;, added in 2.0.1-beta, is a generalized version of a proximity operator. The syntax is `NEAR/N`, it is case-sensitive, and no spaces are allowed between the NEAR keyword, the slash sign, and the distance value.

The original proximity operator only worked on sets of keywords. NEAR is more generic and can accept arbitrary subexpressions as its two arguments, matching the document when both subexpressions are found within N words of each other, no matter in which order. NEAR is left associative and has the same (lowest) precedence as BEFORE.

You should also note how a `(one NEAR/7 two NEAR/7 three)` query using NEAR is not really equivalent to a `(&quot;one two three&quot;~7)` one using keyword proximity operator. The difference here is that the proximity operator allows for up to 6 non-matching words between all the 3 matching words, but the version with NEAR is less restrictive: it would allow for up to 6 words between &#039;one&#039; and &#039;two&#039; and then for up to 6 more between that two-word matching and a &#039;three&#039; keyword.

&lt;b&gt;SENTENCE and PARAGRAPH operators&lt;/b&gt;, added in 2.0.1-beta, matches the document when both its arguments are within the same sentence or the same paragraph of text, respectively. The arguments can be either keywords, or phrases, or the instances of the same operator. Here are a few examples:

```

one SENTENCE two
one SENTENCE "two three"
one SENTENCE "two three" SENTENCE four

```

The order of the arguments within the sentence or paragraph does not matter. These operators only work on indexes built with [index_sp](../index_configuration_options/indexsp.md) (sentence and paragraph indexing feature) enabled, and revert to a mere AND otherwise. Refer to the `index_sp` directive documentation for the notes on what&#039;s considered a sentence and a paragraph.

&lt;b&gt;ZONE limit operator&lt;/b&gt;, added in 2.0.1-beta, is quite similar to field limit operator, but restricts matching to a given in-field zone or a list of zones. Note that the subsequent subexpressions are _not_ required to match in a single contiguous span of a given zone, and may match in multiple spans. For instance, `(ZONE:th hello world)` query _will_ match this example document:

```

<th>Table 1\. Local awareness of Hello Kitty brand.</th>
.. some table data goes here ..
<th>Table 2\. World-wide brand awareness.</th>

```

ZONE operator affects the query until the next field or ZONE limit operator, or the closing parenthesis. It only works on the indexes built with zones support (see [the section called “index_zones”](../index_configuration_options/indexzones.md)) and will be ignored otherwise.

&lt;b&gt;ZONESPAN limit operator&lt;/b&gt;, added in 2.1.1-beta, is similar to the ZONE operator, but requires the match to occur in a single contiguous span. In the example above, `(ZONESPAN:th hello world)&gt;` would not match the document, since &quot;hello&quot; and &quot;world&quot; do not occur within the same span.

&lt;b&gt;MAYBE&lt;/b&gt; operator was added in 2.2.3-beta. It works much like | operator but doesn&#039;t return documents which match only right subtree expression.