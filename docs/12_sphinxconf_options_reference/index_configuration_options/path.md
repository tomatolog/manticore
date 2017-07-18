### path {#path}

Index files path and file name (without extension). Mandatory.

Path specifies both directory and file name, but without extension. `indexer` will append different extensions to this path when generating final names for both permanent and temporary index files. Permanent data files have several different extensions starting with &#039;.sp&#039;; temporary files&#039; extensions start with &#039;.tmp&#039;. It&#039;s safe to remove `.tmp*` files is if indexer fails to remove them automatically.

For reference, different index files store the following data:

*   `.spa` stores document attributes (used in [extern docinfo](../../index_configuration_options/docinfo.md) storage mode only);

*   `.spd` stores matching document ID lists for each word ID;

*   `.sph` stores index header information;

*   `.spi` stores word lists (word IDs and pointers to `.spd` file);

*   `.spk` stores kill-lists;

*   `.spm` stores MVA data;

*   `.spp` stores hit (aka posting, aka word occurrence) lists for each word ID;

*   `.sps` stores string attribute data.

*   `.spe` stores skip-lists to speed up doc-list filtering

#### Example: {#example}

```

path = /var/data/test1

```