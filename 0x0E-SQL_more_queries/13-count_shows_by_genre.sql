-- Lists all genres in hbtn_0d_tvshows and how many shows linked to them
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
LEFT OUTER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
