-- 15. Only Comedy
-- Import the database dump from hbtn_0d_tvshows to
-- your MySQL server: download (same as 14-my_genres.sql)
-- A Script that lists all Comedy shows in
-- the database hbtn_0d_tvshows.
-- (1) The tv_genres table contains only one record
-- (2) where name = Comedy (but the id can be different)
-- (3) Each record should display: tv_shows.title
-- (4) Results must be sorted in ascending
-- order by the show title
-- (5) You can use only one SELECT statement
-- (6) The database name will be passed
-- as an argument of the mysql command
SELECT title FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
