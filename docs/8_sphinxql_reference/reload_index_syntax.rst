RELOAD INDEX syntax
-------------------

::


    RELOAD INDEX idx [ FROM '/path/to/index_files' ]

RELOAD INDEX allows you to rotate indexes using ManticoreQL.

It has two modes of operation. First one (without specifying a path)
makes Manticore daemon check for new index files in directory specified in
`the section called “path” <../index_configuration_options/path.md>`__.
New index files must have a idx.new.sp? names.

And if you additionally specify a path, daemon will look for index files
in specified directory, move them to index `the section called
“path” <../index_configuration_options/path.md>`__, rename from
index\_files.sp? to idx.new.sp? and rotate them.

::


    mysql> RELOAD INDEX plain_index;
    mysql> RELOAD INDEX plain_index FROM '/home/mighty/new_index_files';

