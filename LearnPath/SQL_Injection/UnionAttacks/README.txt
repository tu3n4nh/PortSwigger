 The UNION keyword lets you execute one or more additional SELECT queries and append the results to the original query. 
For example:
SELECT a, b FROM table1 UNION SELECT c, d FROM table2

This SQL query will return single result with two columns, containing values form columns a and b in table1 and c and d in table.

For a UNION query to work. two key requirements must be met:
    - The individual queries must return the same number of columns.
    - The data types in each column must be compatible between the individual queries.

To carry out the UNION attack, you need ensure that the application has two requirements above. This genarally involves figuring out:
    - The number of columns in the original query return.
    - Which columns returned from the original query are of a suitable data type to hold the results of the UNION attack.