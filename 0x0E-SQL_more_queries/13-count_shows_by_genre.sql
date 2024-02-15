-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genre.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_show_genres
join tv_genres
ON tv_genre.id = tv_show_genres.genre_id
GROUP BY tv_genre.name
ORDER BY number_shows DESC; 