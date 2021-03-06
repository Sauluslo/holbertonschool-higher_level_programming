-- 1. Genre ID for all shows
-- Import the database dump of hbtn_0d_tvshows to
-- your MySQL server: download (same as 10-genre_id_by_show.sql)
-- A Script that lists all shows contained in the database hbtn_0d_tvshows.
-- (1) Each record should display: tv_shows.title - tv_show_genres.genre_id
-- (2) Results must be sorted in ascending order
-- by tv_shows.title and tv_show_genres.genre_id
-- (3) If a show doesn’t have a genre, display NULL
-- (4) You can use only one SELECT statement
-- (5) The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
