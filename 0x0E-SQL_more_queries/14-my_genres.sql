SELECT g.name
FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
JOIN tv_shows ts ON tsg.tv_show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY g.name ASC;

