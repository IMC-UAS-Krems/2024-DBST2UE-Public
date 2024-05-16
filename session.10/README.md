# Session 10 - 15/05/24

## Task 2. Query Optimization

Given the following schema:

```
Student(sid, name, age, address)
Book(bid, title, author)
Checkout(sid, bid, date)
```

And assuming:

- There are 10,000 Student records stored on 1,000 pages.
- There are 50,000 Book records stored on 5,000 pages.
- There are 300,000 Checkout records stored on 15,000 pages. 
- There are 500 different authors.
- Student ages range from 7 to 24.

### Task 2.1:
Show the canonical query execution tree for the following query.


```    
    SELECT S.name
    FROM Student S, Book B, Checkout C
    WHERE S.sid = C.sid
    AND B.bid = C.bid
    AND B.author = 'Olden Fames'
    AND S.age > 12
    AND S.age < 20
```

### Task 2.2
Suggest an alternative (optimized) query plan for the query of Task 2.1.

### Task 2.3

Consider the following Relational Model:

```
R(a,b)
S(b,c)
T(b,d)
U(b,e)
```

For the following SQL query, give two equivalent query execution plans such that one is likely to be more efficient than the other. 

```
    SELECT R.a
    FROM R, S
    WHERE R.b = S.b AND
          S.c = 3
```

Indicate which one is likely to be more efficient. Explain.

## Task 3. Hands on 

For this exercise, we need to use an existing database. Among the many sample databases that you find around (e.g., [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html)) we use the `employee data` a large dataset that includes data and test/verification suite.

The dataset is available also on GitHub:
[https://github.com/datacharmer/test_db](https://github.com/datacharmer/test_db)

### Setup the DB

Before we can use it with MariaDB, we need to run a new container:

```
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d mariadb:10.6
```

Now, we connect to the running container and start the `bash` interpreter:

```
docker exec -it mariadbtest /bin/bash
```

You should see a prompt like this:

```
root@25712fc19ceb:/# 
```

At this point, we can run commands just like regular (Linux/Unix) shell/terminal.

First, we update the local package repository:

```
root@25712fc19ceb:/# apt-get update
```

Next, we install git:
```
root@25712fc19ceb:/# apt-get install git
```

Then, we clone the Employee DB repo from GitHub:

```
root@25712fc19ceb:/# git clone https://github.com/datacharmer/test_db.git
```

We load the database

```
root@25712fc19ceb:/# cd test_db
root@25712fc19ceb:/test_db#: mariadb --user root -pmypass < employees.sql 
```

Next, we test it:

```
root@25712fc19ceb:/test_db# mariadb --user root -pmypass -t < test_employees_md5.sql

```

Finally, we exit from the (bash) container:
```
root@25712fc19ceb:/test_db# exit
```

At this point, we have a (large) database available inside the running docker container and we can connect to it for running queries:

```
docker exec -it mariadbtest mariadb --user root -pmypass
```

>> NOTE: This time we execute the command `mariadb` to start the interpret directly in the container. We could also execute `/bin/bash` and then invoke `mariadb`.

### Task 3.1

- Using the `EXPLAIN` and `ANALYZE` commands, execute the following query and find out what execution plan is used to run it.

```
EXPLAIN SELECT * FROM salaries WHERE salary > 150000;
```

```
ANALYZE SELECT * FROM salaries WHERE salary > 150000;
```
    
- What is the estimated total cost and what the actual total cost of the plan?

- Build an index on the field `salary`. What kind of index was created?

```
CREATE INDEX idx_salary ON salaries(salary);
```

```
SHOW INDEX FROM salaries;
```

- Why there are three indices if we created only one?

>> The primary keys are automatically indexed because they are likely used in JOINs

- Re-run the query and report its execution plan again.

- What is the estimated total cost and what the actual total cost of the plan now?

- Drop the previously created index

```
ALTER TABLE salaries DROP INDEX idx_salary;
```

### Task 3.2

- Using the `EXPLAIN` and `ANALYZE` commands, execute the following query and find out the execution plans chosen to run them.

```
SELECT * FROM employees ORDER BY emp_no;
```
  
```
SELECT * FROM salaries ORDER BY salary DESC;
```

- What is the estimated total cost and what the actual total cost of the plans?

- Which sorting algorithm was used for each of the queries? Why are they different?

- Build an index for the second query on the field `salary `.

- Re-run the second query and report its execution plan again.

- What is the estimated total cost and what the actual total cost of the plan?

- Check whether the sorting algorithm remained the same or changed after building the index. Explain briefly. 

- Change the second query and report changes in the analysis.

```
SELECT * FROM salaries WHERE salary > 150000 ORDER BY salary;
```

```
SELECT * FROM salaries ORDER BY salary LIMIT 10;
```
```
SELECT * FROM salaries ORDER BY salary LIMIT 1000;
```
```
SELECT * FROM salaries ORDER BY salary LIMIT 10000;
```

- Drop all the previously created indices

### Tear down your docker containers

To kill the docker container, run the following command:

```
docker kill mariadbtest
```

To completely wipe the container out of your system use:

```
docker rm mariadbtest
```

>> Note: `docker rm` works only on killed containers
