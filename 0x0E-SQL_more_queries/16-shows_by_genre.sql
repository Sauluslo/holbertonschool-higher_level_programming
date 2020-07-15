-- 16. List shows and genres
-- Import the database dump from hbtn_0d_tvshows
-- to your MySQL server: download (same as 15-comedy_only.sql)
-- A Script that lists all shows, and all genres linked
-- to that show, from the database hbtn_0d_tvshows.
-- (1) If a show doesn’t have a genre,
-- display NULL in the genre column
-- (2) Each record should display:
-- tv_shows.title - tv_genres.name
-- (3) Results must be sorted in ascending
-- order by the show title and genre name
-- (4) You can use only one SELECT statement
-- (5) The database name will be passed
-- as an argument of the mysql command
SELECT tv_shows.title, tv_genres.nameFROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
