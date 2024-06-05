# Session 12 - 05/06/24

## Deadlock

Consider the following two transactions: 

T1: 

```
begin
write C 
read B 
write C 
commit
```

T2: 

```
begin
write B 
read C 
read C 
commit
```

### Task 1 
In a DBMS using the two-phase locking algorithm, whether transactions will cause deadlocks depends on how they are executed. If the above two transactions are executed concurrently, under what situations can a deadlock occur?

### Task 2
In a DBMS that has not implemented any concurrency control algorithms, can **non-repeatable reads** occur if the above two transactions are executed concurrently? 

### Task 3

Given the following schedule:

| Tr  | 1     | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
|-----|-------|------|------|------|------|------|------|------|------|
| 1   | S(A)  | S(D) |      | S(B) |      |      |      |      |      |
| 2   |       |      | X(B) |      |      |      | X(C) |      |      |
| 3   |       |      |      |      | S(D) | S(C) |      |      | X(A) |
| 4   |       |      |      |      |      |      |      | X(B) |      | 

#### Task 3.1 
Check if the schedule leads to a deadlock when all the locks are exclusive 

#### Task 3.2
Check if the situation changes if we can distinguish between shared and exclusive locks.

> Note: The following table shows the lock compatibility of Shared (S) and Exclusive (X) locks:


|   | **S** | **X** |
|---|---|---|
| **S** | OK | – |
| **X** | – | – |