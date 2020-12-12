SELECT Table1.id, Table1.name, Table2.id,Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;

SELECT Table1.id, Table1.name, Table2.id,Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;

SELECT Table1.id, Table1.name, Table2.id,Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id
