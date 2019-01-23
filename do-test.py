import unittest
import sqlite3
import os
import json

from util.query import Query

from main import app
from unittest import TestCase
## do-test.py
# tests for Query.py. 
# Shoule be run from Makefile!!
##

class TestQuery(unittest.TestCase):

    def setUp(self):
        # setup flask for testing
        self.app = app.test_client()
    #setUp

    def test_qry_select(self):
        db_name = "_backend/foo-test.db"
        sql_tbl = "CREATE TABLE People (id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT);"
        sql_ins = "INSERT INTO People VALUES(NULL, 'Bob', 'Smith', 'bob.smith+test@example.com');"
        sql_qry = "SELECT * FROM People;"

        select_data = []

        db_conn = sqlite3.connect(db_name)
        c = db_conn.cursor()

        c.execute(sql_tbl)
        c.execute(sql_ins)
        db_conn.commit()
        c.execute(sql_qry)
        select_data = c.fetchall()

        qry_obj = Query("_backend/foo-test.db")
        test_list = qry_obj.run_select_qry("SELECT * FROM People;")
        self.assertEqual(select_data, test_list, "Should be a list")
        os.remove(db_name)
    #test_qry

    def test_api_running(self):
        # check if HTTP request to localhost:5000 works
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    #test_api_running

    def test_REST_is_json(self):
        # check if valid json
        response = self.app.get('/people/1')
        # print(json.loads(response.data))
        self.assertTrue(json.loads(response.data))
        pass
    #test_REST_is_json

    def test_REST_by_id(self):
        # select person by id via SQL, then API, check if equal
        response = self.app.get('/people/1')
        f_name = json.loads(response.data)[0]['first']
        self.assertTrue(type(f_name) == type(""))        
    #test_REST_by_id

    def test_REST_by_name(self):
        # select person by name via SQL, then API, check if equal
        response = self.app.get('/people/bob')
        f_name = json.loads(response.data)[0]['first']
        self.assertTrue(type(f_name) == type(""))
    #test_REST_by_id

# end tests for Query.py

if __name__ == '__main__':
    query_suite = unittest.TestLoader().loadTestsFromTestCase(TestQuery)
    unittest.TextTestRunner(verbosity=2).run(query_suite)