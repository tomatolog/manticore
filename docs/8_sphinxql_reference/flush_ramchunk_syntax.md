## FLUSH RAMCHUNK syntax {#flush-ramchunk-syntax}

```

FLUSH RAMCHUNK rtindex

```

FLUSH RAMCHUNK statement, added in version 2.1.2-release, forcibly creates a new disk chunk in a RT index.

Normally, RT index would flush and convert the contents of the RAM chunk into a new disk chunk automatically, once the RAM chunk reaches the maximum allowed [rt_mem_limit](../index_configuration_options/rtmem_limit.md) size. However, for debugging and testing it might be useful to forcibly create a new disk chunk, and FLUSH RAMCHUNK statement does exactly that.

Note that using FLUSH RAMCHUNK increases RT index fragmentation. Most likely, you want to use FLUSH RTINDEX instead. We suggest that you abstain from using just this statement unless you&#039;re absolutely sure what you&#039;re doing. As the right way is to issue FLUSH RAMCHUNK with following [OPTIMIZE](../optimize_index_syntax.md) command. Such combo allows to keep RT index fragmentation on minimum.

```

mysql> FLUSH RAMCHUNK rt;
Query OK, 0 rows affected (0.05 sec)

```