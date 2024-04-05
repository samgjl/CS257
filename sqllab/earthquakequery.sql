----+ SIMPLE QUERIES +----
-- "Of all earthquakes with a > 4.0 magnitude, 
-- which ones have a depth of more than 10 (km?)?"
-- * Answer: 622
SELECT * FROM earthquakes WHERE mag > 4.0 AND depth > 10.0;
-- "Which ones under a 4.0 magnitude have a depth of less than 10 (km?)?"
SELECT * FROM earthquakes WHERE mag < 4.0 AND depth < 10.0;
-- "What's the average depth for Texas earthquakes in 2023?"
-- * Answer: 7.485 (km?)
SELECT AVG(depth) FROM earthquakes WHERE place LIKE '%Texas' AND EXTRACT(year from quaketime) = 2023;

--+ USING 'SELECT' WITHOUT '*' +--
-- I keep seing this "SELECT *" opener, so I want to see what it means
-- * Intuition: it'll be replaceable by categories within the data.
-- * Result: Yup. (Still 622 rows)
SELECT place FROM earthquakes WHERE mag > 4.0 AND depth > 10.0;
-- Can I select multiple categories per datapoint?
-- * Answer: Yes!
SELECT place, id from earthquakes WHERE mag > 4;
-- Can I return via a function call?
-- * Answer: Yes!
SELECT (latitude + longitude) FROM earthquakes WHERE mag > 6;

----+ FUNCTION CALLS +----
-- "How many earthquakes happened in 2023?"
-- * Answer: 1250
SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) = 2023;
-- "What about ones that are NOT from 2023?"
-- * Answer: 158
SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) != 2023;

--+ STRING MANAGEMENT +--
-- "Of all the ones in 2023 which ones' IDs contain the letters 'us'?
-- * Answer: 924
SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) = 2023 AND LOWER(id) LIKE '%us%';
-- "What about the opposite?"
-- * Answer: 326
SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) = 2023 AND LOWER(id) NOT LIKE '%us%';
-- "Can we do this to check locations? I'd love to see which strings END in 'CA'."
-- * Anser 75
SELECT * FROM earthquakes WHERE place LIKE '%CA';