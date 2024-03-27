-- The script deletes the hbtn_0c_0 database on the MySQL server if it does not exist.
/*
    - **DROP DATABASE:** Tells MySQL you want to delete a database.
    - **IF EXISTS:** Ensures it won't fail if the database isn't there.
    - **hbtn_0c_0:** The name of the database you want to delete.
*/
DROP DATABASE IF EXISTS hbtn_0c_0;
