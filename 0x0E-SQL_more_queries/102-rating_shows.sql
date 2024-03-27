SELECT ts.title, SUM(r.rating) AS rating_sum
FROM tv_shows ts
JOIN ratings r ON ts.id = r.show_id
GROUP BY ts.title
ORDER BY rating_sum DESC;

