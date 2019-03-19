#!/bin/python3

from util import query

# main.py
# The main file used to run API service from angular <-> sqlite
#
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

# TODO: Add POST's & UPDATE's


@app.route('/')
@app.route('/people/')
@app.route('/people/%')
@app.route('/people/all')
def get_all_people():
    db = query.Query("people.db")
    ret = []
    for t in db.run_select_qry("SELECT * FROM People;"):
        tmp = {
            "id": t[0],
            "first": t[1],
            "last": t[2],
            "email": t[3]
        }
        ret.append(tmp)
    # print(ret)
    return json.dumps(ret)
    # return str(ret).replace("'",'"')
# get_all_people


@app.route('/people/<int:param>')
@cross_origin()
def get_person_by_id(param):
    db = query.Query("people.db")
    ret = []
    for t in db.run_select_qry("SELECT * FROM People WHERE id = '" + str(param) + "';"):
        tmp = {
            "id": t[0],
            "first": t[1],
            "last": t[2],
            "email": t[3]
        }
        ret.append(tmp)
    return json.dumps(ret)
# get_person_by_id


@app.route('/people/<string:param>')
@cross_origin()
def get_person_by_name(param):
    db = query.Query("people.db")
    ret = []
    for t in db.run_select_qry("SELECT * FROM People WHERE first_name like '" + str(param) + "%' or last_name like '" + str(param) + "%' ;"):
        tmp = {
            "id": t[0],
            "first": t[1],
            "last": t[2],
            "email": t[3]
        }
        ret.append(tmp)
    return json.dumps(ret)
# get_person_by_name

# TODO: Make this a POST
@app.route('/people/create/')
@cross_origin()
def create_person():
    # sample request: /people/create/?first=blah&last=foo's&email=foo-3@bar.com

    db = query.Query("people.db")

    qry = "INSERT INTO People VALUES (NULL, ?, ?, ?);"
    var_tupl = (request.args['first'],
                request.args['last'], request.args['email'])
    db.run_insert_qry(qry, var_tupl)
    return '{"status": "OK"}'
# create_person

# TODO: Make this a PATCH
@app.route('/people/update', methods=['PATCH'])
@cross_origin()
def update_person():
    # note that request needs data in all the fields
    # sample request: /people/update/3 , data = {id:3, first:"tom", last:"selic", email: "tselic@test.com"}
    data = request.json
    db = query.Query("people.db")

    qry = "UPDATE People SET first_name=?, last_name=?, email=? WHERE id = ?;"
    var_tupl = (data['first'], data['last'], data['email'], data['id'])
    
    db.run_update_qry(qry, var_tupl)
    return '{"status": "OK"}'
# create_person

# TODO: Make this a POST
@app.route('/people/delete/')
@cross_origin()
def delete_person():
    db = query.Query("people.db")
    qry = "DELETE FROM People WHERE id = ?;"
    var_id = request.args['id']
    db.run_delete_qry(qry, var_id)
    return '{"status": "OK"}'
# delete_person


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
