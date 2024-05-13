# How to use the pizza.tests.sh

Note: this works only on bash/sh/etc. consoles. So no PowerShell, but you can always use an Ubuntu via WLS.


This script shows one of the many possible ways to test queries.

Write the DB schema in the `pizza.db.sql` file

Write the query to test in the `pizza.query.sql` file

Write a file called `pizza.test.<DD>.sh` that contains two functions:
- a setup function (to ins
- an oracle function

<DD> stands for a number made of two digits, so 01, 02 etc.

Invoke the script: `pizza.tests.sh`

Check that no errors are detected. If they are, check the corresponding files to see what was produced (`_actual`) and what was expected (`_expected`)