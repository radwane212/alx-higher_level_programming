-- Step 1: Import the table dump into the database hbtn_0c_0
mysql -hlocalhost -uroot -p hbtn_0c_0 < [path_to_your_sql_file]

-- Step 2: Run the script to display the top 3 cities' temperatures during July and August
SELECT city, avg_temp
FROM table_name  -- Replace table_name with the actual name of the table
WHERE month IN ('July', 'August')
ORDER BY avg_temp DESC
LIMIT 3;

