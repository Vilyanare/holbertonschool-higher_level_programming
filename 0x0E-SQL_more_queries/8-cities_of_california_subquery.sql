-- Lists all cities of California in hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities
WHERE state_id =
    (SELECT id
    FROM states
    WHERE name = 'California')
