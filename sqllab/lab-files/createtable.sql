DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  longitude real,
  depth real,
  mag real,
  id text,
  place text
);