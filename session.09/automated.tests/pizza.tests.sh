#!/bin/bash

# Check preconditions:
if [ ! -f "pizza.db.sql" ]; then
  echo "* Missing file pizza.db.sql. You need this file to setup the empty DB"
  exit 1
fi

if [ ! -f "pizza.query.sql" ]; then
  echo "* Missing file pizza.query.sql. This is the file that contain the query to test."
  exit 1
fi

# Look up for pizza.test.***.sh files
for TEST_FILE in $(find . -iname "pizza.test.*.sh"); do
  echo "Executing tests: ${TEST_FILE}"
  SEED=${RANDOM}
  # Prepare temp files
  DB_NAME=${SEED}_pizza.db
  SETUP_NAME=${SEED}_setup.sql
  EXPECTED_OUTPUT=${SEED}_expected
  ACTUAL_OUTPUT=${SEED}_actual
  
  # Setup the empty DB
  sqlite3 ${DB_NAME} < pizza.db.sql

  # Source the test file
  . ${TEST_FILE}

  # Invoke the script that creates the setup file
  setup_test ${SETUP_NAME}
  
  # Load the data from the setup file
  sqlite3 ${DB_NAME} < ${SETUP_NAME}
  
  # Invoke the script that creates the oracle file
  setup_oracle ${EXPECTED_OUTPUT}
  
  # Invoke the Query - Test Executionn
  sqlite3 ${DB_NAME} < pizza.query.sql > ${ACTUAL_OUTPUT}
  
  # Assert Result
  FAILED=$(cmp --silent ${EXPECTED_OUTPUT} ${ACTUAL_OUTPUT}; echo $?)
  if [ ${FAILED} -ne 0 ]; then
    echo "* Test FAILED!. Check ${SEED} Files!"
  else
    echo "* Test PASSED!"
    # Clean up the mess
    rm -f ${SEED}_*
  fi
done





