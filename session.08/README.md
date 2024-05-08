# Session 8 - 24/04/2024

## Task 1: More on Relational Algebra

Making use of the following Operators:

- RENAMING(R)
- UNION (U)
- INTERSECTION (i)
- SET DIFFERENCE (/)
- PROJECTION (P)
- SELECTION (S)
- CARTESIAN PRODUCT (x)

Write the relational algebra expressions corresponding to the following queries in Natural Language and *simulate* their execution on a small dataset.

As a remark, the Relational Model is the following one:

```
Person (name, age, gender)
frequents (Person.name, pizzeria)
eats (Person.name, pizza) 
serves (pizzeria, pizza, price, allergens)
```


1. Find all pizzerias frequented by at least one person under the age of `18`. - Done

2. Find the names of all `female`s who can eat either `mushroom` or `pepperoni` pizzas (but NOT both). - Done

3. Find the names of all `female`s who eat both `mushroom` and `pepperoni` pizzas.

4. Find all pizzerias that serve at least one pizza that `Amy` eats for less than `$10.00`.

5. Find all pizzerias that are frequented by only `female`s or only `male`s.

6. For each person, find all pizzas the person eats that are not served by any pizzeria the person frequents. Return all such person name and pizza pairs.

7. Find the names of all people who frequent only pizzerias serving at least one pizza they eat.

8. Find the names of all people who frequent every pizzeria serving at least one pizza they eat.

9. Find the pizzeria serving the cheapest pepperoni pizza. In the case of ties, return all of the cheapest-pepperoni pizzerias.

## Task 2: SQL as Data Definition Language (DDL)

Using SQLIte, implement the `pizza_connection.sql` database from the above Relational Model.

Make sure to define tables with appropriate attributes, domains, constraints, and so on.

## Task 3: SQL as Data Manipulation Language (DML)

Fill up the database with some data. Find a way to automatically generate data but ensure that the referential  integrity, type, and domain  constrains are met!

## Task 4: SQL as Query Language (QL)

Implement the queries from Task 1 into SQL and run them on the `pizza_connection.sql`. If you realize the queries are wrong (i.e., you have a counter example), fix them in SQL and in Relational Algebra.