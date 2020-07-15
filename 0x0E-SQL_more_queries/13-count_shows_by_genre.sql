-- 13. Number of shows by genre
-- Import the database dump from hbtn_0d_tvshows to
-- your MySQL server: download (same as 12-no_genre.sql)
-- A Script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
-- (1) Each record should display:
-- <TV Show genre> - <Number of shows linked to this genre>
-- (2) First column must be called genre
-- (3) Second column must be called number_of_shows
-- (4) Don’t display a genre that doesn’t have any shows linked
-- (5) Results must be sorted in descending
-- order by the number of shows linked
-- (6) You can use only one SELECT statement
-- (7) The database name will be passed
-- as an argument of the mysql command
SELECT name AS 'genre', COUNT(*) AS 'number_shows'
FROM tv_genres, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
