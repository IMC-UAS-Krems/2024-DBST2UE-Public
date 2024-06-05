## Session 11 - 22/05/24

### Task 1 Normalization

Given the following table:

|StudID |CourseID |StudName |CourseName |Grade| FacName |FacPhone|
|-----|-----|-----|-----|-----|-----|-----|
1 | PROG2, DBSE2UE | Adams | Prog2, Database | 1, 2 | Dhungana, Gambi | 1234, 1122
2 | PROG2 | Jones | Prog2 | 3  | Dhungana | 1234
3 | PROG2 | Smith | Prog2 | 1  | Dhungana | 1234
4 | PROG2, DBSE2UE| Baker | Prog2, Database | 3, 1 | Dhungana, Gambi| 1234, 1122

#### Task 1.1

The above table is susceptible to update anomalies. Provide examples of insertion, deletion, and modification anomalies.

#### Task 1.2
Given the following functional dependencies

- StudID → StudName
- StudID, CourseID → Grade
- CourseID → CourseName
- CourseID → FacName
- FacName → FacPhone

Check if they hold in the above table.

#### Task 1.3

Describe and illustrate the process of normalizing the table shown to 3NF. For each of the steps below list the relations and their Primary Keys

1. 1NF
2. 2NF
3. 3NF 

### Task 2. Transaction

A schedule is an ordering of operations belonging to different transactions. 

A schedule is **serializable** if it is equivalent to a **serial** schedule, which executes all the operations comprising a query before executing the operations that belong to the next query.

Check whether the following schedules are serializable. Explain your answer.

> Note: `READ (A, t)` stands for reading the value of `A` from the DB into the value of variable `t`, whereas `WRITE (A, t)` stands for storing the value of variable `t` into the database as `A`.

### Schedule 1
| T1 | T2 |
|----|----|
|READ (A, t) | | 
| t := t + 100 | |
| WRITE (A, t) | |
| | READ (A, s)| 
| | s := s * 2 |
| | WRITE (A, s) |
| | READ (B, s) |
| | s := s * 2 |
| | WRITE (B, s) |
| READ (B, t) | |
| t := t + 100 | |
| WRITE (B, t) | |

### Schedule 2
| T1 | T2 |
|----|----|
|READ (A, t) | | 
| t := t + 100 | |
| WRITE (A, t) | |
| | READ (A, s)| 
| | s := s * 2 |
| | WRITE (A, s) |
| READ (B, t) | |
| t := t + 100 | |
| WRITE (B, t) | |
| | READ (B, s) |
| | s := s * 2 |
| | WRITE (B, s) |
