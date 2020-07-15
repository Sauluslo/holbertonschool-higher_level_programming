-- 14. My genres
-- Import the database dump from hbtn_0d_tvshows to
-- your MySQL server: download (same as 13-count_shows_by_genre.sql)
-- A Script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter.
-- (1) The tv_shows table contains only one record
-- (2) where title = Dexter (but the id can be different)
-- (3) Each record should display: tv_genres.name
-- (4) Results must be sorted in ascending order by the genre name
-- (5) You can use only one SELECT statement
-- (6) The database name will be passed as an argument of the mysql command
SELECT name
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
