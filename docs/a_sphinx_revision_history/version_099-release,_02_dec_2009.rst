Version 0.9.9-release, 02 dec 2009
----------------------------------

-  added Open, Close, Status calls to libsphinxclient (C API)

-  added automatic persistent connection reopening to PHP, Python APIs

-  added 64-bit value/range filters, fullscan mode support to ManticoreSE

-  MAJOR CHANGE, our IANA assigned ports are 9312 and 9306 respectively
   (goodbye, trusty 3312)

-  MAJOR CHANGE, erroneous filters now fail with an error (were silently
   ignored before)

-  optimized unbuffered .spa writes on merge

-  optimized 1-keyword queries ranking in extended2 mode

-  fixed #441 (IO race in case of highly conccurent load on a preopened)

-  fixed #434 (distrubuted indexes were not searchable via MySQL
   protocol)

-  fixed #317 (indexer MVA progress counter)

-  fixed #398 (stopwords not removed from search query)

-  fixed #328 (broken cutoff)

-  fixed #250 (now quoting paths w/spaces when installing Windows
   service)

-  fixed #348 (K-list was not updated on merge)

-  fixed #357 (destination index were not K-list-filtered on merge)

-  fixed #369 (precaching .spi files over 2 GBs)

-  fixed #438 (missing boundary proximity matches)

-  fixed #371 (.spa flush in case of files over 2 GBs)

-  fixed #373 (crashes on distributed queries via mysql proto)

-  fixed critical bugs in hit merging code

-  fixed #424 (ordinals could be misplaced during indexing in case of
   bitfields etc)

-  fixed #426 (failing SE build on Solaris; thanks to Ben Beecher)

-  fixed #423 (typo in SE caused crash on SHOW STATUS)

-  fixed #363 (handling of read\_timeout over 2147 seconds)

-  fixed #376 (minor error message mismatch)

-  fixed #413 (minus in ManticoreQL)

-  fixed #417 (floats w/o leading digit in ManticoreQL)

-  fixed #403 (typo in SetFieldWeights name in Java API)

-  fixed index rotation vs persistent connections

-  fixed backslash handling in ManticoreQL parser

-  fixed uint unpacking vs. PHP 5.2.9 (possibly other versions)

-  fixed #325 (filter settings send from ManticoreSE)

-  fixed #352 (removed mysql wrapper around close() in ManticoreSE)

-  fixed #389 (display error messages through ManticoreSE status variable)

-  fixed linking with port-installed iconv on OS X

-  fixed negative 64-bit unpacking in PHP API

-  fixed #349 (escaping backslash in query emulation mode)

-  fixed #320 (disabled multi-query route when select items differ)

-  fixed #353 (better quorum counts check)

-  fixed #341 (merging of trailing hits; maybe other ranking issues too)

-  fixed #368 (partially; @field “” caused crashes; now resets field
   limit)

-  fixed #365 (field mask was leaking on field-limited terms)

-  fixed #339 (updated debug query dumper)

-  fixed #361 (added SetConnectTimeout() to Java API)

-  fixed #338 (added missing fullscan to mode check in Java API)

-  fixed #323 (added floats support to ManticoreQL)

-  fixed #340 (support listen=port:proto syntax too)

-  fixed #332 (:raw-latex:`\r `is legal ManticoreQL space now)

-  fixed xmlpipe2 K-lists

-  fixed #322 (safety gaps in mysql protocol row buffer)

-  fixed #313 (return keyword stats for empty indexes too)

-  fixed #344 (invalid checkpoints after merge)

-  fixed #326 (missing CLOCK\_xxx on FreeBSD)
