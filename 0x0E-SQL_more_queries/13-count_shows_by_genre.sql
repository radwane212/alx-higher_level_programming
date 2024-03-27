SELECT g.name AS genre, COUNT(tg.tv_show_id) AS number_of_shows
FROM genre g
JOIN tv_show_genre tg ON g.id = tg.genre_id
GROUP BY g.name
HAVING COUNT(tg.tv_show_id) > 0
ORDER BY COUNT(tg.tv_show_id) DESC;

