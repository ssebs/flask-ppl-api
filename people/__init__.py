# people/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db_name = "people.db"

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../" + db_name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "testfoobar"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views.people import people_routes  # noqa
app.register_blueprint(people_routes)
