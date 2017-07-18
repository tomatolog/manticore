## Version 2.2.8-release, 09 mar 2015 {#version-2-2-8-release-09-mar-2015}

### Minor features {#minor-features}

*   added #2166, per agent HA strategy for distributed indexes

### Bug fixes {#bug-fixes}

*   fixed #2182, incorrect query results with multiple same destination wordforms

*   fixed #2181, improved error message on incorrect filters

*   fixed #2178, ZONESPAN operator for queries with more than two words

*   fixed #2172, incorrect results with field position fulltext operators

*   fixed #2171, some index options do not work for template indexes

*   fixed #2170, joined fields indexation with document id equals to 0

*   fixed #2110, crash on snippet generation

*   fixed WLCCS ranking factor computation

*   fixed memory leak on queries with ZONEs