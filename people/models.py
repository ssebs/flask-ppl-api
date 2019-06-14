# people/models.py
from . import db  # noqa


# ~~ People Model ~~ #
class Person(db.Model):
    __tablename__ = "People"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(64))

    def __repr__(self):
        return "Person {} - {} {} - {}".format(self.id, self.first_name, self.last_name, self.email)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
# Person()
