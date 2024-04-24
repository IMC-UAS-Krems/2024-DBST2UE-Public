# Session 5 - 10/04/2024

### Task 1: From RM to ER and Back

#### Step 1: Lift up RM
Consider an incomplete database schema containing the following Relations:

```
Person (name, age, gender)
frequents (Person.name, pizzeria)
eats (Person.name, pizza) 
serves (pizzeria, pizza, price, allergens)
```

> NOTE: Limit gender to male/female/other

Reverse engineer a possible ER Model that could be used to generate such an incomplete Relation Model.

#### Step 2: Complete the ER Model
Complete the ER Model by adding the missing details, such as attributes, relationships, cardinality/participation constrains. Identify possible keys/superkeys, and missing strong and weak entities.

#### Step 3: Remap the (completed) ER model into RM
Make sure to select primary keys and create appropriate references (i.e., connections via primary and foreign keys) between the various Relations.

### Task 2: Implement the database in SQLite3

- Read online about which queries and SQL operators to use for creating tables and defining constraints and references.
_Hint_: SQL is used as Data Definition Language (DDL)

> Note: Refrain from using ChatGPT or similar tools; instead, face the challenge of understanding something on your own!

- Write pytest fixtures to insert data in a temporary databases. Start by having a method that creates the DB, then write additional methods to insert data.

- Discuss how one can generate test data (e.g., names of persons, pizzas, allergens, etc.). Are there datasets that can be used? Is the use of Generative AI (e.g., ChatGPT) meaningful here?

### Task 3: Relational Algebra
Making use of the following Operators:

- RENAMING(R)
- UNION (U)
- INTERSECTION (i)
- SET DIFFERENCE (/)
- PROJECTION (P)
- SELECTION (S)
- CARTESIAN PRODUCT (x)

Write the relational algebra expressions corresponding to the following queries in Natural Language and *simulate* their execution on a small dataset (from Task 2)

1. Find all pizzerias frequented by at least one person under the age of `18`.

2. Find the names of all `female`s who can eat either `mushroom` or `pepperoni` pizzas (but NOT both)

3. Find the names of all `female`s who eat both `mushroom` and `pepperoni` pizzas.

4. Find all pizzerias that serve at least one pizza that `Amy` eats for less than `$10.00`.

5. Find all pizzerias that are frequented by only `female`s or only `male`s.

6. For each person, find all pizzas the person eats that are not served by any pizzeria the person frequents. Return all such person name and pizza pairs.

7. Find the names of all people who frequent only pizzerias serving at least one pizza they eat.

8. Find the names of all people who frequent every pizzeria serving at least one pizza they eat.

9. Find the pizzeria serving the cheapest pepperoni pizza. In the case of ties, return all of the cheapest-pepperoni pizzerias.