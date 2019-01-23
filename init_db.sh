#!/bin/bash
dbName="people.db"

function create_db() {
    sqlite3 $dbName "CREATE TABLE People (id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT);"

    sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Bob', 'Smith', 'bob.smith+test@example.com');"
    sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Tom', 'Selic', 'Tom.Selic123@example.com');"
    sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Jane', 'Doe', 'jdoe45@example.com');"
    sqlite3 $dbName "INSERT INTO People VALUES(NULL, 'Giselle M.', 'Reyes', 'gmr123@example.com');"

    echo "$dbName has been created"
    echo ""
    #echo "schema below:"
    #sqlite3 $dbName ".schema"
}

function proc() {
    if [ ! -e $dbName ]; then
        create_db
    else
        read -p "$dbName file already exists. Do you want to delete this file? [y/N] " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm $dbName
            echo "Old $dbName deleted"
            create_db
        else
            echo "$dbName not deleted"
        fi
    fi
}

if [ ! -e $1 ]; then
    dbName="$1.db"
    proc
else
    proc
fi
