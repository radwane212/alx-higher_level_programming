SELECT ts.title, g.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.tv_show_id
LEFT JOIN genres g ON tsg.genre_id = g.id
ORDER BY ts.title ASC, g.name ASC;

