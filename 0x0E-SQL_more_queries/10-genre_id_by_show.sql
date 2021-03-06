-- 10. Genre ID by show
-- Import the database dump from hbtn_0d_tvshows
-- to your MySQL server: download
-- A Script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
-- (1) Each record should display: tv_shows.title - tv_show_genres.genre_id
-- (2) Results must be sorted in ascending order by
-- tv_shows.title and tv_show_genres.genre_id
-- (3) You can use only one SELECT statement
-- (4) The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
