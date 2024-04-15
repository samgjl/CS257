DROP TABLE IF EXISTS us_cities;
CREATE TABLE us_cities (
  city text,
  home_state text,
  city_pop integer,
  lat real,
  lon real
);
-- \copy us_cities FROM 'us_cities.csv' DELIMITER ',' CSV;

DROP TABLE IF EXISTS us_states;
CREATE TABLE us_states (
    code char(2),
    state text,
    state_pop integer 
);
-- \copy us_states FROM 'us-state-pop.csv' DELIMITER ',' CSV;


-- CREATE TABLE us_combined as SELECT * FROM us_cities JOIN us_states on us_cities.home_state = us_states.state;