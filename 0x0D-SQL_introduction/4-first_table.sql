-- The script creates a table called first_table in the current database in MySQL server.
/*
    - CREATE TABLE: Creates a new table.
    - IF NOT EXISTS: Ensures table creation only if it doesn't already exist.
    - first_table: The name of the new table.
    - id INT: An integer column named "id".
    - name VARCHAR(256): A text column named "name" with a maximum length of 256 characters.
*/
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
