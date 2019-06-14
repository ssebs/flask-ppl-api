# people/views/people.py
from flask import Blueprint, jsonify, request
from ..models import Person  # noqa
from .. import db  # noqa

people_routes = Blueprint("people", __name__)

# File Layout
#  - imports
#  - GET routes
#  - POST routes
#  - PUT/PATCH routes
#  - DELETE routes


@people_routes.route("/")
def home():
    return "Person view!"
# home()


# GET
@people_routes.route("/people/", methods=["GET"])
def get_people():
    ret = []
    if request.args:
        if not request.args['q']:
            return jsonify({"Status": "No Query"}), 400
        query = request.args['q']

        for person in Person.query.filter(
            (Person.first_name.like("%{}%".format(query))) |
            (Person.last_name.like("%{}%".format(query))) |
            (Person.email.like("%{}%".format(query)))
        ):
            # print(person)
            ret.append(person.as_dict())
    else:
        for person in Person.query.all():
            ret.append(person.as_dict())
    return jsonify(ret), 200
# get_people()


@people_routes.route("/people/<int:id>", methods=["GET"])
def get_person(id):
    ret = []
    return jsonify(
        Person.query.filter_by(id=id).one().as_dict()
    )
# get_person()


@people_routes.route("/people/<string:query>", methods=["GET"])
def query_person(query):
    ret = []
    for person in Person.query.filter(
        (Person.first_name.like("%{}%".format(query))) |
        (Person.last_name.like("%{}%".format(query))) |
        (Person.email.like("%{}%".format(query)))
    ):
        # print(person)
        ret.append(person.as_dict())
    return jsonify(ret), 200
# query_person()


# POST
@people_routes.route("/people/", methods=["POST"])
def create_person():
    if not request.json:
        return jsonify({"Status": "No Data"}), 400

    data = request.json
    try:
        Person.query.filter_by(email=data["email"]).one()
        return jsonify({"Status": "User exists, try a different email."}), 400
    except:
        pass
    newPerson = Person(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"]
    )
    db.session.add(newPerson)
    db.session.commit()
    return jsonify({
        "Status": "Person Created",
        "Data": Person.query.filter_by(email=data["email"]).one().as_dict()
    }), 201
# create_person()


# PATCH/PUT
@people_routes.route("/people/<int:id>", methods=["PATCH", "PUT", "OPTIONS"])
def update_person(id):
    if request.method == "OPTIONS":
        return jsonify({"Status": "OK"}), 200

    if not request.json:
        return jsonify({"Status": "No Data"}), 400
    data = request.json

    person = Person.query.filter_by(id=id).one()
    person.email = data["email"]
    person.first_name = data["first_name"]
    person.last_name = data["last_name"]

    db.session.commit()
    return jsonify({
        "Status": "Person Updated",
        "Data": person.as_dict()
    }), 200
# update_person()


# DELETE
@people_routes.route("/people/<int:id>", methods=["DELETE", "OPTIONS"])
def delete_person(id):
    if request.method == "OPTIONS":
        return jsonify({"Status": "OK"}), 200
    person = Person.query.filter_by(id=id).one()
    db.session.delete(person)
    db.session.commit()
    return jsonify({"Status": "Person Deleted"}), 204
# delete_person
