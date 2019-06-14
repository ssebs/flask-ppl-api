#!/bin/bash
export FLASK_APP=people
export dbName="people.db"

if [ -e $dbName ];then
    echo "Deleting $dbName"
    rm people.db
fi

if [ -e migrations ]; then
    echo "Deleting migrations/"
    rm -rf migrations/
fi

flask db init
flask db migrate
flask db upgrade

sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Bob', 'Smith', 'bob.smith+test@example.com');"
sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Tom', 'Selic', 'Tom.Selic123@example.com');"
sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Jane', 'Doe', 'jdoe45@example.com');"
sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Giselle M.', 'Reyes', 'gmr123@example.com');"
echo "Done, created people.db"