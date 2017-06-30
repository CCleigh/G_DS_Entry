#SQL query that retrieves the name of all salespeople that have more than one 
#order from the tables proved; assuming each salesperson only has one ID.

SELECT Name 
From Orders, Salesperson 
WHERE Orders.salesperson_id = Salesperson.ID
GROUP BY salesperson_id, Name
HAVING COUNT (salesperson_id) > 1
