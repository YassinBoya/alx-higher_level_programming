-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT * from states.cities WHERE state_id = 1 ORDER BY cities.id;
