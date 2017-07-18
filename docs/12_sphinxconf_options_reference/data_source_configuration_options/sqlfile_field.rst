sql\_file\_field
~~~~~~~~~~~~~~~~

File based field declaration. Applies to SQL source types (``mysql``,
``pgsql``, ``mssql``) only. Introduced in version 1.10-beta.

This directive makes ``indexer`` interpret field contents as a file
name, and load and index the referred file. Files larger than
`max\_file\_field\_buffer <../../indexer_program_configuration_options/maxfile_field_buffer.html>`__
in size are skipped. Any errors during the file loading (IO errors,
missed limits, etc) will be reported as indexing warnings and will
<b>not</b> early terminate the indexing. No content will be indexed for
such files.

Example:
^^^^^^^^

::


    sql_file_field = my_file_path # load and index files referred to by my_file_path

