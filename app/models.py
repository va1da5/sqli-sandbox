from . import db


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "created": self.created,
            "admin": self.admin,
        }