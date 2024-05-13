SELECT f.name
FROM Frequents f
GROUP BY f.name
HAVING COUNT(DISTINCT f.pizzeria) = (
    SELECT COUNT(DISTINCT a.pizzeria)
    FROM (
        SELECT s.pizzeria
        FROM Eats e, Serves s
        WHERE e.pizza = s.pizza AND e.name = f.name
        INTERSECT
        SELECT f0.pizzeria
        FROM Frequents f0
        WHERE f0.name = f.name
    ) a
);