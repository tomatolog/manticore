### max_file_field_buffer {#max-file-field-buffer}

Maximum file field adaptive buffer size, bytes. Optional, default is 8 MB, minimum is 1 MB.

File field buffer is used to load files referred to from [sql_file_field](../../data_source_configuration_options/sqlfile_field.md) columns. This buffer is adaptive, starting at 1 MB at first allocation, and growing in 2x steps until either file contents can be loaded, or maximum buffer size, specified by `max_file_field_buffer` directive, is reached.

Thus, if there are no file fields are specified, no buffer is allocated at all. If all files loaded during indexing are under (for example) 2 MB in size, but `max_file_field_buffer` value is 128 MB, peak buffer usage would still be only 2 MB. However, files over 128 MB would be entirely skipped.

#### Example: {#example}

```

max_file_field_buffer = 128M

```