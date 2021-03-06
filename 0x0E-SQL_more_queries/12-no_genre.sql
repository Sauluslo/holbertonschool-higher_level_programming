-- 12. No genre
-- Import the database dump from hbtn_0d_tvshows to
-- your MySQL server: download (same as 11-genre_id_all_shows.sql)
-- A Script that lists all shows contained in
-- hbtn_0d_tvshows without a genre linked.
-- (1) Each record should display:
-- tv_shows.title - tv_show_genres.genre_id
-- (2) Results must be sorted in ascending order
-- by tv_shows.title and tv_show_genres.genre_id
-- (3) You can use only one SELECT statement
-- (4) The database name will be passed as an
-- argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
