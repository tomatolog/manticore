### xmlpipe_command {#xmlpipe-command}

Shell command that invokes xmlpipe2 stream producer. Mandatory. Applies to `xmlpipe2` source types only.

Specifies a command that will be executed and which output will be parsed for documents. Refer to [the section called “xmlpipe2 data source”](../../xmlpipe2_data_source.md) for specific format description.

#### Example: {#example}

```

xmlpipe_command = cat /home/sphinx/test.xml

```