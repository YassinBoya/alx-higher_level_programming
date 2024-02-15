-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT tv_shows.title, tv_show_genres.genre_id
from tv_shows
join tv_show_genres
ORDER BY tv_shows.title, tv_show_genres.genre_id;
