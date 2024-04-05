## SIMPLE QUERIES 
### "Of all earthquakes with a > 4.0 magnitude, which ones have a depth of more than 10 (km?)?"
- ```SELECT * FROM earthquakes WHERE mag > 4.0 AND depth > 10.0;```
- **Answer:** 622

### "Which ones under a 4.0 magnitude have a depth of less than 10 (km?)?"
- ```SELECT * FROM earthquakes WHERE mag < 4.0 AND depth < 10.0;```
- **Answer**: 148

### "At what depths do Texas earthquakes happen?"
- ```SELECT depth FROM earthquakes WHERE place LIKE '%Texas';```
## "What's the average depth for Texas earthquakes in 2023?"
- ```SELECT AVG(depth) FROM earthquakes WHERE place LIKE '%Texas' AND EXTRACT(year from quaketime) = 2023;```
- $7.485$ (km?)

## USING 'SELECT' WITHOUT '*'
### I keep seing this "SELECT *" opener, so I want to see what it means.
- **Intuition:** it'll be replaceable by categories within the data.
- ```SELECT place FROM earthquakes WHERE mag > 4.0 AND depth > 10.0;```
- **Result:** Yup. (Still 622 rows)

### Can I select multiple categories per datapoint?
- ```SELECT place, id from earthquakes WHERE mag > 4;```
- **Answer:** Yes!

### Can I return via a function call?
- ```SELECT (latitude + longitude) FROM earthquakes WHERE mag > 6;```
- **Answer**: Yes!

## FUNCTION CALLS
### "How many earthquakes happened in 2023?"
- ```SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) = 2023;```
- **Answer:** 1250

### "What about ones that are NOT from 2023?"
- ```SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) != 2023;```
- **Answer:** 158

## STRING MANAGEMENT
### "Of all the ones in 2023 which ones' IDs contain the letters 'us'?
- ```SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) = 2023 AND LOWER(id) LIKE '%us%';```
- **Answer:** 924

### "What about the opposite?"
- ```SELECT * FROM earthquakes WHERE EXTRACT(year from quaketime) = 2023 AND LOWER(id) NOT LIKE '%us%';```
- **Answer:** 326

### "Can we do this to check locations? I'd love to see which strings END in 'CA'."
- ```SELECT * FROM earthquakes WHERE place LIKE '%CA';```
- **Answer:** Yes, 75