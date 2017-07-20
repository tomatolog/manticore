SetGeoAnchor
~~~~~~~~~~~~

<b>Prototype:</b> function SetGeoAnchor ( $attrlat, $attrlong, $lat,
$long )

Sets anchor point for and geosphere distance (geodistance) calculations,
and enable them.

``$attrlat`` and ``$attrlong`` must be strings that contain the names of
latitude and longitude attributes, respectively. ``$lat`` and ``$long``
are floats that specify anchor point latitude and longitude, in radians.

Once an anchor point is set, you can use magic ``&quot;@geodist&quot;``
attribute name in your filters and/or sorting expressions. Manticore will
compute geosphere distance between the given anchor point and a point
specified by latitude and longitude attributes from each full-text
match, and attach this value to the resulting match. The latitude and
longitude values both in ``SetGeoAnchor`` and the index attribute data
are expected to be in radians. The result will be returned in meters, so
geodistance value of 1000.0 means 1 km. 1 mile is approximately 1609.344
meters.
