grouping\_in\_utc
~~~~~~~~~~~~~~~~~

Specifies whether timed grouping in API and sphinxql will be calculated
in local timezone, or in UTC. Optional, default is 0 (means ‘local tz’).

By default all ‘group by time’ expressions (like group by day, week,
month and year in API, also group by day, month, year, yearmonth,
yearmonthday in Manticoreql) is done using local time. I.e. when you have
docs with attributes timed ‘13:00 utc’ and ‘15:00 utc’ - in case of
grouping they both will fall into facility group according to your local
tz setting. Say, if you live in ‘utc’, it will be one day, but if you
live in ‘utc+10’, then these docs will be matched into different ‘group
by day’ facility groups (since 13:00 utc in UTC+10 tz 23:00 local time,
but 15:00 is 01:00 of the next day). Sometimes such behavior is
unacceptable, and it is desirable to make time grouping not dependent
from timezone. Of course, you can run the daemon with defined global TZ
env variable, but it will affect not only grouping, but also
timestamping in the logs, which may be also undesirable. Switching ‘on’
this option (either in config, either using ‘set global’ statement in
sphinxql) will cause all time grouping expressions to be calculated in
UTC, leaving the rest of time-depentend functions (i.e. logging of the
daemon) in local TZ.
