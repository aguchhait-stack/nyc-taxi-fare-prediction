SELECT count(*)
FROM taxi_trips
LIMIT 10;

SELECT COUNT(CASE WHEN passenger_count IS NULL THEN 1 END)*100.00/COUNT(*)
FROM taxi_trips;

SELECT distinct extract(year FROM tpep_pickup_datetime::DATE)
from taxi_trips;
