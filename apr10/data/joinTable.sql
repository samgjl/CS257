DROP TABLE us_combined IF EXISTS;
CREATE TABLE us_combined(
    city text,
    state text,
    code real
    pop integer,

)

SELECT * FROM us_cities JOIN us_states on us_cities.state = us_states.state;