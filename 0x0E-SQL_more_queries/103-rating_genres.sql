SELECT g.name, SUM(r.rating) AS rating_sum
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.tv_show_id
JOIN genres g ON tsg.genre_id = g.id
JOIN ratings r ON ts.id = r.show_id
GROUP BY g.name
ORDER BY rating_sum DESC;

