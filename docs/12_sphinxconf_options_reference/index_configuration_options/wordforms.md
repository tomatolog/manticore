### wordforms {#wordforms}

Word forms dictionary. Optional, default is empty.

Word forms are applied after tokenizing the incoming text by [charset_table](../../index_configuration_options/charsettable.md) rules. They essentially let you replace one word with another. Normally, that would be used to bring different word forms to a single normal form (eg. to normalize all the variants such as &quot;walks&quot;, &quot;walked&quot;, &quot;walking&quot; to the normal form &quot;walk&quot;). It can also be used to implement stemming exceptions, because stemming is not applied to words found in the forms list.

Starting with version 2.1.1-beta small enough files are stored in the index header, see [the section called “embedded_limit”](../../index_configuration_options/embeddedlimit.md) for details.

Dictionaries are used to normalize incoming words both during indexing and searching. Therefore, to pick up changes in wordforms file it&#039;s required to rotate index.

Word forms support in Sphinx is designed to support big dictionaries well. They moderately affect indexing speed: for instance, a dictionary with 1 million entries slows down indexing about 1.5 times. Searching speed is not affected at all. Additional RAM impact is roughly equal to the dictionary file size, and dictionaries are shared across indexes: ie. if the very same 50 MB wordforms file is specified for 10 different indexes, additional `searchd` RAM usage will be about 50 MB.

Dictionary file should be in a simple plain text format. Each line should contain source and destination word forms, in UTF-8 encoding, separated by &quot;greater&quot; sign. Rules from the [charset_table](../../index_configuration_options/charsettable.md) will be applied when the file is loaded. So basically it&#039;s as case sensitive as your other full-text indexed data, ie. typically case insensitive. Here&#039;s the file contents sample:

```

walks > walk
walked > walk
walking > walk

```

There is a bundled `spelldump` utility that helps you create a dictionary file in the format Sphinx can read from source `.dict` and `.aff` dictionary files in `ispell` or `MySpell` format (as bundled with OpenOffice).

Starting with version 0.9.9-rc1, you can map several source words to a single destination word. Because the work happens on tokens, not the source text, differences in whitespace and markup are ignored.

Starting with version 2.1.1-beta, you can use &quot;=&gt;&quot; instead of &quot;&gt;&quot;. Comments (starting with &quot;#&quot; are also allowed. Finally, if a line starts with a tilde (&quot;~&quot;) the wordform will be applied after morphology, instead of before.

```

core 2 duo > c2d
e6600 > c2d
core 2duo => c2d # Some people write '2duo' together...

```

Stating with version 2.2.4, you can specify multiple destination tokens:

```

s02e02 > season 2 episode 2
s3 e3 > season 3 episode 3

```

#### Example: {#example}

```

wordforms = /usr/local/sphinx/data/wordforms.txt
wordforms = /usr/local/sphinx/data/alternateforms.txt
wordforms = /usr/local/sphinx/private/dict*.txt

```

Starting with version 2.1.1-beta you can specify several files and not only just one. Masks can be used as a pattern, and all matching files will be processed in simple ascending order. (If multi-byte codepages are used, and file names can include foreign characters, the resulting order may not be exactly alphabetic.) If a same wordform definition is found in several files, the latter one is used, and it overrides previous definitions.