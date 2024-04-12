SELECT * FROM us_cities JOIN us_states on us_cities.home_state = us_states.state LIMIT 10;

CREATE VIEW 
    city_state 
AS 
    SELECT * 
    FROM 
        us_cities JOIN us_states 
    ON 
        us_cities.home_state = us_states.state;

SELECT 
    city, 
    state, 
    CAST(city_pop as REAL)/state_pop AS percent_pop 
FROM 
    city_state 
ORDER BY
    percent_pop DESC 
LIMIT 10;

/* 
    city     |        state         |     percent_pop     
-------------+----------------------+---------------------
 Washington  | District of Columbia |  0.9811137771990293
 New York    | New York             | 0.42569332359037504
 Anchorage   | Alaska               | 0.40849318340997814
 Albuquerque | New Mexico           | 0.26683087421580265
 Honolulu    | Hawaii               | 0.24506449529114988
 Omaha       | Nebraska             |  0.2308542691667247
 Phoenix     | Arizona              | 0.22481922262609552
 Las Vegas   | Nevada               |  0.2125632110750629
 Chicago     | Illinois             | 0.21107605402862292
 Sioux Falls | South Dakota         | 0.19301550092302283
*/