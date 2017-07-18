Known caveats with RT indexes
-----------------------------

RT indexes are currently quality feature, but there are still a few
known usage quirks. Those quirks are listed in this section.

-  Default conservative RAM chunk limit (``rt_mem_limit``) of 32M can
   lead to poor performance on bigger indexes, you should raise it to
   256..1024M if you're planning to index gigabytes.

-  The only attribute storage mode is ‘extern’ which requires at least
   one attribute to be present.
-  High DELETE/REPLACE rate can lead to kill-list fragmentation and
   impact searching performance.

-  No transaction size limits are currently imposed; too many concurrent
   INSERT/REPLACE transactions might therefore consume a lot of RAM.

-  In case of a damaged binlog, recovery will stop on the f.html damaged
   transaction, even though it's technically possible to keep looking
   further for subsequent undamaged transactions, and recover those.
   This mid-file damage case (due to flaky HDD/CDD/tape?) is supposed to
   be extremely rare, though.

-  Multiple INSERTs grouped in a single transaction perform better than
   equivalent single-row transactions and are recommended for batch
   loading of data.
