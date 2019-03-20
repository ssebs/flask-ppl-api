#!/bin/python3

# query.py
# perform queries for SQL/etc

import os.path
import sqlite3
from sqlite3 import Error as SQError

class Query():

    def __init__(self, db_file="_backend/test.db"):
        '''
        SQLite connection object that can run queries against a specified db
        '''
        self.db_exists(db_file)
        self.conn = self.create_conn(db_file)
        
    #init

    def create_conn(self,p_db_file):
        '''
        Create db connection
        :return: db connection var
        '''
        try:
            connection = sqlite3.connect(p_db_file, check_same_thread=False)
            return connection
        except SQError as e:
            print(e)
        return None
    #create_conn

    def run_select_qry(self,p_qry):
        '''
        Run sql SELECT query
        :return: list of rows
        '''
        cur = self.conn.cursor()
        cur.execute(p_qry)
        rows = cur.fetchall()
        return list(rows)
    #run_qry

    def run_insert_qry(self, p_qry, p_vars_tupl):
        '''
        Run sql INSERT query
        :return: new ID
        '''
        cur = self.conn.cursor()
        cur.execute(p_qry, p_vars_tupl)
        self.conn.commit()
        return cur.lastrowid
    #run_insert_qry

    def run_update_qry(self, p_qry, p_vars_tupl):
        '''
        Run sql UPDATE query
        '''
        cur = self.conn.cursor()
        cur.execute(p_qry, p_vars_tupl)
        self.conn.commit()
    #run_update_qry

    def run_delete_qry(self, p_qry, p_var_id):
        '''
        Run sql DELETE query
        '''
        cur = self.conn.cursor()
        cur.execute(p_qry, p_var_id)
        self.conn.commit()
    #run_update_qry

    def db_exists(self,dbname):
        '''Checks if db file exists, if not, create it
        :return: 0 if it exists, 1 if not and it gets created
        '''
        if dbname[-3:] == ".db":
            dbname = dbname[:-3]
        if dbname.startswith("_backend/"):
            dbname = dbname[9:]

        if not os.path.isfile("_backend/" + dbname + ".db"):
            os.system("cd _backend && sh ./init_db.sh " + dbname)
            return 1
        else:
            return 0
    #db_exists

#class Query