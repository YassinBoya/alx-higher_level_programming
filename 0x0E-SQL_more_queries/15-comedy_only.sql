--a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT tv_shows.title as 'Title' From tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE Title = 'Comedy'
ORDER BY Title;
