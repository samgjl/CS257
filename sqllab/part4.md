# Part 4: Writing Queries
### How many earthquakes occurred between midnight and 6am Alaska time (GMT - 9)?
Query: 
> ```SELECT * FROM earthquakes WHERE extract(hour from quaketime) between 15 and 20;```
> *change to ```SELECT COUNT(\*) FROM ...``` for the number of entries*

There were 359 Earthquakes from 12am to 6am Alaska Time.
### How many of these happened in Alaska?
Query:
> ``` SELECT * FROM earthquakes WHERE longitude BETWEEN -180 and -130 AND latitude BETWEEN 52 and 71;```

There were 75 earthquakes in Australia.

### Comibing the two:
Query:
> ```SELECT * FROM earthquakes WHERE extract(hour from quaketime) BETWEEN 15 AND 20```
> <br> ```INTERSECT``` <br> 
> ```SELECT * FROM earthquakes WHERE longitude BETWEEN -180 AND -130 AND latitude BETWEEN 52 AND 71 ORDER BY magnitude DESC;```

Unified Query:
> ````SELECT * FROM earthquakes WHERE WHERE longitude BETWEEN -180 and -130 AND latitude BETWEEN 52 and 71 AND extract(hour from quaketime) BETWEEN 15 AND 20;```

There were 17 quakes between 12am and 6am Alaska time that occurred in Australia.